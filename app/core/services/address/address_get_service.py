from typing import List, Optional
from app.api.schemas.address_schema import AddressOutputSchema
from app.core.repositories.address.address_get_repository import AddressGetRepository
from app.core.services.shared.get_service import GetService


class AddressGetService(GetService):
    """
    Service for managing address-related business logic, leveraging generic
    methods from GetService.

    This service adds address-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = AddressGetRepository

    def __init__(self, repository: AddressGetRepository):
        """
        Initialize the service with a Address-specific repository.

        Args:
            repository (AddressGetRepository): Repository for address
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[AddressOutputSchema]:
        address = await self.get_by_id(id)
        return AddressOutputSchema.validate(address)

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[AddressOutputSchema]]:
        addresss = await self.get_all_records(filters)
        return [AddressOutputSchema.validate(address) for address in addresss]

    async def get_by_name(self, name: str) -> Optional[AddressOutputSchema]:
        address = await self._get_repository.get_address_by_name(name)
        return AddressOutputSchema.validate(address)
