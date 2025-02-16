from pydantic import BaseModel, Field
from typing import Optional
from app.utils.helpers import PyDate, PyObjectId

class WorklogModel(BaseModel):
    """
    Model for a worklog record.
    """
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    # day: PyDate
    # day: str = Field(..., description="Date")
    day: PyDate = Field(..., description="Date")
    worked_hours: int = Field(..., ge=0, le=24, description="Worked hours (0-24)")
    descr: Optional[str] = Field(None, description="Description of worklog")
    ref_activity: PyObjectId = Field(..., description="ID of the activity this worklog refers to")

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example": {
                "date": "2024-02-02",
                "worked_hours": 8,
                "descr": "Sviluppo nuova feature",
                "ref_activity": "65b2f5d2e34a1b1234567890"
            }
        }
    }
