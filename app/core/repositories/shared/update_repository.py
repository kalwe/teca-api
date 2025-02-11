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
            # model_class = self._model_class(**record_fields)
            self._model_class.update_from_dict(**record_fields)
            self._model_class.version += 1
            await self._model_class.save()
            return self._model_class
        except RepositoryError as e:
            raise RepositoryError(
                f"Failed UpdateRepository.update_record(): {e}"
            ) from e

type UpdateRepositoryT = UpdateRepository
