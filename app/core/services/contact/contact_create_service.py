from typing import Optional

from app.api.schemas.contact_schema import ContactInputSchema, ContactOutputSchema
from app.core.repositories.contact.contact_create_repository import (
    ContactCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class ContactCreateService(CreateService):
    """
    Service for managing contact-related business logic.
    Handles creation of new contacts with role assignment and password hashing.
    """

    def __init__(self, repository: ContactCreateRepository):
        """
        Initialize the service with a repository for contact operations.

        Args:
            repository (ContactCreateRepository): An instance of
                ContactCreateRepository
                to handle data persistence for the Contact model.
        """
        super().__init__(repository)

    async def create(
        self,
        contact_data: ContactInputSchema,
    ) -> Optional[ContactOutputSchema]:
        """
        Create a new contact with additional business logic.

        Args:
            contact_data (ContactInputSchema): The data for the new contact.

        Returns:
            ContactOutputSchema: Serialized data of the created contact.

        Raises:
            ValueError: If the employee with the given ID does not exist.
        """
        employee = await self._validate_employee(contact_data.employee)
        contact_data.employee = employee

        created_contact = await self.create_record(contact_data)
        return ContactOutputSchema().validate(created_contact)


# FIXME: pydantic_core._pydantic_core.ValidationError: validation errors for EmployeeOutputSchema
