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
        record_exist = await self._get_service.get_by_id(id)
        if not record_exist:
            return None
        self._repository._model_class.version += record_exist.version
        data_fields = data_field.dump(exclude_unset=True)
        updated_data = await self._repository.update_record(data_fields)
        # SchemaT should be OutputSchemaT
        # validated_schema = data_field.validate(updated_data)
        # return validated_schema
        return updated_data
