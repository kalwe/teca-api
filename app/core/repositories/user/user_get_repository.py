from typing import List, Optional
from app.api.schemas.user_schema import UserOutputSchema
from app.core.models.user_model import User
from app.core.repositories.shared.get_repository import GetRepository


class UserGetRepository(GetRepository[User]):
    def __init__(self, model: type[User]):
        """
        Initialize the repository with the User model.

        Args:
            model (type[User]): The User model class to be managed by
            the repository.
        """
        super().__init__(model)

    async def get_user_by_email(
        self,
        email: str
    ) -> Optional[UserOutputSchema]:
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            Optional[UserOutputSchema]: The serialized user data or None if not found.
        """
        user = await self.model.filter(email=email).first()
        if user:
            return UserOutputSchema.model_validate(user)
        return None

    async def get_users_by_role(self, role: str) -> List[UserOutputSchema]:
        """
        Fetch users by their role and return serialized data.

        Args:
            role (str): The role to filter users by.

        Returns:
            List[UserOutputSchema]: A list of serialized users with the specified role.
        """
        users = await self.model.filter(roles__contains=[role]).all()
        return [UserOutputSchema.model_validate(user) for user in users]
