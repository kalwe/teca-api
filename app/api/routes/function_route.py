from app.api.controllers.function_controller import FunctionController
from app.api.routes import function_bp
from app.api.routes.base_route import BaseRoute
from quart.blueprints import Blueprint

class FunctionRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, FunctionController, 'function', 'functions')

FunctionRoute(function_bp)
