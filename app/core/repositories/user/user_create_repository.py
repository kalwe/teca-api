from typing import Type, TypeVar
from app.core.models.user_model import UserModel
from app.core.repositories.shared.create_repository import CreateRepository

T = TypeVar("T", bound=UserModel)


class UserCreateRepository(CreateRepository[UserModel]):
    """
    Repository for managing user-related create .
    """

    def __init__(self, model_class: Type[UserModel]):
        """
        Initialize the repository with the User model_class.

        Args:
            model_class: The User model_class class
            to be managed by
            the repository.
        """
        super().__init__(model_class)
