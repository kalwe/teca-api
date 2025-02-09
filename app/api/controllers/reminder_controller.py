from http import HTTPStatus
from typing import List

from quart_schema import validate_request, validate_response

from app.api.schemas.reminder_schema import (
    ReminderDeletedSchema,
    ReminderInputSchema,
    ReminderOutputSchema,
)
from app.core.repositories.reminder.reminder_create_repository import (
    ReminderCreateRepository,
)
from app.core.repositories.reminder.reminder_delete_repository import (
    ReminderDeleteRepository,
)
from app.core.repositories.reminder.reminder_get_repository import ReminderGetRepository
from app.core.repositories.reminder.reminder_update_repository import (
    ReminderUpdateRepository,
)
from app.core.services.reminder.reminder_create_service import ReminderCreateService
from app.core.services.reminder.reminder_delete_service import ReminderDeleteService
from app.core.services.reminder.reminder_get_service import ReminderGetService
from app.core.services.reminder.reminder_update_service import ReminderUpdateService


class ReminderController:
    """
    Controller that handles reminder-related HTTP requests.
    """

    @staticmethod
    @validate_request(ReminderInputSchema)
    @validate_response(ReminderOutputSchema)
    async def create_reminder(data: ReminderInputSchema) -> ReminderOutputSchema:
        """
        Creates a new reminder from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the reminder data and the
            HTTP status code.
        """
        repository = ReminderCreateRepository()
        service = ReminderCreateService(repository)
        reminder = await service.create(data)
        return reminder, HTTPStatus.CREATED

    @staticmethod
    @validate_response(ReminderOutputSchema)
    async def get_reminder(id: int) -> ReminderOutputSchema:
        """
        Retrieves a reminder by ID.

        Args:
            id (str): The ID of the reminder to retrieve.

        Returns:
            Tuple: A tuple containing the reminder data (or an error message)
            and the HTTP status code.
        """
        repository = ReminderGetRepository()
        service = ReminderGetService(repository)
        reminder = await service.get(id)
        return reminder, HTTPStatus.OK

    @staticmethod
    @validate_response(List[ReminderOutputSchema])
    async def get_all_reminders() -> List[ReminderOutputSchema]:
        """
        Retrieves all reminders using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of reminders
            (or an error message)
            and the HTTP status code.
        """
        repository = ReminderGetRepository()
        service = ReminderGetService(repository)
        reminders = await service.get_all()
        return reminders, HTTPStatus.OK

    @staticmethod
    @validate_request(ReminderInputSchema)
    @validate_response(ReminderOutputSchema)
    async def update_reminder(
        id: int, data: ReminderInputSchema
    ) -> ReminderOutputSchema:
        repository = ReminderUpdateRepository()
        service = ReminderUpdateService(repository)
        reminder = await service.update(id, data)
        return reminder, HTTPStatus.OK

    @staticmethod
    @validate_response(ReminderDeletedSchema)
    async def delete_reminder(id: int) -> ReminderDeletedSchema:
        repository = ReminderDeleteRepository()
        service = ReminderDeleteService(repository)
        reminder = service.delete(id)
        return reminder, HTTPStatus.NO_CONTENT
