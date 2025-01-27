from typing import List, Optional
from app.core.models.shared.base_model import BaseModel
from app.core.repositories.shared.get_repository import GetRepository


class GetService[T]:
    """
    Generic service layer for retrieving data using a repository.
    """

    def __init__(self, repository: GetRepository):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[GetRepository[T]]): The repository class
            used for data access.
        """
        self.repository = repository

    async def get_by_id(self) -> Optional[T]:
        """
        Retrieve a single record by its ID.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            Optional[T]: The retrieved record if found, otherwise None.
        """
        model_class = self.repository.model_class
        try:
            if self.repository.model_class.id <= 0:
                raise ValueError(f"Invalid record ID: {model_class.id}")

            record = await self.repository.get_record_by_id()
            if not record:
                return None

            return record
        except Exception as e:
            raise Exception(f"Failed GetService().get_by_id(): {e}") from e

    async def get_all_records(self, filters: Optional[dict] = None
                              ) -> Optional[List[T]]:
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
