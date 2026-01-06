import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

DBBaseModel = declarative_base()


class Settings(BaseSettings):
    # API
    API_V1_STR = os.getenv('API_V1_STR')    
    # DATABASE
    DATABASE_URL = os.getenv('DATABASE_URL')
    # JWT
    JWT_SECRET = os.getenv('JWT_SECRET')
    ALGORITHM = os.getenv('ALGORITHM')
    ACESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACESS_TOKEN_EXPIRE_MINUTES')

    class Config:
        case_sensitive = True


settings = Settings()