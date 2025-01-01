from tortoise import Tortoise
from app.config import Config

async def init_db():
    await Tortoise.init(
        db_url=Config.DB_URI,
        modules={'models': ['app.models', "aerich.models"]}
    )
    await Tortoise.generate_schemas()
