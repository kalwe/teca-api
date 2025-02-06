from typing import Optional
from app.api.schemas.reminder_schema import ReminderInputSchema, ReminderOutputSchema
from app.core.repositories.reminder.reminder_update_repository import (ReminderUpdateRepository)
from app.core.services.shared.update_service import UpdateService


class ReminderUpdateService(UpdateService):
    """
    Service for managing reminder-related business logic.
    """
    def __init__(self, repository: ReminderUpdateRepository):
        super().__init__(repository)

    async def update(
        self,
        id: int,
        reminder_data: ReminderInputSchema
    ) -> Optional[ReminderOutputSchema]:
        updated_reminder = await self.update_data(id, reminder_data)
        return ReminderOutputSchema.validate(updated_reminder)
