from typing import Optional
from app.core.common.custom_types import DeleteRepositoryT, ModelT
from app.core.repositories.shared.get_repository import GetRepository


class DeleteService:
    """
    Base service for handling soft-delete operations.
    """

    def __init__(self, repository: DeleteRepositoryT):
        """
        Initialize the delete service with a repository instance.
        :param repository: The repository for managing delete operations.
        """
        self._repository = repository
        self._get_repository = GetRepository(repository._model_class)

    async def soft_delete(self, id: int) -> Optional[ModelT]:
        """
        Perform a soft delete operation on the given instance.
        :param instance: The model instance to soft delete.
        :return: The soft-deleted instance, or None if the operation fails.
        """
        if id <= 0:
            return None

        record = self._get_repository.get_record_by_id(id)
        if not record:
            return None

        deleted_record = self._repository.soft_delete_record(record)
        return deleted_record
