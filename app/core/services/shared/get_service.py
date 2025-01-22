from typing import Generic, List, Optional, Type, TypeVar
from app.core.repositories.shared.get_repository import GetRepository


T = TypeVar("T")


class GetService(Generic[T]):
    """
    Generic service layer for retrieving data using a repository.
    """

    def __init__(self, repository: GetRepository[T]):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[GetRepository[T]]): The repository class
            used for data access.
        """
        self.repository = repository

    async def get_by_id(self, record_id: int) -> Optional[T]:
        """
        Retrieve a single record by its ID.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            Optional[T]: The retrieved record if found, otherwise None.
        """
        try:
            if record_id <= 0:
                raise ValueError(f"Invalid record ID: {record_id}")
            record = await self.repository.get_record_by_id(record_id=record_id)
            if not record:
                return None

            return record
        except Exception as e:
            raise Exception(f"Failed GetService().get_by_id(): {e}") from e

    async def get_all(self, filters: Optional[dict] = None) -> Optional[List[T]]:
        """
        Retrieve all records from the repository.

        Returns:
            List[T]: A list of all retrieved records.
        """
        try:
            records = await self.repository.get_all_records(filters=filters)
            if not records:
                return None

            return records
        except Exception as e:
            raise Exception(f"Failed GetService().get_all(): {e}") from e
