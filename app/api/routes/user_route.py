from app.api.controllers.user_controller import UserController
from app.api.routes import user_bp
from app.api.routes.base_route import BaseRoute
from quart.blueprints import Blueprint

class UserRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, UserController, 'user', 'users')

UserRoute(user_bp)
