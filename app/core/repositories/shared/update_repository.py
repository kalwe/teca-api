from typing import Generic, Type, List, Optional, TypeVar

from app.core.models.shared.base_entity import BaseEntity

T = TypeVar("T")


class UpdateRepository(Generic[T]):
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model: Type[T]):
        self.model = model

    async def update_record(
        self, record_id: int, **fields_data
    ) -> T:
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
