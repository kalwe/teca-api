from typing import List, Optional
from app.api.schemas.user_schema import UserOutputSchema
from app.common.crypto_utils import hash_password
from app.common.custom_exceptions import UserAlreadyExistsException
from app.core.models.user_model import User
from app.core.repositories.user.user_create_repository import (
    UserCreateRepository)
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.shared.create_service import CreateService
from app.core.services.user.get_user_service import UserGetService


class UserCreateService(CreateService[User]):
    """
    Service for managing user-related business logic.
    Handles creation of new users with role assignment and password hashing.
    """

    def __init__(self, repository: UserCreateRepository):
        """
        Initialize the service with a repository for user operations.

        Args:
            repository (UserCreateRepository): An instance of UserCreateRepository
                to handle data persistence for the User model.
        """
        super().__init__(repository)
        self.repository = repository

    async def create(
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
        user_get_repository = UserGetRepository()
        user_get_service = UserGetService(user_get_repository)
        existing_user = await user_get_service.get_user_by_email(
            email
        )
        if existing_user:
            raise UserAlreadyExistsException(
                f"User with email {email} already exists."
            )

        password_hash = hash_password(password)

        created_user = await self.create_record(
            username=username,
            email=email,
            password_hash=password_hash,
            roles=roles
        )
        return UserOutputSchema.model_validate(created_user)

# Instantiate the repository
# user_repository = UserCreateRepository(User)

# # Initialize the service
# user_service = UserCreateService(user_repository)
