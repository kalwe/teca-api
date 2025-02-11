from typing import Optional

from app.api.schemas.user_schema import UserDeletedSchema, UserOutputSchema
from app.core.repositories.user.user_delete_repository import UserDeleteRepository
from app.core.services.shared.delete_service import DeleteService


class UserDeleteService(DeleteService):
    """
    Service for managing user-related delete business logic.
    """

    def __init__(self, repository: UserDeleteRepository):
        """
        Initialize the user delete service.
        :param repository: The user delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[UserOutputSchema]:
        """
        Delete a user by ID.
        :param id: The ID of the user to delete.
        :return: The deleted user as a schema, or None if not found.
        """
        deleted_user = await self.soft_delete(id)
        return UserDeletedSchema().validate(deleted_user)
