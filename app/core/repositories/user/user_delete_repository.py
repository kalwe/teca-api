from app.core.models.user_model import User
from app.core.repositories.shared.delete_repository import DeleteRepository


class UserDeleteRepository(DeleteRepository[User]):
    """
    Repository for managing user-related soft deletes.
    """

    def __init__(self, model_class: User):
        """
        Initialize the user-specific delete repository.
        :param model_class: The User class.
        """
        super().__init__(model_class=model_class)
