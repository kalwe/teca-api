import os
import secrets


class Config(object):
    TESTING = False
    QUART_AUTH_MODE = os.getenv("QUART_AUTH_MODE", "bearer")
    QUART_SCHEMA_CONVERSION_PREFERENCE = "pydantic"
    ENGINE_SUFFIX = os.getenv("ENGINE_SUFFIX")
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(128))
    DB_URI = os.getenv("DATABASE_URL")

    # should be a dictionary, will be passed to Pydantic’s model_dump()
    # QUART_SCHEMA_PYDANTIC_DUMP_OPTIONS = "dict[str, Any]"
    # PROVIDE_AUTOMATIC_OPTIONS = True


class DevelopmentConfig(Config):
    # QUART_AUTH_COOKIE_SECURE = False
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

secret_key = Config.SECRET_KEY
