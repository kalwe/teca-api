from typing import List, Optional

from app.api.schemas.contact_schema import ContactOutputSchema
from app.core.repositories.contact.contact_get_repository import ContactGetRepository
from app.core.services.shared.get_service import GetService


class ContactGetService(GetService):
    """
    Service for managing contact-related business logic, leveraging generic
    methods from GetService.

    This service adds contact-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = ContactGetRepository

    def __init__(self, repository: ContactGetRepository):
        """
        Initialize the service with a Contact-specific repository.

        Args:
            repository (ContactGetRepository): Repository for contact
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[ContactOutputSchema]:
        contact = await self.get_by_id(id)
        # TypeError: BaseSchema.validate() missing 1 required positional argument: 'model', (Resolved) with ()
        return ContactOutputSchema().validate(contact)

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[ContactOutputSchema]]:
        contacts = await self.get_all_records(filters)
        return [ContactOutputSchema().validate(contact) for contact in contacts]

    # With no records returns an empty list


# FIXME: pydantic_core._pydantic_core.ValidationError: 4 validation errors for ContactOutputSchema
