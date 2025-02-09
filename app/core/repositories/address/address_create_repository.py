from app.core.models.address_model import Address
from app.core.repositories.shared.create_repository import CreateRepository


class AddressCreateRepository(CreateRepository):
    """
    Repository for managing address-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Address model_class.

        Args:
            model_class: The Address model_class class
            to be managed by
            the repository.
        """
        super().__init__(Address())
