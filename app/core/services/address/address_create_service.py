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

    async def create(
        self,
        address_data: AddressInputSchema,
    ) -> Optional[AddressOutputSchema]:
        """
        Create a new address with additional business logic.

        Args:
            address_data (AddressInputSchema): The data for the new address.

        Returns:
            AddressOutputSchema: Serialized data of the created address.

        Raises:
            ValueError: If the employee with the given ID does not exist.
        """
        employee = await self._validate_employee(address_data.employee)
        address_data.employee = employee

        created_address = await self.create_record(address_data)
        return AddressOutputSchema().validate(created_address)


# FIXME: pydantic_core._pydantic_core.ValidationError: 14 validation errors for EmployeeOutputSchema
