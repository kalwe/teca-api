from typing import Generic, Type, Optional, TypeVar

from app.common.datetime_utils import aware_utcnow

T = TypeVar("T")


class DeleteRepository(Generic[T]):
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model: Type[T]):
        self.model = model

    async def soft_delete_record(self, record: Type[T]) -> Optional[T]:
        """
        Perform a soft delete by marking a record as inactive and setting a deleted_at timestamp.
        """
        record.is_active = False
        record.deleted_at = aware_utcnow()
        await record.save()
        return record
