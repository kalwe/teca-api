from app.core.models.roles_model import Role
from app.core.repositories.shared.create_repository import CreateRepository


class RolesCreateRepository(CreateRepository):
    """
    Repository for managing roles-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Roles model_class.

        Args:
            model_class: The Roles model_class class
            to be managed by
            the repository.
        """
        super().__init__(Role())
