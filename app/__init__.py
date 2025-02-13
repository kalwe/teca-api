from quart import Quart
from quart_schema import QuartSchema

# from app.database.db_manager import close_db, init_db
from tortoise.contrib.quart import register_tortoise

from app.api.auth import init_auth
from app.api.routes import init_bp

from .config import config_by_name


def create_app(mode="dev") -> Quart:
    """In production create as app = create_app('Production')"""
    app = Quart(__name__)
    app.config.from_object(config_by_name[mode])
    # QuartSchemaConfig.configure_schema(app)
    QuartSchema(app)
    # init_db(app)
    # close_db(app)
    register_tortoise(
        app,
        db_url="postgres://docker:docker@db:5432/teca_coif",
        modules={"models": ["app.core.models", "aerich.models"]},
        generate_schemas=False,
    )

    init_bp(app)
    init_auth(app)

    return app
