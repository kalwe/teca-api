from typing import Any, Optional, Type
from app.core.repositories.shared.update_repository import UpdateRepository
from app.core.services.shared.get_service import GetService


class UpdateService(UpdateRepository):

    async def update(self, id, data):
        record_updated = await self.update_record(id, data)
        return record_updated
