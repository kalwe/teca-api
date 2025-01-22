from typing import Generic, Optional, TypeVar
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

    async def update_data(self, record, **fields_data) -> Optional[T]:
        try:
            updated_record = await self.repository.update_record(record,
                                                                 **fields_data)
            if not updated_record:
                return None

            return updated_record
        except Exception as e:
            raise Exception(f"Failed UpdateService.update_record")
