from quart_schema import QuartSchema
from quart import Quart

from app.api.auth import init_auth

# from app.routes.swagger_ui_routes import swagger_ui  # Import the new blueprint
from .config import config_by_name
from app.database.db_manager import close_db, init_db
from app.api.routes import init_bp


def create_app(mode='dev') -> Quart:
    """In production create as app = create_app('Production')"""
    app = Quart(__name__)
    """In production create as app = create_app('prod')"""
    app.config.from_object(config_by_name[mode])
    QuartSchema(app)

    init_db(app)
    close_db(app)

    init_auth(app)
    init_bp(app)

    return app
