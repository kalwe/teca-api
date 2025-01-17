import hashlib
from typing import List, Optional
from app.api.schemas.user_schema import UserOutputSchema
from app.common.custom_exceptions import UserAlreadyExistsException
from app.core.repositories.user.user_create_repository import UserCreateRepository
from app.core.services.user.get_user_service import UserGetService


class UserCreateService():
    """
    Service for managing user-related business logic.
    Handles creation of new users with role assignment and password hashing.
    """

    def __init__(self):
        self._repository = UserCreateRepository()

    async def create_user(
        self,
        username: str,
        email: str,
        password: str,
        roles: Optional[List[str]] = None
    ) -> UserOutputSchema:
        """
        Create a new user with additional business logic.

        Args:
            username (str): The username of the user.
            email (str): The email of the user.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the user.

        Returns:
            UserOutputSchema: Serialized data of the created user.

        Raises:
            UserAlreadyExistsException: If a user with the given email already exists.
        """        """
        Create a new user with additional business logic.

        Args:
            username (str): The username of the user.
            email (str): The email of the user.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the user.

        Returns:
            UserOutputSchema: Serialized data of the created user.

        Raises:
            UserAlreadyExistsException: If a user with the given email already exists.
        """
        roles = roles or ["user"]  # Assign default role if none provided

        # Check if a user with the email already exists
        user_get_service = UserGetService()
        existing_user = await user_get_service.repository.get_user_by_email(
            email
        )
        if existing_user:
            raise UserAlreadyExistsException(
                f"User with email {email} already exists."
            )

        password_hash = self._hash_password(password)

        created_user = await self._repository.create_record(
            username=username,
            email=email,
            password_hash=password_hash,
            roles=roles
        )
        return UserOutputSchema.from_orm(created_user)

    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hash the given password using SHA-256.

        Args:
            password (str): The plain-text password to hash.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()
