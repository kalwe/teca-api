from typing import Optional
from app.api.schemas.user_schema import UserInputSchema, UserOutputSchema
from app.core.models.user_model import UserModel
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.shared.update_service import UpdateService
from app.core.services.user.user_get_service import UserGetService


class UserUpdateService(UpdateService[UserModel]):
    """
    Service for managing user-related business logic.
    """

    def __init__(self, repository: UserUpdateRepository):
        super().__init__(repository)
        self.get_service = UserGetService(UserGetRepository())

    async def update(self, id, data: UserInputSchema
                     ) -> Optional[UserOutputSchema]:
        try:
            user = self.get_service.get_by_id(id)
            if not user:
                return None

            updated_user = self.update_data(user, data)
            return UserOutputSchema.validate(updated_user)
        except Exception as e:
            raise Exception(
                f"Failed UserUpdateService().update(): {e}") from e
