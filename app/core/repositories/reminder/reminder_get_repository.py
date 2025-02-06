from typing import Optional
from app.common.custom_exceptions import RepositoryError
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


    async def get_reminder_by_name(self, name) -> Optional[Reminder]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Reminder]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed ReminderGetRepository.get_reminder_by_name: {e}") from e
