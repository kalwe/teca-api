from app.config import Config

TORTOISE_ORM = {
    "connections": {
        "default": Config.DB_URI,
    },
    "apps": {
        "models": {
            "models": ["app.core.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
