from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.models.worklog import WorklogModel
from app.models.project import ProjectModel
from app.schemas.worklog import WorklogOut, WorklogCollection, WorklogStatsCollection, WorklogStats, UpdateWorklogModel
import logging
from datetime import datetime
from pymongo import ReturnDocument
from app.utils.helpers import random_rgba

logger = logging.getLogger("main")

class WorklogCRUD:
    def __init__(self, db: AsyncIOMotorClient) -> None:
        self.db = db
        self.collection = db["worklogs"]

    async def create_worklog(self, worklog: WorklogModel) -> WorklogOut | None:
        ret = None
        proj_id = worklog.ref_activity
        project = await self.db["projects"].find_one({"_id": ObjectId(proj_id)})
        if project: #TODO
            
            new_worklog = await self.collection.insert_one(worklog.model_dump(by_alias=True, exclude=["id"]))
            created_worklog = await self.collection.find_one({"_id": new_worklog.inserted_id})
            ret = WorklogOut(**created_worklog, project=project)

        return ret
    async def get_worklogs_by_month(self, month) -> WorklogCollection:
        worklogs = []
        start_date = datetime.strptime(month, "%Y-%m")
        end_date = datetime(start_date.year, start_date.month + 1, 1) if start_date.month < 12 else datetime(start_date.year + 1, 1, 1)

        async for wl in self.collection.find(
            {"day": {"$gte": start_date, "$lt": end_date}}
        ).sort("day", -1):
            proj_id = wl["ref_activity"]
            data = await self.db["projects"].find_one({"_id": ObjectId(proj_id)})
            if not data: #TODO
                logger.warning(f"Project Id {proj_id} not found. Skipped.")
                continue
            proj = ProjectModel(**data)
            item = WorklogOut(**wl, project=proj)
            worklogs.append(item.model_dump(by_alias=True))

        return WorklogCollection(worklogs=worklogs)
    
    async def get_worklogs(self) -> WorklogCollection:
        worklogs = []
        async for wl in self.collection.find().sort("day", -1):
            proj_id = wl["ref_activity"]
            data = await self.db["projects"].find_one({"_id": ObjectId(proj_id)})
            if not data: #TODO
                logger.warning(f"Project Id {proj_id} not found. Skipped.")
                continue
            proj = ProjectModel(**data)
            item = WorklogOut(**wl, project=proj)
            worklogs.append(item.model_dump(by_alias=True))

        return WorklogCollection(worklogs=worklogs)
    
    async def get_stats(self) -> WorklogStatsCollection:
        # TODO refactor this shit
        pipeline = [
            {"$group": {"_id": "$ref_activity", "total_hours": {"$sum": "$worked_hours"}}}
        ]
        worklogs = await self.collection.aggregate(pipeline).to_list(None)

        if not worklogs:
            return WorklogStatsCollection(stats=[])

        project_ids = [ObjectId(wl["_id"]) for wl in worklogs]
        projects = {
            str(p["_id"]): p for p in await self.db["projects"].find({"_id": {"$in": project_ids}}).to_list(None)
        }

        max_hours = 0
        for wl in worklogs:
            max_hours += wl.get('total_hours')

        stats = []
        count_graph = 0
        for wl in worklogs:
            proj_id = wl["_id"]
            total_hours = wl["total_hours"]
            proj_data = projects.get(proj_id)
            perc = int((total_hours / max_hours) * 100)

            if not proj_data:
                logger.warning(f"Project Id {proj_id} not found. Skipped.")
                continue
            
            proj = ProjectModel(**proj_data)
            start = count_graph
            count_graph += perc
            end = count_graph

            stats.append(WorklogStats(
                id=proj_id,
                label=f"{proj.title} ({proj.code})",
                color=random_rgba(), 
                start=start,
                end=end,
                total_hours=total_hours,
                perc=perc
            ))

        return WorklogStatsCollection(stats=stats)
    
    async def show_worklog(self, wl_id) -> WorklogModel:
        return await self.collection.find_one({"_id": ObjectId(wl_id)})
    
    async def update_worklog(self, wl_id: str, update_data: UpdateWorklogModel) -> WorklogModel | None:
        new_proj = {
            k: v for k, v in update_data.model_dump(by_alias=True).items() if v is not None
        }
        result = await self.collection.find_one_and_update(
            {"_id": ObjectId(wl_id)},
            {"$set": new_proj},
            return_document=ReturnDocument.AFTER
        )
        return result

    async def delete_worklog(self, wl_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(wl_id)})
        return result.deleted_count > 0