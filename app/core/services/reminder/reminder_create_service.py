from typing import Optional

from app.api.schemas.reminder_schema import ReminderInputSchema, ReminderOutputSchema
from app.core.repositories.reminder.reminder_create_repository import (
    ReminderCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class ReminderCreateService(CreateService):
    """
    Service for managing reminder-related business logic.
    Handles creation of new reminders with role assignment and password hashing.
    """

    def __init__(self, repository: ReminderCreateRepository):
        """
        Initialize the service with a repository for reminder operations.

        Args:
            repository (ReminderCreateRepository): An instance of
                ReminderCreateRepository
                to handle data persistence for the Reminder model.
        """
        super().__init__(repository)
        # self._get_service = ReminderGetService(ReminderGetRepository(Reminder()))

    async def create(
        self,
        reminder_data: ReminderInputSchema,
    ) -> Optional[ReminderOutputSchema]:
        (
            """
        Create a new reminder with additional business logic.

        Args:
            name (str): The name of the reminder.
            email (str): The email of the reminder.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the reminder.

        Returns:
            ReminderOutputSchema: Serialized data of the created reminder.

        Raises:
            ReminderAlreadyExistsException: If a reminder with the given email
            already exists.
        """
            """
        Create a new reminder with additional business logic.

        Args:
            name (str): The name of the reminder.
            email (str): The email of the reminder.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the reminder.

        Returns:
            ReminderOutputSchema: Serialized data of the created reminder.

        Raises:
            ReminderAlreadyExistsException: If a reminder with the given email
            already exists.
        """
        )
        created_reminder = await self.create_record(reminder_data)
        return ReminderOutputSchema().validate(created_reminder)


# FIXME: <p>Failed to decode JSON: Expecting property name enclosed in double quotes: line 5 column 1 (char 74)</p>
