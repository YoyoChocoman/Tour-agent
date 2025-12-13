from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ACCESS_TOKEN: str | None = None
    EXPIRE_TIME: float | None = None
    CLIENT_ID: str
    CLIENT_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()