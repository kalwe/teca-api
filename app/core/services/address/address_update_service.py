from typing import Optional
from app.api.schemas.address_schema import AddressInputSchema, AddressOutputSchema
from app.core.repositories.address.address_update_repository import (
    AddressUpdateRepository,
)
from app.core.services.shared.update_service import UpdateService


class AddressUpdateService(UpdateService):
    """
    Service for managing address-related business logic.
    """

    def __init__(self, repository: AddressUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, address_data: AddressInputSchema
    ) -> Optional[AddressOutputSchema]:
        updated_address = await self.update_data(id, address_data)
        return AddressOutputSchema.validate(updated_address)
