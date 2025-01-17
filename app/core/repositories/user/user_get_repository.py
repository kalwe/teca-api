from typing import List, Optional
from app.core.models.user_model import User
from app.core.repositories.shared.get_repository import GetRepository


class UserGetRepository(GetRepository[User]):

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Fetch a user by their email address.
        """
        user = await self.model.filter(email=email).first()
        return user

    async def get_users_by_role(self, role: str) -> List[User]:
        """
        Fetch users by their role.
        """
        users = await self.model.filter(roles__contains=[role]).all()
        return users
