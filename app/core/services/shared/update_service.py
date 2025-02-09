from typing import Optional

from app.api.schemas.base_schema import SchemaT
from app.core.models.shared.base_model import ModelT
from app.core.repositories.shared.get_repository import GetRepository
from app.core.repositories.shared.update_repository import UpdateRepositoryT
from app.core.services.shared.get_service import GetService


class UpdateService:
    def __init__(self, repository: UpdateRepositoryT):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[UpdateRepositoryT]): The repository
            class used for data update.
        """
        self._repository = repository
        self._get_repository = GetRepository(repository._model_class)
        self._get_service = GetService(self._get_repository)

    async def update_data(self, id: int, data_field: SchemaT) -> Optional[ModelT]:
        record_exist = self._get_service.get_by_id(id)
        if not record_exist:
            return None

        # TODO: use fields = record_fields.dump(exclude_unset=True)
        #       update_record(**data_field)
        updated_record = await self._repository.update_record(data_field)
        return updated_record
