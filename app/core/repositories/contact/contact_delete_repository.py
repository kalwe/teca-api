from app.core.models.contact_model import Contact
from app.core.repositories.shared.delete_repository import DeleteRepository


class ContactDeleteRepository(DeleteRepository):
    """
    Repository for managing contact-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the contact-specific delete repository.
        :param model_class: The Contact class.
        """
        super().__init__(Contact())
