import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class Configs:
    # base
    ENV: str = os.getenv("ENV", "dev")
    API: str = "/api"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "N5 TRANSIT RECORD"

    PROJECT_ROOT: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # auth
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    TOKEN_TIME: int = os.getenv("TOKEN_TIME", "10")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = (int(TOKEN_TIME))

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    # database
    DB_NAME: str = os.getenv("DB_NAME", "db_dev")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_ENGINE: str = "postgresql"

    DATABASE_URI = "{db_engine}://{user}:{password}@{host}:{port}/{database}".format(
        db_engine=DB_ENGINE,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )

    PAGE = 1
    PAGE_SIZE = 50
    ORDERING = "-id"
