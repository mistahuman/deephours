from pydantic import BaseModel
from typing import Optional, List
from app.models.project import ProjectModel
from bson import ObjectId

class ProjectCollection(BaseModel):
    """
    A container holding a list of `ProjectModel` instances.
    """

    projects: List[ProjectModel]


class UpdateProjectModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """
    
    title: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    model_config = {
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "title": "Dev business software",
                "code": "DBS01",
                "description": "alblablalablabl"
            }
        },
    }