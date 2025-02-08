from app.core.models.address_model import Address
from app.core.repositories.shared.get_repository import GetRepository


class AddressGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Address model_class.

        Args:
            model_class ([Address): The Address model_class class to be managed by
            the repository.
        """
        super().__init__(Address())
