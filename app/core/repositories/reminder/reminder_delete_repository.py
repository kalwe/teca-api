from app.core.models.reminder_model import Reminder
from app.core.repositories.shared.delete_repository import DeleteRepository


class ReminderDeleteRepository(DeleteRepository):
    """
    Repository for managing reminder-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the reminder-specific delete repository.
        :param model_class: The Reminder class.
        """
        super().__init__(Reminder())
