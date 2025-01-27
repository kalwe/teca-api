from typing import Optional
from app.api.schemas.user_schema import UserDeletedSchema, UserOutputSchema
from app.core.models.user_model import User
from app.core.repositories.user.user_delete_repository import (
    UserDeleteRepository)
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.shared.delete_service import DeleteService
from app.core.services.user.user_get_service import UserGetService


class UserDeleteService(DeleteService[User]):
    """
    Service for managing user-related delete business logic.
    """

    def __init__(self, repository: UserDeleteRepository):
        """
        Initialize the user delete service.
        :param repository: The user delete repository instance.
        """
        super().__init__(repository)
        self.get_service = UserGetService(UserGetRepository(User()))

    async def delete(self, id: int) -> Optional[UserOutputSchema]:
        """
        Delete a user by ID.
        :param id: The ID of the user to delete.
        :return: The deleted user as a schema, or None if not found.
        """
        try:
            user = await self.get_service.get_by_id(id)
            if not user:
                return None

            # self.repository.
            deleted_user = await self.soft_delete(user)
            return UserDeletedSchema.validate(deleted_user)
        except Exception as e:
            raise Exception(f"Failed user service delete: {e}") from e
