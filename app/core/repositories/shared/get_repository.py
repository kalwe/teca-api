from typing import List, Optional

from app.core.models.shared.base_model import BaseModel


class GetRepository[T: BaseModel]:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: T):
        """
        Initialize the repository with the model class.
        :param model_class: The model class to operate on.
        """
        self.model_class = model_class

    async def get_record_by_id(self) -> Optional[T]:
        """
        Retrieve a record by its ID if it is active.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            Optional[T]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self.model_class.get_or_none(id=self.model_class.id,
                                                        is_active=True)
            return record
        except Exception as e:
            raise Exception(
                f"Failed to retrieve record by ID {self.model_class.id}: {e}") from e

    async def get_all_records(
        self,
        filters: Optional[dict] = None
    ) -> Optional[List[T]]:
        """
        Retrieve all records, optionally applying filters.

        Args:
            filters (Optional[dict]): Filters to apply when fetching records.

        Returns:
            List[T]: A list of all matching records.
        """
        try:
            records = await (self.model_class.filter(filters) if filters
                             else await self.model_class.all())
            if not records:
                return None

            return records
        except Exception as e:
            raise Exception(f"Failed to retrieve all records: {e}") from e
