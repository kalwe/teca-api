from typing import Optional
from app.api.schemas.user_schema import UserOutputSchema
from app.core.models.user_model import User
from app.core.repositories.user.user_delete_repository import UserDeleteRepository
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.shared.delete_service import DeleteService
from app.core.services.user.get_user_service import UserGetService


class UserDeleteService(DeleteService[User]):
    """
    Service for managing user-related business logic.
    """

    def __init__(self, repository: UserDeleteRepository):
        super().__init__(repository)
        self.repository = repository

    async def delete(self, id: int) -> Optional[UserOutputSchema]:
        get_user_repository = UserGetRepository()
        get_user_service = UserGetService(get_user_repository)
        user = get_user_service.get_by_id(id)
        if user:
            deleted_user = self.soft_delete(user)
            return UserOutputSchema.model_validate(deleted_user)
        return None
