from typing import Optional

from app.api.schemas.base_schema import SchemaT
from app.core.models.shared.base_model import ModelT


class UpdateRepository:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: ModelT):
        self._model_class = model_class

    async def update_record(self, record_fields: SchemaT) -> Optional[ModelT]:
        """
        Update fields for an existing record and increment its version.
        """
        try:
            fields = record_fields.dump(exclude_unset=True)
            self._model_class.update_from_dict(**fields)
            self._model_class.version += 1
            await self._model_class.save()
            return self._model_class
        except Exception as e:
            raise Exception(
                f"Failed UpdateRepository.update_record(): {e}") from e

type UpdateRepositoryT = UpdateRepository
