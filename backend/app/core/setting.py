from typing import Optional
from pydantic import BaseSettings
import toml
import argparse

""" From pyproject.toml """
project_info = toml.load("./pyproject.toml")

name = project_info["tool"]["poetry"]["name"]
version = project_info["tool"]["poetry"]["version"]
description = project_info["tool"]["poetry"]["description"]

""" From arguments """
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=3001)
parser.add_argument("--env", type=str, default="development")
args = parser.parse_args()


class Settings(BaseSettings):
    PROJECT_NAME: str = name
    PROJECT_VERSION: str = version
    PROJECT_DESCRIPTION: str = description
    PORT: int = args.port
    ENVIRONMENT: str = args.env

    """ From .env """
    SQLALCHEMY_DATABASE_URL: Optional[str] = None

    class Config:
        env_file = f".env.{args.env}"
        env_file_encoding = "utf-8"


settings = Settings()
