import os
from quart import Quart
from quart.blueprints import Blueprint

from app.api.auth import auth_bp

API_PREFIX_V1 = os.getenv("ENGINE_SUFFIX_V1")

api = Blueprint('api', __name__, url_prefix=API_PREFIX_V1)
user_bp = Blueprint('user', __name__, url_prefix=API_PREFIX_V1)


def init_blueprints(app: Quart):
    with app.app_context():
        app.register_blueprint(auth_bp)
        app.register_blueprint(user_bp)
        from app.api.auth import auth_routes
        from app.api.routes import user_route


# parent = Blueprint("parent", __name__, url_prefix="/parent")
# child = Blueprint("child", __name__, url_prefix="/child")
# parent.register_blueprint(child)
# app.register_blueprint(parent)
