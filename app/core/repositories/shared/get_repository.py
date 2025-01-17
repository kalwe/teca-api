from typing import Generic, Type, List, Optional, TypeVar


T = TypeVar("T")


class GetRepository(Generic[T]):
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model: Type[T]):
        self.model = model

    async def get_by_id(self, record_id: int) -> Optional[T]:
        """
        Retrieve a record by its ID if it is active.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            Optional[T]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self.model.get_or_none(id=record_id, is_active=True)
            return record
        except Exception as e:
            raise Exception(
                f"Failed to retrieve record by ID {record_id}: {e}")

    async def get_all(self, filters: Optional[dict] = None) -> List[T]:
        """
        Retrieve all records, optionally applying filters.

        Args:
            filters (Optional[dict]): Filters to apply when fetching records.

        Returns:
            List[T]: A list of all matching records.
        """
        try:
            records = await (self.model.filter() if filters
                             else await self.model.all())
            return records
        except Exception as e:
            raise Exception(f"Failed to retrieve all records: {e}")
