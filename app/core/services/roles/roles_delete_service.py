from typing import Optional
from app.api.schemas.roles_schema import RolesDeletedSchema, RolesOutputSchema
from app.core.repositories.roles.roles_delete_repository import RolesDeleteRepository
from app.core.services.shared.delete_service import DeleteService


class RolesDeleteService(DeleteService):
    """
    Service for managing roles-related delete business logic.
    """

    def __init__(self, repository: RolesDeleteRepository):
        """
        Initialize the roles delete service.
        :param repository: The roles delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[RolesOutputSchema]:
        """
        Delete a roles by ID.
        :param id: The ID of the roles to delete.
        :return: The deleted roles as a schema, or None if not found.
        """
        deleted_roles = await self.soft_delete(id)
        return RolesDeletedSchema.validate(deleted_roles)
