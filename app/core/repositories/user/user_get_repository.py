from typing import List, Optional, Type, TypeVar
from app.api.schemas.user_schema import UserOutputSchema
from app.core.models.user_model import UserModel
from app.core.repositories.shared.get_repository import GetRepository

T = TypeVar("T", bound=UserModel)


class UserGetRepository(GetRepository[UserModel]):
    def __init__(self, model_class: Type[UserModel]):
        """
        Initialize the repository with the User model_class.

        Args:
            model_class (type[User]): The User model_class class to be managed by
            the repository.
        """
        super().__init__(model_class)

    async def get_user_by_email(
        self,
        email: str
    ) -> Optional[UserModel]:
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            Optional[UserOutputSchema]: The serialized user data or None if not found.
        """
        try:
            user = await self.model_class.filter(email=email).first()
            if not user:
                return None

            return user
        except Exception as e:
            raise Exception(
                f"Failed repository get_user_by_email(): {e}") from e

    async def get_users_by_role(self, role: str) -> List[UserModel]:
        """
        Fetch users by their role and return serialized data.

        Args:
            role (str): The role to filter users by.

        Returns:
            List[UserOutputSchema]: A list of serialized users with the specified role.
        """
        try:
            users = await self.model_class.filter(roles__contains=[role]).all()
            if not users:
                return None

            return users
        except Exception as e:
            raise Exception(
                f"Failed repository get_users_by_role(): {e}") from e
