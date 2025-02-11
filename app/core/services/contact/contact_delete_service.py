from typing import Optional

from app.api.schemas.contact_schema import ContactDeletedSchema, ContactOutputSchema
from app.core.repositories.contact.contact_delete_repository import (
    ContactDeleteRepository,
)
from app.core.services.shared.delete_service import DeleteService


class ContactDeleteService(DeleteService):
    """
    Service for managing contact-related delete business logic.
    """

    def __init__(self, repository: ContactDeleteRepository):
        """
        Initialize the contact delete service.
        :param repository: The contact delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[ContactOutputSchema]:
        """
        Delete a contact by ID.
        :param id: The ID of the contact to delete.
        :return: The deleted contact as a schema, or None if not found.
        """
        deleted_contact = await self.soft_delete(id)
        # TypeError: BaseSchema.validate() missing 1 required positional argument: 'model', (Resolved) with ()
        return ContactDeletedSchema().validate(deleted_contact)


# FIXME: pydantic_core._pydantic_core.ValidationError: 1 validation error for ContactDeletedSchema
