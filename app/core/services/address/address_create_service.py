from typing import Optional

from app.api.schemas.address_schema import AddressInputSchema, AddressOutputSchema
from app.core.repositories.address.address_create_repository import (
    AddressCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class AddressCreateService(CreateService):
    """
    Service for managing address-related business logic.
    Handles creation of new addresss with role assignment and password hashing.
    """

    def __init__(self, repository: AddressCreateRepository):
        """
        Initialize the service with a repository for address operations.

        Args:
            repository (AddressCreateRepository): An instance of
                AddressCreateRepository
                to handle data persistence for the Address model.
        """
        super().__init__(repository)
        # self._get_service = AddressGetService(AddressGetRepository(Address()))

    async def create(
        self,
        address_data: AddressInputSchema,
    ) -> Optional[AddressOutputSchema]:
        (
            """
        Create a new address with additional business logic.

        Args:
            name (str): The name of the address.
            email (str): The email of the address.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the address.

        Returns:
            AddressOutputSchema: Serialized data of the created address.

        Raises:
            AddressAlreadyExistsException: If a address with the given email
            already exists.
        """
            """
        Create a new address with additional business logic.

        Args:
            name (str): The name of the address.
            email (str): The email of the address.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the address.

        Returns:
            AddressOutputSchema: Serialized data of the created address.

        Raises:
            AddressAlreadyExistsException: If a address with the given email
            already exists.
        """
        )
        created_address = await self.create_record(address_data)
        return AddressOutputSchema().validate(created_address)

    # FIXME: Testing in swagger(/docs) returned: "POST /address/ HTTP/1.1" 400 Bad Request
