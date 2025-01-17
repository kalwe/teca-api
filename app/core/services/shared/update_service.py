from typing import Generic, TypeVar
from app.core.repositories.shared.update_repository import UpdateRepository

T = TypeVar("T")


class UpdateService(Generic[T]):
    def __init__(self, repository: UpdateRepository[T]):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[UpdateRepository[T]]): The repository
            class used for data update.
        """
        self.repository = repository

    async def update_record(self, record, **fields_data) -> T:
        updated_record = await self.repository.update_record(record,
                                                             **fields_data)
        return updated_record
