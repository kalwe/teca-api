from typing import Generic, TypeVar
from app.core.repositories.shared.create_repository import CreateRepository

T = TypeVar("T")


class CreateService(Generic[T]):
    """
    Generic service layer for creating new records using a repository.
    """

    def __init__(self, repository: CreateRepository[T]):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[CreateRepository[T]]): The repository
                class used for data creation.
        """
        self.repository = repository

    async def create_record(self, **fields_data) -> T:
        """
        Create a new record in the repository.

        Args:
            **fields_data: The fields and their values for the new record.

        Returns:
            T: The newly created record.
        """
        created_record = await self.repository.create_record(**fields_data)
        return created_record
