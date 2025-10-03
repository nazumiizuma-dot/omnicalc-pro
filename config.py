from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    ALLOWED_ORIGINS: List[str] = ["http://localhost:5173"]
    RATE_LIMIT_PER_MINUTE: int = 100
    ENV: str = "development"

    class Config:
        env_file = "../.env"

settings = Settings()
