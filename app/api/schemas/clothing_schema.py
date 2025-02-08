from pydantic import Field

from app.api.schemas.base_schema import BaseSchema, InputSchema, OutputSchema


class ClothingSchema(BaseSchema):
    """
    Schema for serializing and deserializing the
    Clothing model using Pydantic.
    """
    shirt_size: str = Field(
        max_length=80,
    )
    pants_size: str = Field(
        max_length=80,
    )
    shoe_size: str = Field(
        max_length=80,
    )


class ClothingInputSchema(ClothingSchema, InputSchema):
   pass


class ClothingOutputSchema(ClothingSchema, OutputSchema):
   pass
