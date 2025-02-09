from app.core.models.address_model import Address
from app.core.repositories.shared.delete_repository import DeleteRepository


class AddressDeleteRepository(DeleteRepository):
    """
    Repository for managing address-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the address-specific delete repository.
        :param model_class: The Address class.
        """
        super().__init__(Address())
