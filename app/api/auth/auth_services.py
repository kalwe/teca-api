from quart_auth import AuthUser, Unauthorized, current_user, login_user
from app.api.auth.auth_schemas import UserLoginSchema
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.user.user_get_service import UserGetService
from secrets import compare_digest

# Setup the password context for hashing passwords


class AuthService:

    # @staticmethod
    # async def register_user(email: str, password: str):
    #     # hashed_password = pwd_context.hash(password)
    #     user = await UserModel.create(email=email, hashed_password=hashed_password)
    #     return user

    @staticmethod
    async def auth_login_user(user_data: UserLoginSchema):
        try:
            user_service = UserGetService(UserGetRepository())
            user = await user_service.get_by_email(email=user_data.email)
            user = user.dump()
            if user["email"] == user_data.email and compare_digest(
                    user["password_hash"],  user_data.password_hash):
                login_user(AuthUser(user["email"]))
                user_auth_id = current_user
                # access_token = dump_token()

                # return redirect(url_for("dashboard"))
                # return {
                #     "access_token": access_token,
                #     "refresh_token": refresh_token
                # }
        except Exception as e:
            raise ValueError("Invalid credentials")

    @staticmethod
    async def auth_register_user()

    # @app.errorhandler(Unauthorized)
    # async def redirect_to_login(*_: Exception) -> ResponseReturnValue:
    #     return redirect(url_for("login"))
