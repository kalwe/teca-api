import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_URI = os.getenv('DATABASE_URL')
    PROVIDE_AUTOMATIC_OPTIONS = True
    DEBUG = True

TORTOISE_ORM = {
    "connections": {
        "default": Config.DB_URI,
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
