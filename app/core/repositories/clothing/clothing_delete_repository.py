from app.core.models.clothing_model import Clothing
from app.core.repositories.shared.delete_repository import DeleteRepository


class ClothingDeleteRepository(DeleteRepository):
    """
    Repository for managing clothing-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the clothing-specific delete repository.
        :param model_class: The Clothing class.
        """
        super().__init__(Clothing())
