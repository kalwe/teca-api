from typing import Optional

from app.core.models.shared.base_model import BaseModel


class DeleteRepository[T: BaseModel]:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: T):
        """
        Initialize the repository with the model class.
        :param model_class: The model class to operate on.
        """
        self.model_class = model_class

    async def soft_delete_record(self) -> Optional[T]:
        """
        Perform a soft delete by marking a record as inactive and setting
        a deleted_at timestamp.

        :param instance: The model instance to soft delete.
        :return: The updated model instance, or None if the operation fails.
        """
        # instance.deactivate_record()
        self.model_class.deactivate_record
        try:
            await self.model_class.save()
            return self.model_class
        except Exception as e:
            raise Exception(
                f"Failed DeleteRepository().soft_delete(): {e}") from e
