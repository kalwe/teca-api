from app.api.controllers.clothing_controller import ClothingController
from app.api.routes import clothing_bp
from app.api.routes.base_route import BaseRoute
from quart import Blueprint

class ClothingRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, ClothingController, 'clothing', 'clothings')

ClothingRoute(clothing_bp)
