from quart import Quart
from app.config import TORTOISE_ORM, Config
from tortoise import Tortoise
from threading import Lock


class DatabaseManager():
    """Singleton class for managing the database connection."""
    _instance = None
    _lock = Lock()

    def __new__(cls, app: Quart, *args, **kwargs):
        """Ensure only one instance is created (thread-safe)."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """Initialize the database connection."""
        if hasattr(self, "_initialized") and self._initialized:
            return  # Prevent re-initialization
        self._initialized = False

    async def init_db(self):
        """Initialize the database connection."""
        if not self._initialized:
            try:
                await Tortoise.init(
                    db_url=Config.DB_URI,
                    modules={
                        "models": TORTOISE_ORM["apps"]["models"]["models"]
                    }
                )
                await Tortoise.generate_schemas()
                self._initialized = True
            except Exception as e:
                raise RuntimeError("Failed to init database") from e

    async def close_db(self):
        """Close the database connection."""
        if self._initialized:
            try:
                await Tortoise.close_connections()
                self._initialized = False
            except Exception as e:
                raise RuntimeError("Failed to close database") from e


async def init_db():
    await DatabaseManager().init_db()


async def close_db():
    await DatabaseManager().close_db()
