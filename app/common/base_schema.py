from pydantic import BaseModel, Field

from app.common.responses.response_types import DataBodyType


class BaseSchema(BaseModel):
    """
    Base class for defining generic fields for models using Quart-Schema and Pydantic.
    """

    def get_fields(self) -> DataBodyType:
        """
        Each subclass should implement this method to define model-specific fields.
        """
        raise NotImplementedError(
            "Subclasses must implement get_fields method.")

    def dump(self) -> DataBodyType:
        """
        Serializes the model instance into a dictionary.
        """
        return self.model_dump()
