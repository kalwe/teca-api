import os
from quart import Blueprint, Quart
from quart_auth import QuartAuth

API_PREFIX_V1 = os.getenv("ENGINE_SUFFIX_V1")

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

auth_manager = QuartAuth


def init_auth(app: Quart):
    auth_manager.init_app(app)
