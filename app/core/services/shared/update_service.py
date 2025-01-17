from typing import Any, Optional, Type
from app.core.repositories.shared.update_repository import UpdateRepository


class UpdateService():
    def __init__(self, repository_class: Type[UpdateRepository]):
        self.repository = repository_class

    async def update(self, id: int, **data) -> Optional[Any]:
        return await self.repository.update_record(id, **data)
