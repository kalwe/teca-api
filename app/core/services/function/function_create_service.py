from typing import Optional

from app.api.schemas.function_schema import FunctionInputSchema, FunctionOutputSchema
from app.core.repositories.function.function_create_repository import (
    FunctionCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class FunctionCreateService(CreateService):
    """
    Service for managing function-related business logic.
    Handles creation of new functions with role assignment and password hashing.
    """

    def __init__(self, repository: FunctionCreateRepository):
        """
        Initialize the service with a repository for function operations.

        Args:
            repository (FunctionCreateRepository): An instance of
                FunctionCreateRepository
                to handle data persistence for the Function model.
        """
        super().__init__(repository)
        # self._get_service = FunctionGetService(FunctionGetRepository(Function()))

    async def create(
        self,
        function_data: FunctionInputSchema,
    ) -> Optional[FunctionOutputSchema]:
        (
            """
        Create a new function with additional business logic.

        Args:
            name (str): The name of the function.
            email (str): The email of the function.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the function.

        Returns:
            FunctionOutputSchema: Serialized data of the created function.

        Raises:
            FunctionAlreadyExistsException: If a function with the given email
            already exists.
        """
            """
        Create a new function with additional business logic.

        Args:
            name (str): The name of the function.
            email (str): The email of the function.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the function.

        Returns:
            FunctionOutputSchema: Serialized data of the created function.

        Raises:
            FunctionAlreadyExistsException: If a function with the given email
            already exists.
        """
        )
        created_function = await self.create_record(function_data)
        return FunctionOutputSchema().validate(created_function)


# FIXME: If I pass only the name, it creates but returns: pydantic_core._pydantic_core.ValidationError: 2 validation errors for FunctionOutputSchema
