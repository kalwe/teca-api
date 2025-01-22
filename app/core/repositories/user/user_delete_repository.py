from typing import Type, TypeVar
from app.core.models.user_model import UserModel
from app.core.repositories.shared.delete_repository import DeleteRepository

T = TypeVar("T", bound=UserModel)


class UserDeleteRepository(DeleteRepository[UserModel]):
    """
    Repository for managing user-related soft deletes.
    """

    def __init__(self, model_class: Type[UserModel]):
        """
        Initialize the user-specific delete repository.
        :param model_class: The UserModel class.
        """
        super().__init__(model_class)
