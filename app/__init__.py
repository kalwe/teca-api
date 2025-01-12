from typing import Any

from dynaconf import settings
from quart import Quart
from quart_schema import QuartSchema

from app.api.routes import init_blueprints
# from app.core.middlewares import authentication_middleware, init_middlewares
# from app.core.middlewares.error_handling_middleware import error_handling_middleware
# from app.core.middlewares.logging_middleware import logging_middleware
from app.database.db import init_db
# from app.routes.swagger_ui_routes import swagger_ui  # Import the new blueprint


def init_config(app: Quart, **config_overrides: Any) -> Quart:
    app.config.from_object(settings)
    app.config.update(config_overrides)


def create_app(**config_overrides: Any) -> Quart:
    app = Quart(__name__)
    QuartSchema(app)

    # Application config
    # app.config.from_object('app.config.Config')
    init_config(app, **config_overrides)

    # Init database
    @app.before_serving
    async def before_serving():
        await init_db()

    init_blueprints(app)

    return app
