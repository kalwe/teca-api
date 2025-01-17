from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.shared.update_service import UpdateService


class UpdateUserService(UpdateService):
    """
    Service for managing user-related business logic.
    """

    def __init__(self):
        super().__init__(UserUpdateRepository)

    async def update(self, id, **data):
        return await super().update(id, **data)
