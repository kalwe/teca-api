from typing import Any, Optional, Type
from app.core.repositories.shared.delete_repository import DeleteRepository


class DeleteService():
    def __init__(self, repository_class: Type[DeleteRepository]):
        self.repository = repository_class

    async def soft_delete(self, id: int) -> Optional[Any]:
        return await self.repository.soft_delete_record(id)
