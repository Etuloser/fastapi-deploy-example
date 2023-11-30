import os

from configparser import ConfigParser
from pathlib import Path

from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent

config = ConfigParser()
config.read(os.path.join(BASE_DIR, "config", "config.ini"))


class AppSettings(BaseSettings):
    PORT: int = config.get("app", "port")
    DEBUG: bool = config.get("app", "debug")


class DevelopmentSettings(AppSettings):
    """DevelopmentSettings"""


class ProductionSettings(AppSettings):
    """ProductionSettings"""


if os.getenv("environment") == "production":
    settings = ProductionSettings()
else:
    settings = DevelopmentSettings()
