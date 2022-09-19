import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE: str="Jobboard"
    PROJECT_VERSION: str="0.1.1"
    
    POSTGRES_USER : str = os.getenv("POSTGES_USER")
    POSTGRES_PASSWORD : str = os.getenv("POSTGES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGES_PORT",5432)
    POSTGRES_DB : str = os.getenv("POSTGES_DB","db_course")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}" 
    
settings = Settings() 