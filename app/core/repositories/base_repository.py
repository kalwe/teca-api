from datetime import datetime
from typing import Type, List, Optional

from app.models.base import BaseEntity

class BaseRepository:
    """
    Abstract repository that defines common database operations.
    """
    def __init__(self, model_class: Type[BaseEntity]):
        self.model_class = model_class

    async def get_by_id(self, record_id: int) -> Optional[BaseEntity]:
        """
        Retrieve a record by its ID if it is active.
        """
        return await self.model_class.get_or_none(id=record_id, is_active=True)

    async def list_all_active(self) -> List[BaseEntity]:
        """
        Retrieve all active records.
        """
        return await self.model_class.filter(is_active=True).all()

    async def create_record(self, **fields_data) -> BaseEntity:
        """
        Create a new record in the database.
        """
        return await self.model_class.create(**fields_data)

    async def update_record(self, record_id: int, **fields_data) -> Optional[BaseEntity]:
        """
        Update fields for an existing record and increment its version.
        """
        record = await self.get_by_id(record_id)
        if record is None:
            return None
        for field_name, value in fields_data.items():
            setattr(record, field_name, value)
        record.version += 1
        await record.save()
        return record

    async def soft_delete_record(self, record_id: int) -> Optional[BaseEntity]:
        """
        Perform a soft delete by marking a record as inactive and setting a deleted_at timestamp.
        """
        record = await self.get_by_id(record_id)
        if record is None:
            return None
        record.is_active = False
        record.deleted_at = datetime.utcnow()
        await record.save()
        return record
