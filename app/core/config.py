import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ACCESS_TOKEN: str | None = None
    EXPIRE_TIME: float | None = None
    CLIENT_ID: str
    CLIENT_SECRET: str
    DB_PATH: str = "tour_agent.db"
    APP_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR: str = os.path.join(APP_DIR, "templates")

    class Config:
        env_file = ".env"

settings = Settings()