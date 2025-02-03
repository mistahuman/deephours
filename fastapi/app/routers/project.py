from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.project import ProjectCollection, UpdateProjectModel
from app.models.project import ProjectModel
from app.crud.project import ProjectCRUD
from fastapi.responses import Response
from app.dependencies import get_project_db


router = APIRouter(prefix="/projects", tags=["projects"])

# POST /projects
@router.post(
    "/", 
    response_description="Add a new project",
    response_model=ProjectModel, 
	response_model_by_alias=False,
)
async def add_project(proj: ProjectModel, db: ProjectCRUD = Depends(get_project_db)):
    """ ... """
    return await db.create_project(proj)

# GET /projects
@router.get(
    "/",
    response_description="Get project collection",
    response_model=ProjectCollection,
    response_model_by_alias=False,
)
async def get_projects(db: ProjectCRUD = Depends(get_project_db)):
    """ ... """
    return await db.get_projects()

# GET /projects/{id}
@router.get(
    "/{id}",
    response_description="Get a single project",
    response_model=ProjectModel,
    response_model_by_alias=False,
)
async def show_project(id: str, db: ProjectCRUD = Depends(get_project_db)):
    """
    Get the record for a specific project, looked up by `id`.
    """
    proj = await db.show_project(id)
    if proj: 
        return proj
    
    raise HTTPException(status_code=404, detail=f"Project {id} not found")

# PATCH /projects/{id}
@router.patch(
    "/{id}",
    response_description="Update a single project",
    response_model=ProjectModel,
    response_model_by_alias=False,
)
async def update_project(id: str, update_data: UpdateProjectModel, db: ProjectCRUD = Depends(get_project_db)):
    """
    Update the record for a specific project, looked up by `id`.
    """
    proj = await db.update_project(id, update_data)
    if proj: 
        return proj
    
    raise HTTPException(status_code=404, detail=f"Project {id} not found")



# DELETE /projects/{id}
@router.delete(
    "/{id}",
    response_description="Delete a project"
)
async def delete_project(id: str, db: ProjectCRUD = Depends(get_project_db)):
    """
    Remove a single project record from the database if not associated to worklog
    """
    delete_result = await db.delete_project(id)

    if delete_result:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Project {id} not found")

