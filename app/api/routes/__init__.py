import os
from quart import Quart
from quart.blueprints import Blueprint

from app.api.auth import auth_bp

API_PREFIX_V1 = os.getenv("ENGINE_SUFFIX_V1")

api = Blueprint('api', __name__, url_prefix=API_PREFIX_V1)
user_bp = Blueprint('user', __name__, url_prefix='/user')
employee_bp = Blueprint('employee', __name__, url_prefix='/employee')


def init_bp(app: Quart):
    api.register_blueprint(auth_bp)
    api.register_blueprint(user_bp)
    api.register_blueprint(employee_bp)
    app.register_blueprint(api)

    from app.api.auth import auth_routes
    from app.api.routes import user_route
    from app.api.routes import employee_route
