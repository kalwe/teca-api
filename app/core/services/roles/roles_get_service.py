from typing import List, Optional

from app.api.schemas.roles_schema import RolesOutputSchema
from app.core.repositories.roles.roles_get_repository import RolesGetRepository
from app.core.services.shared.get_service import GetService


class RolesGetService(GetService):
    """
    Service for managing roles-related business logic, leveraging generic
    methods from GetService.

    This service adds roles-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = RolesGetRepository

    def __init__(self, repository: RolesGetRepository):
        """
        Initialize the service with a Roles-specific repository.

        Args:
            repository (RolesGetRepository): Repository for roles
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[RolesOutputSchema]:
        roles = await self.get_by_id(id)
        return RolesOutputSchema().validate(roles)

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[RolesOutputSchema]]:
        roless = await self.get_all_records(filters)
        return [RolesOutputSchema().validate(roles) for roles in roless]

    # FIXME: Without records returns an empty list
    # With records returns: pydantic_core._pydantic_core.ValidationError: 2 validation errors for RolesOutputSchema

    async def get_by_name(self, name: str) -> Optional[RolesOutputSchema]:
        roles = await self._get_repository.get_roles_by_name(name)
        return RolesOutputSchema().validate(roles)
