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


# Example subclass using the BaseSchema
class ExampleSchema(BaseSchema):
    """
    Example schema to define fields.
    """
    id: int = Field(..., description="The unique identifier of the object", gt=0)
    name: str = Field(..., description="The name of the object", min_length=1)
    age: int = Field(..., description="Age of the object", ge=0)

    def get_fields(self) -> DataBodyType:
        """
        Returns the fields of the schema as a dictionary.
        """
        return self.model_dump()
