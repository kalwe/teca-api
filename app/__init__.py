from quart import Quart
from quart_auth import QuartAuth
from quart_schema import QuartSchema

# from app.core.middlewares import authentication_middleware, init_middlewares
# from app.core.middlewares.error_handling_middleware import error_handling_middleware
# from app.core.middlewares.logging_middleware import logging_middleware
# from app.routes.swagger_ui_routes import swagger_ui  # Import the new blueprint
from .config import config_by_name
from app.database.db_manager import DatabaseManager, init_db
from app.api.routes import init_blueprints

db = DatabaseManager()
auth_manager = QuartAuth()


def create_app(mode='dev') -> Quart:
    """In production create as app = create_app('Production')"""
    app = Quart(__name__)
    QuartSchema(app)

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
        await db.init_db()

    QuartAuth(app)

    init_blueprints(app)

    @app.after_serving
    async def close_orm():
        await db.close_db()

    return app
