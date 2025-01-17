from typing import Type, List, Optional

from app.common.datetime_utils import aware_utcnow
from app.core.models.shared.base_entity import BaseEntity


class DeleteRepository:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model: Type[BaseEntity]):
        self.model = model

    async def soft_delete_record(self, record_id: int) -> Optional[BaseEntity]:
        """
        Perform a soft delete by marking a record as inactive and setting a deleted_at timestamp.
        """
        record = await self.get_by_id(record_id)
        if record is None:
            return None
        record.is_active = False
        # record.deleted_at = datetime.aware_utcnow()()
        record.deleted_at = aware_utcnow()
        await record.save()
        return record
