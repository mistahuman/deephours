from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from app.models.project import ProjectModel
from app.schemas.project import ProjectCollection, UpdateProjectModel
from pymongo import ReturnDocument

class ProjectCRUD:
    def __init__(self, db: AsyncIOMotorClient):
        self.db = db
        self.collection = db["projects"]

    async def create_project(self, task: ProjectModel) -> ProjectModel:
        new_task = await self.collection.insert_one(task.model_dump(by_alias=True, exclude=["id"]))
        created_task = await self.collection.find_one({"_id": new_task.inserted_id})
        return created_task

    async def get_projects(self) -> ProjectCollection:
        return ProjectCollection(projects=await self.collection.find().to_list())

    async def show_project(self, proj_id: str) -> ProjectModel | None:
        return await self.collection.find_one({"_id": ObjectId(proj_id)})

    async def update_project(self, proj_id: str, update_data: UpdateProjectModel) -> ProjectModel | None:
        new_proj = {
            k: v for k, v in update_data.model_dump(by_alias=True).items() if v is not None
        }
        result = await self.collection.find_one_and_update(
            {"_id": ObjectId(proj_id)},
            {"$set": new_proj},
            return_document=ReturnDocument.AFTER
        )
        return result

    async def delete_project(self, proj_id: str) -> bool:
        worklog = await self.db["worklogs"].find_one({"ref_activity": proj_id})
        if worklog is not None:
            return False
        result = await self.collection.delete_one({"_id": ObjectId(proj_id)})
        return result.deleted_count > 0
