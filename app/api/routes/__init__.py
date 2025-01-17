import os
from quart.blueprints import Blueprint

from .user_route import user_bp

API_PREFIX = os.getenv("API_PREFIX")

api = Blueprint('api', __name__)


def init_blueprints(app):
    with app.app_context():
        app.register_blueprint(user_bp)


# def bp_url_prefix(bp: Blueprint, prefix: str):
#     bp.url_prefix


def register_blueprints(api):
    """Initialize application with all modules"""
    for module in MODULES:
        api.register_blueprint(module.blp, url_prefix="/v2/")
