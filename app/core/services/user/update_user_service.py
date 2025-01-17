from typing import Optional
from app.api.schemas.user_schema import UserOutputSchema
from app.core.models.user_model import User
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.shared.update_service import UpdateService
from app.core.services.user.get_user_service import UserGetService


class UserUpdateService(UpdateService[User]):
    """
    Service for managing user-related business logic.
    """

    def __init__(self, repository: UserUpdateRepository):
        super().__init__(repository)
        self.repository = repository

    async def update(self, id, data) -> Optional[UserOutputSchema]:
        get_user_repository = UserGetRepository()
        get_user_service = UserGetService(get_user_repository)
        user = get_user_service.get_by_id(id)
        if user:
            updated_user = self.update_record(user, data)
            return UserOutputSchema.model_validate(updated_user)
        return None
