from app.api.controllers.roles_controller import RolesController
from app.api.routes import roles_bp
from app.api.routes.base_route import BaseRoute
from quart import Blueprint

class RolesRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, RolesController, 'roles', 'roles')

RolesRoute(roles_bp)
