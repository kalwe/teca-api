from app.core.models.function_model import Function
from app.core.repositories.shared.create_repository import CreateRepository


class FunctionCreateRepository(CreateRepository):
    """
    Repository for managing function-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Function model_class.

        Args:
            model_class: The Function model_class class
            to be managed by
            the repository.
        """
        super().__init__(Function())
from app.core.models.function_model import Function
from app.core.repositories.shared.create_repository import CreateRepository


class FunctionCreateRepository(CreateRepository):
    """
    Repository for managing function-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Function model_class.

        Args:
            model_class: The Function model_class class
            to be managed by
            the repository.
        """
        super().__init__(Function())
