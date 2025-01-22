
from pydantic.v1.env_settings import BaseSettings
from pydantic import Field, SecretStr, AnyUrl
# from enum import Enum
# import os


# class Envs(Enum):
#     SECRET_KEY = os.getenv("SECRET_KEY")

#     DB_USER = os.getenv("DB_USER") | "docker"  # Default .env.dev
#     DB_PASSWORD = os.getenv("DB_PASSWORD") | "docker"  # Default .env.dev
#     DB_NAME = os.getenv("DB_NAME") | "teca_coif"
#     DATABASE_URL = os.getenv("DATABASE_URL") | (
#         f"postgres//docker:docker@db:5432/{DB_NAME}")


class Settings(BaseSettings):
    API_PORT: str = Field(..., env="API_PORT", default="5000")
    API_HOST: str = Field(..., env="API_HOST", default="0.0.0.0")
    ENGINE_SUFFIX: str = Field(..., env="ENGINE_SUFFIX")
    JWT_SECRET: SecretStr = Field(..., env="JWT_SECRET")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: SecretStr = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    DATABASE_URL: AnyUrl = Field(..., env="DATABASE_URL")
    AWS_S3_REGION: str = Field(..., env="AWS_S3_REGION")
    AWS_S3_ACCESS_KEY_ID: str = Field(..., env="AWS_S3_ACCESS_KEY_ID")
    AWS_S3_SECRET_ACCESS_KEY: SecretStr = Field(
        ..., env="AWS_S3_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME: str = Field(..., env="AWS_S3_BUCKET_NAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    # def __init__(self, env_file_path: Optional[str] = None, **kwargs):
    #     # Set the environment file dynamically if provided
    #     if env_file_path:
    #         self.__config__.env_file = env_file_path
    #     super().__init__(**kwargs)


# def load_envs():
#     settings = Settings()
#     return settings
