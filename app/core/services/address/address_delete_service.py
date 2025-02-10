from typing import Optional
from app.api.schemas.address_schema import AddressDeletedSchema, AddressOutputSchema
from app.core.repositories.address.address_delete_repository import (
    AddressDeleteRepository,
)
from app.core.services.shared.delete_service import DeleteService


class AddressDeleteService(DeleteService):
    """
    Service for managing address-related delete business logic.
    """

    def __init__(self, repository: AddressDeleteRepository):
        """
        Initialize the address delete service.
        :param repository: The address delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[AddressOutputSchema]:
        """
        Delete a address by ID.
        :param id: The ID of the address to delete.
        :return: The deleted address as a schema, or None if not found.
        """
        deleted_address = await self.soft_delete(id)
        return AddressDeletedSchema.validate(deleted_address)
