from typing import Any, Self

from pydantic import BaseModel

from app.common.responses.response_types import DictType


class CommonSchema(BaseModel):
    """
    Base class for defining generic methods for models using Pydantic.
    """

    # def get_fields(self) -> DictType:
    #     """
    #     Each subclass should implement this method to define model-specific fields.
    #     """
    #     raise NotImplementedError(
    #         "Subclasses must implement get_fields method.")

    def validate(self, model: Any) -> Self:
        return self.model_validate(model)

    def dump(self) -> DictType:
        """
        Serializes the model instance into a dictionary.
        """
        return self.model_dump()

    def dum_json(self) -> str:
        return self.model_dump_json()
