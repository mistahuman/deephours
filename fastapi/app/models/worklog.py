from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator



def date_to_datetime(value: str | datetime) -> datetime:
    if isinstance(value, datetime):
        # Se è già un datetime, restituiscilo senza modifiche
        return value
    elif isinstance(value, date):
        # Se è un date, combinalo con l'ora 00:00:00
        return datetime.combine(value, datetime.min.time())
    elif isinstance(value, str):
        # Se è una stringa, prova a parsarla come data ISO
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            raise ValueError(f"Invalid date format: {value}. Expected ISO format (YYYY-MM-DD).")
    else:
        raise TypeError(f"Unsupported type for 'day': {type(value)}. Expected str, date, or datetime.")

PyDate = Annotated[datetime, BeforeValidator(date_to_datetime)]

PyObjectId = Annotated[str, BeforeValidator(str)]

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
