from typing import Optional

from app.api.schemas.function_schema import FunctionDeletedSchema, FunctionOutputSchema
from app.core.repositories.function.function_delete_repository import (
    FunctionDeleteRepository,
)
from app.core.services.shared.delete_service import DeleteService


class FunctionDeleteService(DeleteService):
    """
    Service for managing function-related delete business logic.
    """

    def __init__(self, repository: FunctionDeleteRepository):
        """
        Initialize the function delete service.
        :param repository: The function delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[FunctionOutputSchema]:
        """
        Delete a function by ID.
        :param id: The ID of the function to delete.
        :return: The deleted function as a schema, or None if not found.
        """
        deleted_function = await self.soft_delete(id)
        # TypeError: BaseSchema.validate() missing 1 required positional argument: 'model', (Resolved) with ()
        return FunctionDeletedSchema().validate(deleted_function)


# FIXME: pydantic_core._pydantic_core.ValidationError: 1 validation error for FunctionDeletedSchema
