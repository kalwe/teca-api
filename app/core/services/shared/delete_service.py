from typing import Any, Generic, Optional, Type, TypeVar
from app.core.repositories.shared.delete_repository import DeleteRepository

T = TypeVar("T")


class DeleteService(Generic[T]):
    def __init__(self, repository: DeleteRepository[T]):
        self.repository = repository

    async def soft_delete(self, record) -> Optional[T]:
        return await self.repository.soft_delete_record(record)
