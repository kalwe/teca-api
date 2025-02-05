from typing import Optional

from app.core.models.shared.base_model import ModelT
from app.api.schemas.base_schema import SchemaT


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
        # for field_name, value in fields_data.items():
        #     setattr(self.model_class, field_name, value)
        try:
            # record.version += 1
            self._model_class.update_from_dict(**record_fields.dump())
            await self._model_class.save()
            return self._model_class
        except Exception as e:
            raise Exception(
                f"Failed UpdateRepository.update_record(): {e}") from e
