from typing import List, Optional, TypeVar
from app.api.schemas.user_schema import UserOutputSchema, UserInputSchema
from app.common.crypto_utils import hash_password
from app.common.custom_exceptions import UserAlreadyExistsException
from app.core.models.user_model import UserModel
from app.core.repositories.user.user_create_repository import (
    UserCreateRepository)
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.shared.create_service import CreateService
from app.core.services.user.user_get_service import UserGetService


class UserCreateService(CreateService[UserModel]):
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
        # self.repository = repository
        self.get_service = UserGetService(UserGetRepository())

    async def create(self, user: UserInputSchema) -> UserOutputSchema:
        """
        Create a new user with additional business logic.

        Args:
            name (str): The name of the user.
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
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the user.

        Returns:
            UserOutputSchema: Serialized data of the created user.

        Raises:
            UserAlreadyExistsException: If a user with the given email already exists.
        """
        roles = user.roles or ["user"]  # Assign default role if none provided

        try:
            # Check if a user with the email already exists
            existing_user = await self.get_service.get_by_email(
                user.email
            )
            if existing_user:
                raise UserAlreadyExistsException(
                    f"User with email {user.email} already exists."
                )

            password_hash = hash_password(user.password_hash)

            created_user = await self.create_record(
                name=user.name,
                email=user.email,
                password_hash=password_hash,
                roles=roles
            )
            return UserOutputSchema().dump_json(created_user)
        except Exception as e:
            raise Exception(
                f"Failed UserCreateService().create(): {e}") from e
