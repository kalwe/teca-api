from quart_auth import logout_user
from quart_schema import validate_request

from app.api.auth.auth_services import AuthService
from app.api.auth.auth_schemas import UserLoginSchema


class AuthController():
    """
    Controller that handles auth HTTP requests.
    """

    @staticmethod
    @validate_request(UserLoginSchema)
    async def login(data: UserLoginSchema):
        AuthService.auth_user(data)

    @staticmethod
    @validate_request(UserLoginSchema)
    async def register(data: UserLoginSchema):
        AuthService.auth_login_user(data)

    @staticmethod
    async def logout():
        logout_user()
