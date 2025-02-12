from typing import Optional

from app.api.schemas.user_schema import UserInputSchema, UserOutputSchema
from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.shared.update_service import UpdateService


class UserUpdateService(UpdateService):
    """
    Service for managing user-related business logic.
    """

    def __init__(self, repository: UserUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, user_data: UserInputSchema
    ) -> Optional[UserOutputSchema]:
        updated_user = await self.update_data(id, user_data)
        return UserOutputSchema().validate(updated_user)
