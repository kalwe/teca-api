from quart import Quart, request
from app.core.middlewares import authentication_middleware, register_middlewares
from app.core.middlewares.error_handling_middleware import error_handling_middleware
from app.core.middlewares.logging_middleware import logging_middleware
from app.database.db import init_db
# from app.routes.swagger_ui_routes import swagger_ui  # Import the new blueprint


def create_app():
    app = Quart(__name__)

    # Application config
    app.config.from_object('app.config.Config')

    register_middlewares(app)

    # Init database
    @app.before_serving
    async def before_serving():
        await init_db()

    # Register blueprints
    # app.register_blueprint(main_bp)
    # app.register_blueprint(swagger_ui)  # Register the new blueprint
    # app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
