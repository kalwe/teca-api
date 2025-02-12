from typing import List, Optional

from app.common.custom_exceptions import RepositoryError
from app.core.models.user_model import User
from app.core.repositories.shared.get_repository import GetRepository


class UserGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the User model_class.

        Args:
            model_class ([User): The User model_class class to be managed by
            the repository.
        """
        super().__init__(User())

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by their email address.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            Optional[User]: The serialized user data or None if not found.
        """
        try:
            users = await self.get_all_records(filters={"email": email})
            return users[0] if users else None
        except RepositoryError as e:
            raise RepositoryError(
                f"Failed UserGetRepository.get_user_by_email(): {e}"
            ) from e

    async def get_users_by_role(self, role: str) -> List[User]:
        """
        Fetch users by their role and return serialized data.

        Args:
            role (str): The role to filter users by.

        Returns:
            List[User]: A list of serialized users with the specified role.
        """
        try:
            users = await self.get_all_records(roles__contains=[role])
            if not users:
                return None

            return users
        except RepositoryError as e:
            raise RepositoryError(f"Failed repository get_users_by_role(): {e}") from e

    async def get_user_by_name(self, name) -> Optional[User]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[User]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)
            return record
        except RepositoryError as e:
            raise RepositoryError(
                f"Failed UserGetRepository.get_user_by_name: {e}"
            ) from e
