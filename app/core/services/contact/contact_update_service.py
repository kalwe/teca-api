from typing import Optional

from app.api.schemas.contact_schema import ContactInputSchema, ContactOutputSchema
from app.core.repositories.contact.contact_update_repository import (
    ContactUpdateRepository,
)
from app.core.services.shared.update_service import UpdateService


class ContactUpdateService(UpdateService):
    """
    Service for managing contact-related business logic.
    """

    def __init__(self, repository: ContactUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, contact_data: ContactInputSchema
    ) -> Optional[ContactOutputSchema]:
        updated_contact = await self.update_data(id, contact_data)
        return ContactOutputSchema().validate(updated_contact)


# FIXME: validation errors
