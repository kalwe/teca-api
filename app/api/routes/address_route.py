from app.api.controllers.address_controller import AddressController
from app.api.routes import address_bp
from app.api.routes.base_route import BaseRoute
from quart.blueprints import Blueprint

class AddressRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, AddressController, 'address', 'addresses')

AddressRoute(address_bp)
