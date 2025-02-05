from app.core.models.reminder_model import Reminder
from app.core.repositories.shared.create_repository import CreateRepository


class ReminderCreateRepository(CreateRepository):
    """
    Repository for managing reminder-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Reminder model_class.

        Args:
            model_class: The Reminder model_class class
            to be managed by
            the repository.
        """
        super().__init__(Reminder())
