from typing import Optional
from app.api.schemas.user_schema import UserOutputSchema
from app.core.models.user_model import User
from app.core.repositories.user.user_update_repository import (
    UserUpdateRepository)
from app.core.services.shared.update_service import UpdateService


class UserUpdateService(UpdateService[User]):
    """
    Service for managing user-related business logic.
    """

    def __init__(self, repository: UserUpdateRepository):
        super().__init__(repository)

    async def update(self, id, data: User) -> Optional[UserOutputSchema]:
        try:
            updated_user = self.update_data(id, data)
            return UserOutputSchema.validate(updated_user)
        except Exception as e:
            raise Exception(
                f"Failed UserUpdateService().update(): {e}") from e
