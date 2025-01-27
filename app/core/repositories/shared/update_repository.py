from typing import Generic, Type, Optional, TypeVar

from app.core.models.shared.base_model import BaseModel


class UpdateRepository[T: BaseModel]:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: T):
        self.model_class = model_class

    async def update_record(self) -> Optional[T]:
        """
        Update fields for an existing record and increment its version.
        """
        # for field_name, value in fields_data.items():
        #     setattr(self.model_class, field_name, value)
        self.model_class.version += 1
        try:

            await self.model_class.update_or_create()
            # await self.model_class.save()
            return self.model_class
        except Exception as e:
            raise Exception(
                f"Failed UpdateRepository.update_record(): {e}") from e
