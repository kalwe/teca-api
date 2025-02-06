from typing import List, Optional
from app.core.models.shared.base_model import ModelT
from app.core.repositories.shared.get_repository import GetRepositoryT


class GetService:
    """
    Generic service layer for retrieving data using a repository.
    """

    def __init__(self, repository: GetRepositoryT):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[GetRepository[T]]): The repository class
            used for data access.
        """
        self._repository = repository

    async def get_by_id(self, id: int) -> Optional[ModelT]:
        """
        Retrieve a single record by its ID.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            Optional[T]: The retrieved record if found, otherwise None.
        """
        if id <= 0:
            raise ValueError(f"Invalid record ID: {id}")

        record = await self._repository.get_record_by_id(id)
        return record

    async def get_all_records(self, filters: Optional[dict] = None
                              ) -> Optional[List[ModelT]]:
        """
        Retrieve all records from the repository.

        Returns:
            List[T]: A list of all retrieved records.
        """
        records = await self._repository.get_all_records(filters=filters)
        return records
