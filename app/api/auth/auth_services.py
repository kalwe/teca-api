from secrets import compare_digest

from quart_auth import current_user

from app.api.auth import auth_manager
from app.api.auth.auth_schemas import UseAuthInputSchema, UserAuthOutputLoginSchema
from app.common.hash_utils import hash_provider
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.user.user_get_service import UserGetService


class AuthService:

    @staticmethod
    async def auth_login_user(
        user_data: UseAuthInputSchema
    ) -> UserAuthOutputLoginSchema:
        try:
            user_service = UserGetService(UserGetRepository())
            user = await user_service.get_by_name(name=user_data.name)
            user = user.index()
            password_hash = hash_provider(user_data["password_hash"])
            if user["name"] == user_data["name"] and compare_digest(
                    user["password_hash"], password_hash
            ):
                token_dump = auth_manager.dump_token(user["name"])
                user_auth = {
                    "current_user_id": current_user.auth_id,
                    "name": user["name"],
                    "id_authenticated": current_user.is_authenticated,
                    "token": token_dump,
                }
                return UserAuthOutputLoginSchema.model_validate(user_auth)
        except Exception as e:
            raise ValueError("Invalid credentials: {e}") from e
