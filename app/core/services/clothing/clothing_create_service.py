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
        # self._get_service = ClothingGetService(ClothingGetRepository(Clothing()))

    async def create(
        self,
        clothing_data: ClothingInputSchema,
    ) -> Optional[ClothingOutputSchema]:
        (
            """
        Create a new clothing with additional business logic.

        Args:
            name (str): The name of the clothing.
            email (str): The email of the clothing.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the clothing.

        Returns:
            ClothingOutputSchema: Serialized data of the created clothing.

        Raises:
            ClothingAlreadyExistsException: If a clothing with the given email
            already exists.
        """
            """
        Create a new clothing with additional business logic.

        Args:
            name (str): The name of the clothing.
            email (str): The email of the clothing.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the clothing.

        Returns:
            ClothingOutputSchema: Serialized data of the created clothing.

        Raises:
            ClothingAlreadyExistsException: If a clothing with the given email
            already exists.
        """
        )
        created_clothing = await self.create_record(clothing_data)
        return ClothingOutputSchema().validate(created_clothing)
