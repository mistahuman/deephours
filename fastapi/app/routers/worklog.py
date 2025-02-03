from fastapi import Body, status, APIRouter, Depends, HTTPException
from fastapi.responses import Response
from app.crud.worklog import WorklogCRUD
from app.schemas.worklog import WorklogCreate, WorklogOut, WorklogCollection, WorklogStatsCollection
from app.models.worklog import WorklogModel
from app.dependencies import get_worklog_db
from typing import List

router = APIRouter(prefix="/worklogs", tags=["worklogs"])

@router.post(
	"/",
	response_description="Add new worklog",
	response_model=WorklogOut,
	status_code=status.HTTP_201_CREATED,
	response_model_by_alias=False,
)
async def create_worklog(worklog: WorklogModel = Body(...), db: WorklogCRUD = Depends(get_worklog_db)):
    """
    Insert a new worklog record.

    A unique `id` will be created and provided in the response.
    """
    new_wl: WorklogOut = await db.create_worklog(worklog)
    return new_wl
    

@router.get(
    "/{year_month}",
	response_model=WorklogCollection,
	response_model_by_alias=False,
)
async def get_worklogs_by_month(year_month: str, db: WorklogCRUD = Depends(get_worklog_db)):
    """
	List all of the worklogs data in the database by month
    """
    return await db.get_worklogs_by_month(year_month)


@router.get(
	"/", 
	response_description="List all worklogs",
	response_model=WorklogCollection,
	response_model_by_alias=False,
)       
async def get_all_worklogs(db: WorklogCRUD = Depends(get_worklog_db)):
	"""
	List all of the worklogs data in the database.

	The response is unpaginated.
	"""
	return await db.get_worklogs()


@router.get(
    "/{id}",
    response_description="Get a single project",
    response_model=WorklogModel,
    response_model_by_alias=False,
)
async def show_project(id: str, db: WorklogCRUD = Depends(get_worklog_db)):
    """
    Get the record for a specific worklog, looked up by `id`.
    """
    wl = await db.show_worklog(id)
    if wl: 
        return wl
    
    raise HTTPException(status_code=404, detail=f"Worklog {id} not found")


@router.delete(
    "/{id}",
    response_description="Delete a project"
)
async def delete_project(id: str, db: WorklogCRUD = Depends(get_worklog_db)):
    """
    Remove a single worklog record from the database
    """
    delete_result = await db.delete_worklog(id)

    if delete_result:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Worklog {id} not found")
