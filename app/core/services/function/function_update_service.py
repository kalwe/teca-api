from typing import Optional

from app.api.schemas.function_schema import FunctionInputSchema, FunctionOutputSchema
from app.core.repositories.function.function_update_repository import (
    FunctionUpdateRepository,
)
from app.core.services.shared.update_service import UpdateService


class FunctionUpdateService(UpdateService):
    """
    Service for managing function-related business logic.
    """

    def __init__(self, repository: FunctionUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, function_data: FunctionInputSchema
    ) -> Optional[FunctionOutputSchema]:
        updated_function = await self.update_data(id, function_data)
        return FunctionOutputSchema().validate(updated_function)


# FIXME: pydantic_core._pydantic_core.ValidationError: 2 validation errors for FunctionOutputSchema
