from app.core.models.roles_model import Role
from app.core.repositories.shared.delete_repository import DeleteRepository


class RolesDeleteRepository(DeleteRepository):
    """
    Repository for managing roles-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the roles-specific delete repository.
        :param model_class: The Roles class.
        """
        super().__init__(Role())
