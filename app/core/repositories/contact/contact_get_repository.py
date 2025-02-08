from app.core.models.contact_model import Contact
from app.core.repositories.shared.get_repository import GetRepository


class ContactGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Contact model_class.

        Args:
            model_class ([Contact): The Contact model_class class to be managed by
            the repository.
        """
        super().__init__(Contact())
