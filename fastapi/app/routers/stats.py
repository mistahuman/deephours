from fastapi import Body, status, APIRouter, Depends, HTTPException
from fastapi.responses import Response
from app.crud.worklog import WorklogCRUD
from app.schemas.worklog import WorklogStatsCollection
from app.dependencies import get_worklog_db



router = APIRouter(prefix="/stats", tags=["stats"])


@router.get(
	"/", 
	response_description="Stats all worklogs",
	response_model=WorklogStatsCollection,
	response_model_by_alias=False,
)       
async def get_all_stats(db: WorklogCRUD = Depends(get_worklog_db)):
	"""
	Stats worklogs data in the database.

	"""
	return await db.get_stats()
