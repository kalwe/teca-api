from app.core.models.clothing_model import Clothing
from app.core.repositories.shared.create_repository import CreateRepository


class ClothingCreateRepository(CreateRepository):
    """
    Repository for managing clothing-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Clothing model_class.

        Args:
            model_class: The Clothing model_class class
            to be managed by
            the repository.
        """
        super().__init__(Clothing())
