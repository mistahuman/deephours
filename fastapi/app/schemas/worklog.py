from pydantic import BaseModel, Field
from app.models.project import ProjectModel
from app.models.worklog import WorklogModel
from typing import Optional, List
from app.utils.helpers import PyDate, PyObjectId

class WorklogCreate(BaseModel):
    day: str
    worked_hours: int = Field(..., ge=0, le=24, description="Worked hours (0-24)")
    descr: Optional[str] = None
    ref_activity: str 

class WorklogOut(WorklogModel):
    project: ProjectModel


class WorklogCollection(BaseModel):
    worklogs: List[WorklogOut]


class WorklogStats(BaseModel):
    id: str
    label: str
    color: str
    start: int
    end: int
    total_hours: int
    perc: int

class WorklogStatsCollection(BaseModel):
    
    stats: List[WorklogStats]


class UpdateWorklogModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """
    
    day: PyDate = None
    worked_hours: Optional[int] = None
    descr: Optional[str] = None
    ref_activity: Optional[PyObjectId] = None
    model_config = {
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "date": "2024-02-02",
                "worked_hours": 8,
                "descr": "Sviluppo nuova feature",
                "ref_activity": "65b2f5d2e34a1b1234567890"
            }
        },
    }