from typing import Optional

from app.api.schemas.clothing_schema import ClothingDeletedSchema, ClothingOutputSchema
from app.core.repositories.clothing.clothing_delete_repository import (
    ClothingDeleteRepository,
)
from app.core.services.shared.delete_service import DeleteService


class ClothingDeleteService(DeleteService):
    """
    Service for managing clothing-related delete business logic.
    """

    def __init__(self, repository: ClothingDeleteRepository):
        """
        Initialize the clothing delete service.
        :param repository: The clothing delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[ClothingOutputSchema]:
        """
        Delete a clothing by ID.
        :param id: The ID of the clothing to delete.
        :return: The deleted clothing as a schema, or None if not found.
        """
        deleted_clothing = await self.soft_delete(id)
        # TypeError: BaseSchema.validate() missing 1 required positional argument: 'model', (Resolved) with ()
        return ClothingDeletedSchema().validate(deleted_clothing)


# FIXME: pydantic_core._pydantic_core.ValidationError: 1 validation error for ClothingDeletedSchema
