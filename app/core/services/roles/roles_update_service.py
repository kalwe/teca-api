from typing import Optional

from app.api.schemas.roles_schema import RolesInputSchema, RolesOutputSchema
from app.core.repositories.roles.roles_update_repository import RolesUpdateRepository
from app.core.services.shared.update_service import UpdateService


class RolesUpdateService(UpdateService):
    """
    Service for managing roles-related business logic.
    """

    def __init__(self, repository: RolesUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, roles_data: RolesInputSchema
    ) -> Optional[RolesOutputSchema]:
        updated_roles = await self.update_data(id, roles_data)
        return RolesOutputSchema().validate(updated_roles)
