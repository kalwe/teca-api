from typing import Optional

from app.api.schemas.clothing_schema import ClothingInputSchema, ClothingOutputSchema
from app.core.repositories.clothing.clothing_update_repository import (
    ClothingUpdateRepository,
)
from app.core.services.shared.update_service import UpdateService


class ClothingUpdateService(UpdateService):
    """
    Service for managing clothing-related business logic.
    """

    def __init__(self, repository: ClothingUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, clothing_data: ClothingInputSchema
    ) -> Optional[ClothingOutputSchema]:
        updated_clothing = await self.update_data(id, clothing_data)
        return ClothingOutputSchema().validate(updated_clothing)


# FIXME: validation errors
