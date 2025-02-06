from typing import List, Optional
from app.api.schemas.clothing_schema import ClothingOutputSchema
from app.core.repositories.clothing.clothing_get_repository import (
    ClothingGetRepository)
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
        clothing = self.get_by_id(id)
        return ClothingOutputSchema.validate(clothing)

    async def get_all(self, filters: Optional[dict] = None
                      ) -> Optional[List[ClothingOutputSchema]]:
        clothings = self.get_all_records(filters)
        return [ClothingOutputSchema.validate(clothing) for clothing in clothings]

    async def get_by_name(self, name: str) -> Optional[ClothingOutputSchema]:
        clothing = self._get_repository.get_clothing_by_name(name)
        return ClothingOutputSchema.validate(clothing)
