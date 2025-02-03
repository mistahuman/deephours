from typing import Optional
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class ProjectModel(BaseModel):
    """
    Model for a project
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(..., description="Title of project")
    code: str = Field(..., description="Code of project")
    description: Optional[str] = Field(None, description="Description of project")

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "title": "Dev business software",
                "code": "DBS01",
                "description": "Blablablabla"
            }
        }
    }