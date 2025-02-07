from typing import Optional
from app.core.repositories.shared.get_repository import GetRepository
from app.core.common.custom_types import UpdateRepositoryT, ModelT, SchemaT
from app.core.services.shared.get_service import GetService


class UpdateService:
    def __init__(self, repository: UpdateRepositoryT):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[UpdateRepository[T]]): The repository
            class used for data update.
        """
        self._repository = repository
        self._get_repository = GetRepository(repository._model_class)
        self._get_service = GetService(GetRepository(repository._model_class))

    async def update_data(self, id: int, data_field: SchemaT) -> Optional[ModelT]:
        record_exist = self._get_service.get_by_id(id)
        if not record_exist:
            return None

        updated_record = await self._repository.update_record(data_field)
        return updated_record
