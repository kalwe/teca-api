from typing import List, Optional

from app.api.schemas.function_schema import FunctionOutputSchema
from app.core.repositories.function.function_get_repository import FunctionGetRepository
from app.core.services.shared.get_service import GetService


class FunctionGetService(GetService):
    """
    Service for managing function-related business logic, leveraging generic
    methods from GetService.

    This service adds function-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = FunctionGetRepository

    def __init__(self, repository: FunctionGetRepository):
        """
        Initialize the service with a Function-specific repository.

        Args:
            repository (FunctionGetRepository): Repository for function
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[FunctionOutputSchema]:
        function = await self.get_by_id(id)
        return FunctionOutputSchema().validate(function)

    # FIXME: In both cases return: pydantic_core._pydantic_core.ValidationError: 2 validation errors for FunctionOutputSchema

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[FunctionOutputSchema]]:
        functions = await self.get_all_records(filters)
        return [FunctionOutputSchema().validate(function) for function in functions]

    # With no records return an empty list
    # FIXME: With records return an error: pydantic_core._pydantic_core.ValidationError: 2 validation errors for FunctionOutputSchema

    async def get_by_name(self, name: str) -> Optional[FunctionOutputSchema]:
        function = await self._get_repository.get_function_by_name(name)
        return FunctionOutputSchema().validate(function)
