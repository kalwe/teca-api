from .authentication import authentication_middleware
from .logging import logging_middleware
from .error_handling import error_handling_middleware

def register_middlewares(app):
    """
    Registers all middlewares to the app.
    This will be called in the `main.py` to apply them to the app.
    """
    @app.before_request
    async def before_request():
        # Middlewares globais para todas as requisições
        await logging_middleware(app)
        await authentication_middleware(app)

    @app.after_request
    async def after_request(response):
        # Middlewares que modificam a resposta
        return response

    @app.errorhandler(Exception)
    async def handle_exception(e):
        # Middleware de tratamento de erro global
        return await error_handling_middleware(app)
