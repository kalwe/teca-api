from typing import Optional

from app.api.schemas.clothing_schema import ClothingInputSchema, ClothingOutputSchema
from app.core.repositories.clothing.clothing_create_repository import (
    ClothingCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class ClothingCreateService(CreateService):
    """
    Service for managing clothing-related business logic.
    Handles creation of new clothings with role assignment and password hashing.
    """

    def __init__(self, repository: ClothingCreateRepository):
        """
        Initialize the service with a repository for clothing operations.

        Args:
            repository (ClothingCreateRepository): An instance of
                ClothingCreateRepository
                to handle data persistence for the Clothing model.
        """
        super().__init__(repository)

    async def create(
        self,
        clothing_data: ClothingInputSchema,
    ) -> Optional[ClothingOutputSchema]:
        """
        Create a new clothing with additional business logic.

        Args:
            clothing_data (ClothingInputSchema): The data for the new clothing.

        Returns:
            ClothingOutputSchema: Serialized data of the created clothing.

        Raises:
            ValueError: If the employee with the given ID does not exist.
        """
        employee = await self._validate_employee(clothing_data.employee)
        clothing_data.employee = employee

        created_clothing = await self.create_record(clothing_data)
        return ClothingOutputSchema().validate(created_clothing)


# FIXME: pydantic_core._pydantic_core.ValidationError: validation errors for EmployeeOutputSchema
