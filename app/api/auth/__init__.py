from quart import Quart
from quart_auth import QuartAuth

from app.api.auth.auth_models import UserAuth

auth_manager = QuartAuth()


def init_auth(app: Quart) -> None:
    auth_manager.user_class = UserAuth
    auth_manager.init_app(app)
