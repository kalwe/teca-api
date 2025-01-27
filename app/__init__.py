from quart import Quart
from quart_auth import QuartAuth
from quart_schema import QuartSchema

from app.api.auth import init_auth

# from app.routes.swagger_ui_routes import swagger_ui  # Import the new blueprint
from .config import config_by_name
from app.database.db_manager import DatabaseManager
from app.api.routes import init_bp


def create_app(mode='dev') -> Quart:
    """In production create as app = create_app('Production')"""
    app = Quart(__name__)
    app.config["QUART_AUTH_MODE"] = "bearer"
    init_auth(app)

    # Application config
    # app.config.from_object('app.config.{mode}')

    # TEST
    app.config.from_object(config_by_name[mode])
    # app.config.from_prefixed_env()
    # assert app.config["TESTING"] is True
    # app.config.from_object(f"config.{mode}")

    # Init database

    @app.before_serving
    async def init_orm():
        db = DatabaseManager(app)
        await db.init_db()

    init_bp(app)

    @app.after_serving
    async def close_orm():
        db = DatabaseManager(app)
        await db.close_db()

    return app
