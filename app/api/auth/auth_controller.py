from typing import Any, Dict
from quart_auth import logout_user
from quart_schema import validate_request, validate_response

from app.api.auth.auth_services import AuthService
from app.api.auth.auth_schemas import (
    UseAuthInputSchema, UserAuthOutputLoginSchema)
from app.api.auth import auth_bp
from app.core.models.user_model import User


class AuthController:
    """
    Controller that handles auth HTTP requests.
    """

    @staticmethod
    @validate_request(UseAuthInputSchema)
    @auth_bp.route('/', methods=["POST"])
    @validate_response(UserAuthOutputLoginSchema)
    async def login(data: Dict[str, Any]):
        user_auth = AuthService.auth_login_user(data)
        return user_auth, 200

    @auth_bp.route('/', methods=["POST"])
    @staticmethod
    async def logout():
        logout_user(), 200
