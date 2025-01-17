from app.core.models.user_model import User
from app.core.repositories.shared.create_repository import CreateRepository


class UserCreateRepository(CreateRepository[User]):
    def __init__(self, model: type[User]):
        """
        Initialize the repository with the User model.

        Args:
            model (type[User]): The User model class to be managed by
            the repository.
        """
        super().__init__(model)
