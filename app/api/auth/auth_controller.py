from quart import request
from quart_auth import logout_user
from quart_schema import validate_request, validate_response

from app.api.auth.auth_services import AuthService
from app.api.auth.auth_schemas import (
    UseAuthInputSchema, UserAuthOutputLoginSchema)


class AuthController:
    """
    Controller that handles auth HTTP requests.
    """

    @staticmethod
    @validate_request(UseAuthInputSchema)
    @validate_response(UserAuthOutputLoginSchema)
    async def login(data: UseAuthInputSchema):
        user_auth = await AuthService.auth_login_user(data)
        return user_auth, 200

    @staticmethod
    async def logout():
        logout_user()
        return {}, 200
