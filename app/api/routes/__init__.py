from app.api.routes.settings import api_settings
from .user_route import user_blueprint
from quart.blueprints import Blueprint

API_PREFIX = 'api'

api = Blueprint('api', __name__)


def init_blueprints(app):
    with app.app_context():
        app.register_blueprint(user_blueprint)
        app.register_blueprint(api_settings)
