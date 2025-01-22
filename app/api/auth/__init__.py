import os
from quart import Blueprint

API_PREFIX_V1 = os.getenv("ENGINE_SUFFIX_V1")

auth_bp = Blueprint('auth', __name__, url_prefix=API_PREFIX_V1)
