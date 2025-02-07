from app.core.models.user_model import User
from app.core.repositories.shared.delete_repository import DeleteRepository


class UserDeleteRepository(DeleteRepository):
    """
    Repository for managing user-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the user-specific delete repository.
        :param model_class: The User class.
        """
        super().__init__(User())
