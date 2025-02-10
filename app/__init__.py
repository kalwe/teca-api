from quart import Quart
from quart_schema import QuartSchema, Info

from app.api.auth import init_auth
from app.api.routes import init_bp
from app.database.db_manager import close_db, init_db

from .config import config_by_name


def create_app(mode="dev") -> Quart:
    """In production create as app = create_app('Production')"""
    app = Quart(__name__)
    app.config.from_object(config_by_name[mode])
    QuartSchema(app, info=Info(title="Teca API", version="0.1.0"))
    init_db(app)
    close_db(app)

    init_bp(app)
    init_auth(app)

    return app
