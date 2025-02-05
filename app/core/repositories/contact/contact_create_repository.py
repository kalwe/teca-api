from app.core.models.contact_model import Contact
from app.core.repositories.shared.create_repository import CreateRepository


class ContactCreateRepository(CreateRepository):
    """
    Repository for managing contact-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Contact model_class.

        Args:
            model_class: The Contact model_class class
            to be managed by
            the repository.
        """
        super().__init__(Contact())
