"""Configuration for API """

# project/main/app/config.py

import logging
import os
from functools import lru_cache

from pydantic import BaseSettings
from pydantic.networks import AnyUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """
    Class to set BasicSettings as dependency
    """

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = bool(os.getenv("TESTING", False))
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    """
    environment settings dependency function
    """
    log.info("Loading Settings from the environment...")
    return Settings()
