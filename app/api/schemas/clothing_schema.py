from pydantic import Field

from app.api.schemas.base_schema import (
    BaseSchema,
    DeletedSchema,
    InputSchema,
    OutputSchema,
)


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
    employee: int = None


class ClothingInputSchema(ClothingSchema, InputSchema):
   pass


class ClothingOutputSchema(ClothingSchema, OutputSchema):
   pass


class ClothingDeletedSchema(DeletedSchema):
    pass
