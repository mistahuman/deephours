import os
from motor.motor_asyncio import AsyncIOMotorClient
from app.crud.project import ProjectCRUD
from app.crud.worklog import WorklogCRUD
from app.conf.config import Config


DB_NAME = Config.app_settings.get('db_name')
MONGO_URI = Config.app_settings.get('mongodb_url')
motor_client = AsyncIOMotorClient(MONGO_URI)

def get_project_db() -> ProjectCRUD:
    db = motor_client[DB_NAME]  
    return ProjectCRUD(db)

def get_worklog_db() -> WorklogCRUD:
    db = motor_client[DB_NAME]  
    return WorklogCRUD(db)

