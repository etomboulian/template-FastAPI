from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import List, Optional, Union

# Pydantic BaseSettings class will attempt to determine the values of any settings
# not passed in as keyword args by reading environment variables with the same name

class Settings(BaseSettings):
    API_V1_PREFIX: str = "/api/v1"

    #BACKEND_CORS_ORIGINS is a list of allowed origins eg ['http://localhost:8080', '...']
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///data.db"

    class Config:
        case_sensitive = True


settings = Settings()
