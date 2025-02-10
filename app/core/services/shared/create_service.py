from typing import Optional

from app.api.schemas.base_schema import SchemaT
from app.core.models.shared.base_model import ModelT
from app.core.repositories.shared.create_repository import CreateRepositoryT


class CreateService:
    """
    Generic service layer for creating new records using a repository.
    """

    def __init__(self, repository: CreateRepositoryT):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[CreateRepository[T]]): The repository
                class used for data creation.
        """
        self._repository = repository

    async def create_record(self, data_fields: SchemaT) -> Optional[ModelT]:
        """
        Create a new record in the repository.

        Args:
            **fields_data: The fields and their values for the new record.

        Returns:
            T: The newly created record.
        """
        dumped_fields = data_fields.dump()
        created_record = await self._repository.model_create(dumped_fields)
        return created_record
