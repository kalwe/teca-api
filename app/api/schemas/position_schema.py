from pydantic import Field
from app.api.schemas.base_schema import BaseSchema, InputBaseSchema, OutputBaseSchema


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


class PositionInputSchema(PositionSchema, InputBaseSchema):
   pass

class PositionOutputSchema(PositionSchema, OutputBaseSchema):
   pass
