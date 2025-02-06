from pydantic import Field
from app.api.schemas.base_schema import BaseSchema, InputBaseSchema, OutputBaseSchema


class RegionSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Region model using Pydantic.
    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=120,
        description="Name of region",
    )


class RegionInputSchema(RegionSchema, InputBaseSchema):
   pass

class RegionOutputSchema(RegionSchema, OutputBaseSchema):
   pass
