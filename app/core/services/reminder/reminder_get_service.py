from typing import List, Optional
from app.api.schemas.reminder_schema import ReminderOutputSchema
from app.core.repositories.reminder.reminder_get_repository import (
    ReminderGetRepository)
from app.core.services.shared.get_service import GetService


class ReminderGetService(GetService):
    """
    Service for managing reminder-related business logic, leveraging generic
    methods from GetService.

    This service adds reminder-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = ReminderGetRepository

    def __init__(self, repository: ReminderGetRepository):
        """
        Initialize the service with a Reminder-specific repository.

        Args:
            repository (ReminderGetRepository): Repository for reminder
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[ReminderOutputSchema]:
        reminder = self.get_by_id(id)
        return ReminderOutputSchema.validate(reminder)

    async def get_all(self, filters: Optional[dict] = None
                      ) -> Optional[List[ReminderOutputSchema]]:
        reminders = self.get_all_records(filters)
        return [ReminderOutputSchema.validate(reminder) for reminder in reminders]

    async def get_by_name(self, name: str) -> Optional[ReminderOutputSchema]:
        reminder = self._get_repository.get_reminder_by_name(name)
        return ReminderOutputSchema.validate(reminder)
