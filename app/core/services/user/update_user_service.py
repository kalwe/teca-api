from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.shared.update_service import UpdateService
from app.core.services.user.get_user_service import UserGetService


class UserUpdateService(UpdateService):
    """
    Service for managing user-related business logic.
    """

    def __init__(self, model):
        super().__init__(model)

    async def update(self, id, data):
        get_service = UserGetService()
        record = await get_service.get(id)
        if record is None:
            return None
        record_updated = await self.update_record(id, data)
        return record_updated
