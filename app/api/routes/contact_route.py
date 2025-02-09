from app.api.controllers.contact_controller import ContactController
from app.api.routes import contact_bp
from app.api.routes.base_route import BaseRoute
from quart.blueprints import Blueprint

class ContactRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, ContactController, 'contact', 'contacts')

ContactRoute(contact_bp)
