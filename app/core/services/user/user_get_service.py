from typing import List, Optional, TypeVar
from app.api.schemas.user_schema import UserOutputSchema
from app.core.models.user_model import UserModel
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.shared.get_service import GetService


class UserGetService(GetService[UserModel]):
    """
    Service for managing user-related business logic, leveraging generic
    methods from GetService.

    This service adds user-specific business logic on top of the generic
    functionality provided by GetService.
    """

    def __init__(self, repository: UserGetRepository):
        """
        Initialize the service with a User-specific repository.

        Args:
            repository (UserGetRepository): Repository for user
            data retrieval.
        """
        super().__init__(repository)
        self.repository = repository

    async def get(self, id: int) -> Optional[UserOutputSchema]:
        try:
            user = self.get_by_id(id)
            if not user:
                return None

            return UserOutputSchema.dump_json(user)
        except Exception as e:
            raise Exception(
                f"Failed UserGetService().get(): {e}") from e

    async def get_all(self) -> Optional[List[UserOutputSchema]]:
        try:
            users = self.get_all()
            if not users:
                return None

            return [UserOutputSchema.dump_json(user) for user in users]
        except Exception as e:
            raise Exception(
                f"Failed UserGetService().get_all(): {e}") from e

    async def get_by_email(self, email: str) -> Optional[UserOutputSchema]:
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            Optional[UserOutputSchema]: The serialized user data or None
            if not found.
        """
        try:
            user = await self.repository.get_user_by_email(email)
            if not user:
                return None

            return UserOutputSchema.validate(user)
        except Exception as e:
            raise Exception(
                f"Failed UserGetService().get_by_email(): {e}") from e

    async def get_by_role(self, role: str) -> List[UserOutputSchema]:
        """
        Retrieve users by their role.

        Args:
            role (str): The role to filter users by.

        Returns:
            List[UserOutputSchema]: A list of serialized users with the
            specified role.
        """
        try:
            users = await self.repository.get_users_by_role(role)
            if not users:
                return None

            return [UserOutputSchema.dump_json(user) for user in users]
        except Exception as e:
            raise Exception(
                f"Failed UserGetService().get_by_role(): {e}") from e
