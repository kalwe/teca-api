from typing import Any, Optional

from app.common.custom_exceptions import RepositoryError
from app.core.models.shared.base_model import ModelT


class UpdateRepository:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: ModelT):
        self._model_class = model_class

    async def update_record(
        self,
        record_fields: dict[str, Any],
    ) -> Optional[ModelT]:
        """
        Update fields for an existing record and increment its version.
        """
        try:
            record = await self._model_class.get(id=record_fields["id"])
            for key, value in record_fields.items():
                setattr(record, key, value)
            record.version += 1
            await record.save()
            return record
        except RepositoryError as e:
            raise RepositoryError(
                f"Failed UpdateRepository.update_record(): {e}"
            ) from e


type UpdateRepositoryT = UpdateRepository
