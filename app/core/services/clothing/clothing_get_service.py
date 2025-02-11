from typing import List, Optional

from app.api.schemas.clothing_schema import ClothingOutputSchema
from app.core.repositories.clothing.clothing_get_repository import ClothingGetRepository
from app.core.services.shared.get_service import GetService


class ClothingGetService(GetService):
    """
    Service for managing clothing-related business logic, leveraging generic
    methods from GetService.

    This service adds clothing-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = ClothingGetRepository

    def __init__(self, repository: ClothingGetRepository):
        """
        Initialize the service with a Clothing-specific repository.

        Args:
            repository (ClothingGetRepository): Repository for clothing
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[ClothingOutputSchema]:
        clothing = await self.get_by_id(id)
        # TypeError: BaseSchema.validate() missing 1 required positional argument: 'model', (Resolved) with ()
        return ClothingOutputSchema().validate(clothing)

    # FIXME: pydantic_core._pydantic_core.ValidationError: 4 validation errors for ClothingOutputSchema

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[ClothingOutputSchema]]:
        clothings = await self.get_all_records(filters)
        return [ClothingOutputSchema.validate(clothing) for clothing in clothings]

    # With no records returns an empty list
