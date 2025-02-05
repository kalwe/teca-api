import os
from quart import Quart
from quart.blueprints import Blueprint

from app.config import Config

# from app.api.auth import auth_bp

# TODO: use app config class
API_PREFIX = f"/api/{Config.ENGINE_SUFFIX}"

# gen_bp = {
#     'user_bp': {
#         'name': 'user_',
#         'end_point': '/user'
#     },
#     'employee_bp': {
#         'name': 'employee',
#         'end_point': '/employee'
#     },
# }
# TODO:
# def gen_bp(bp: Dict[str, Any]) -> None:
#     for k in bp.items():
#         for v in bp.
#             locals()[k] = Blueprint(name, __name__, url_prefix=endpoint)


api_bp = Blueprint('api', __name__, url_prefix=API_PREFIX)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
user_bp = Blueprint('user', __name__, url_prefix='/user')
employee_bp = Blueprint('employee', __name__, url_prefix='/employee')


def init_bp(app: Quart) -> None:
    api_bp.register_blueprint(auth_bp)
    api_bp.register_blueprint(user_bp)
    api_bp.register_blueprint(employee_bp)
    app.register_blueprint(api_bp)

    from app.api.auth import auth_routes
    # from app.api.routes import user_route
    # from app.api.routes import employee_route
