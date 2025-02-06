from app.core.models.reminder_model import Reminder
from app.core.repositories.shared.update_repository import UpdateRepository


class ReminderUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Reminder)
