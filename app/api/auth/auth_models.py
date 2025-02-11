from quart_auth import AuthUser

from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.user.user_get_service import UserGetService


class UserAuth(AuthUser):
    def __init__(self, auth_id):
        super().__init__(auth_id)
        self._resolved = False
        self._email = None
        self._get_service = UserGetService(UserGetRepository())

    async def _resolve(self):
        if not self._resolved:
            self._email = await self._get_service.get_by_name(self.auth_id)
            self._resolved = True

    @property
    async def email(self):
        await self._resolve()
        return self._email
