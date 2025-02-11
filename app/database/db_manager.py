from threading import Lock

from quart import Quart
from tortoise import Tortoise, connections

from app.database.config import TORTOISE_ORM


class DatabaseManager:
    """Singleton class for managing the database connection."""

    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
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

    @classmethod
    async def init_db(cls, generate_schemas: bool = False) -> None:
        """Initialize the database connection."""
        _generate_schemas = generate_schemas
        if not cls._initialized:
            try:
                await Tortoise.init(config=TORTOISE_ORM)
                # use only in develop
                if _generate_schemas:
                    await Tortoise.generate_schemas()
                cls._initialized = True
            except Exception as e:
                raise RuntimeError("Failed to init database: {e}") from e

    async def close_db(self) -> None:
        """Close the database connection."""
        if self._initialized:
            try:
                await connections.close_all()
                self._initialized = False
            except Exception as e:
                raise RuntimeError("Failed to close database: {e}") from e


def init_db(app: Quart) -> None:
    @app.before_serving
    async def init_orm():
        app.config["DEBUG"] # TODO: remove this line after testing
        db = DatabaseManager()
        await DatabaseManager().init_db()


def close_db(app: Quart) -> None:
    @app.after_serving
    async def close_orm():
        db = DatabaseManager()
        await DatabaseManager().close_db()
