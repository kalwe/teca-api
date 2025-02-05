from typing import List, Optional
from app.api.schemas.contact_schema import ContactOutputSchema
from app.core.repositories.contact.contact_get_repository import (
    ContactGetRepository)
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
        contact = self.get_by_id(id)
        return ContactOutputSchema.validate(contact)

    async def get_all(self, filters: Optional[dict] = None
                      ) -> Optional[List[ContactOutputSchema]]:
        contacts = self.get_all_records(filters)
        return [ContactOutputSchema.validate(contact) for contact in contacts]

    async def get_by_name(self, name: str) -> Optional[ContactOutputSchema]:
        contact = self._get_repository.get_contact_by_name(name)
        return ContactOutputSchema.validate(contact)
