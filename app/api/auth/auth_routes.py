from app.api.auth import auth_bp
from app.api.auth.auth_controller import AuthController

auth_bp.add_url_rule(
    '/login', view_func=AuthController.login)
