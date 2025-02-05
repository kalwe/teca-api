from app.core.models.function_model import Function
from app.core.repositories.shared.delete_repository import DeleteRepository


class FunctionDeleteRepository(DeleteRepository):
    """
    Repository for managing function-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the function-specific delete repository.
        :param model_class: The Function class.
        """
        super().__init__(Function())
