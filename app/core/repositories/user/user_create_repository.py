from app.core.models.user_model import User
from app.core.repositories.shared.create_repository import CreateRepository


class UserCreateRepository(CreateRepository):
    """
    Repository for managing user-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the User model_class.

        Args:
            model_class: The User model_class class
            to be managed by
            the repository.
        """
        super().__init__(User())
