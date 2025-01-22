from typing import Generic, Type, Optional, TypeVar

from app.core.models.shared.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class DeleteRepository(Generic[T]):
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: Type[T]):
        """
        Initialize the repository with the model class.
        :param model_class: The model class to operate on.
        """
        self.model_class = model_class

    async def soft_delete_record(self, instance: T) -> Optional[T]:
        """
        Perform a soft delete by marking a record as inactive and setting
        a deleted_at timestamp.

        :param instance: The model instance to soft delete.
        :return: The updated model instance, or None if the operation fails.
        """
        instance.deactivate_record()
        try:
            await instance.save()
            return instance
        except Exception as e:
            raise Exception(
                f"Failed DeleteRepository().soft_delete(): {e}") from e
