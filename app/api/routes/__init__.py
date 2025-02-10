from quart import Quart
from quart import Blueprint

from app.config import Config

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


api_bp = Blueprint("api", __name__, url_prefix=API_PREFIX)
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
user_bp = Blueprint("user", __name__, url_prefix="/user")
employee_bp = Blueprint("employee", __name__, url_prefix="/employee")
address_bp = Blueprint("address", __name__, url_prefix="/address")
bank_account_bp = Blueprint("bank_account", __name__, url_prefix="/bank_account")
clothing_bp = Blueprint("clothing", __name__, url_prefix="/clothing")
contact_bp = Blueprint("contact", __name__, url_prefix="/contact")
vacancy_bp = Blueprint("vacancy", __name__, url_prefix="/vacancy")
function_bp = Blueprint("function", __name__, url_prefix="/function")
reminder_bp = Blueprint("reminder", __name__, url_prefix="/reminder")
roles_bp = Blueprint("roles", __name__, url_prefix="/roles")

def init_bp(app: Quart) -> None:
    from app.api.routes import (
        user_route,
        vacancy_route,
        address_route,
        bank_account_route,
        clothing_route,
        contact_route,
        employee_route,
        function_route,
        reminder_route,
        roles_route)  # noqa: F401
    # from app.api.auth import auth_routes  # noqa: F401

    app.register_blueprint(user_bp)
    app.register_blueprint(vacancy_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(bank_account_bp)
    app.register_blueprint(clothing_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(function_bp)
    app.register_blueprint(reminder_bp)
    app.register_blueprint(roles_bp)
    # app.register_blueprint(auth_bp) # TODO: implement auth
    app.register_blueprint(api_bp)
