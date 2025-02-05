from typing import Any, Optional

# from app.core.models.shared.base_model import BaseModel
from app.common.custom_exceptions import RepositoryError
from app.core.models.shared.base_model import ModelT
# from app.api.schemas.base_schema import SchemaT


class DeleteRepository:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: ModelT):
        """
        Initialize the repository with the model class.
        :param model_class: The model class to operate on.
        """
        self._model_class = model_class

    async def soft_delete_record(self, record: ModelT) -> Optional[ModelT]:
        """
        Perform a soft delete by marking a record as inactive and setting
        a deleted_at timestamp.

        :param instance: The model instance to soft delete.
        :return: The updated model instance, or None if the operation fails.
        """
        try:
            record.deactivate_record()
            await record.save()
            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed DeleteRepository().soft_delete_record(): {e}") from e
