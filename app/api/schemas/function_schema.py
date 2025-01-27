from pydantic import Field
from app.api.schemas.base_schema import BaseSchema


class FunctionSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Function model using Pydantic.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=120,
        description="Name of function",
    )
