from pydantic import BaseModel, Field
from app.models.project import ProjectModel
from app.models.worklog import WorklogModel
from typing import Optional, List

class WorklogCreate(BaseModel):
    day: str
    worked_hours: int = Field(..., ge=0, le=24, description="Worked hours (0-24)")
    descr: Optional[str] = None
    ref_activity: str  # Riferimento all'attività come ID stringa

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