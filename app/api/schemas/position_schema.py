from pydantic import Field

from app.api.schemas.base_schema import BaseSchema, InputSchema, OutputSchema


class PositionSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Position model using Pydantic.
    """
    name: str = Field(
        ...,
        min_length=3,
        max_length=120,
        description="Name of position",
    )


class PositionInputSchema(PositionSchema, InputSchema):
   pass


class PositionOutputSchema(PositionSchema, OutputSchema):
   pass
