from quart.blueprints import Blueprint

from .user_route import user_blueprint

API_PREFIX = 'api'

api = Blueprint('api', __name__)


def init_blueprints(app):
    with app.app_context():
        app.register_blueprint(user_blueprint)
