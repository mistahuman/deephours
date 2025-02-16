import random 
from datetime import date, datetime
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

def str_to_datetime_midnight(value: str | date | datetime) -> datetime:
    if isinstance(value, datetime):
        # Reset time to midnight
        return datetime.combine(value.date(), datetime.min.time())
    elif isinstance(value, date):
        return datetime.combine(value, datetime.min.time())
    elif isinstance(value, str):
        try:
            dt = datetime.fromisoformat(value)
            return datetime.combine(dt.date(), datetime.min.time())
        except ValueError:
            raise ValueError(f"Invalid date format: {value}. Expected ISO format (YYYY-MM-DD).")
    else:
        raise TypeError(f"Unsupported type for 'day': {type(value)}. Expected str, date, or datetime.")

PyDate = Annotated[datetime, BeforeValidator(str_to_datetime_midnight)]

PyObjectId = Annotated[str, BeforeValidator(str)]

def random_rgba():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    a = round(random.uniform(0.5, 1), 2) 
    return f'rgba({r},{g},{b},{a})'
