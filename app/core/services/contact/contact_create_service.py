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
        # self._get_service = ContactGetService(ContactGetRepository(Contact()))

    async def create(
        self,
        contact_data: ContactInputSchema,
    ) -> Optional[ContactOutputSchema]:
        (
            """
        Create a new contact with additional business logic.

        Args:
            name (str): The name of the contact.
            email (str): The email of the contact.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the contact.

        Returns:
            ContactOutputSchema: Serialized data of the created contact.

        Raises:
            ContactAlreadyExistsException: If a contact with the given email
            already exists.
        """
            """
        Create a new contact with additional business logic.

        Args:
            name (str): The name of the contact.
            email (str): The email of the contact.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the contact.

        Returns:
            ContactOutputSchema: Serialized data of the created contact.

        Raises:
            ContactAlreadyExistsException: If a contact with the given email
            already exists.
        """
        )
        created_contact = await self.create_record(contact_data)
        return ContactOutputSchema().validate(created_contact)
