from typing import Optional
from app.api.schemas.reminder_schema import (
    ReminderDeletedSchema, ReminderOutputSchema)
from app.core.repositories.reminder.reminder_delete_repository import (
    ReminderDeleteRepository)
from app.core.services.shared.delete_service import DeleteService


class ReminderDeleteService(DeleteService):
    """
    Service for managing reminder-related delete business logic.
    """

    def __init__(self, repository: ReminderDeleteRepository):
        """
        Initialize the reminder delete service.
        :param repository: The reminder delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[ReminderOutputSchema]:
        """
        Delete a reminder by ID.
        :param id: The ID of the reminder to delete.
        :return: The deleted reminder as a schema, or None if not found.
        """
        deleted_reminder = await self.soft_delete(id)
        return ReminderDeletedSchema.validate(deleted_reminder)
