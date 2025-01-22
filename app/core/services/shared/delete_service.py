from typing import Any, Generic, Optional,  TypeVar
from app.core.repositories.shared.delete_repository import DeleteRepository

T = TypeVar("T")


class DeleteService(Generic[T]):
    """
    Base service for handling soft-delete operations.
    """

    def __init__(self, repository: DeleteRepository[T]):
        """
        Initialize the delete service with a repository instance.
        :param repository: The repository for managing delete operations.
        """
        self.repository = repository

    async def soft_delete(self, instance: T) -> Optional[T]:
        """
        Perform a soft delete operation on the given instance.
        :param instance: The model instance to soft delete.
        :return: The soft-deleted instance, or None if the operation fails.
        """
        try:
            deleted_record = self.repository.soft_delete_record(instance)
            return deleted_record
        except Exception as e:
            raise Exception(f"Failed service soft_delete(): {e}") from e
