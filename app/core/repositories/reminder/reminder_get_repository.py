from app.core.models.reminder_model import Reminder
from app.core.repositories.shared.get_repository import GetRepository


class ReminderGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Reminder model_class.

        Args:
            model_class ([Reminder): The Reminder model_class class to be managed by
            the repository.
        """
        super().__init__(Reminder())
