from app.api.routes import auth_bp
from app.api.auth.auth_controller import AuthController


# def add_rules():
auth_bp.add_url_rule(
    '/login', view_func=AuthController.login,
    methods=["POST"]
)

auth_bp.add_url_rule(
    '/logout', view_func=AuthController.logout,
    methods=["POST"]
)
