import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', "change_on_prod")
    DB_URI = os.getenv('DATABASE_URL')
    # PROVIDE_AUTOMATIC_OPTIONS = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

# TORTOISE_ORM = {
#     "connections": {
#         "default": Config.DB_URI,
#     },
#     "apps": {
#         "models": {
#             "models": ["app.core.models", "aerich.models"],
#             "default_connection": "default",
#         },
#     },
# }
