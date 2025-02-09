from pydantic import Field

from app.api.schemas.base_schema import (
    BaseSchema,
    DeletedSchema,
    InputSchema,
    OutputSchema,
)


class ContactSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Contact model using Pydantic.
    """

    phone_number: str = Field(
        max_length=120,
        description="Number of phone of contact",
    )
    email: str = Field(
        max_length=255,
        description="Information about contact",
    )
    website: str = Field(min_length=4, max_length=255)
    employee: int = None


class ContactInputSchema(ContactSchema, InputSchema):
    pass


class ContactOutputSchema(ContactSchema, OutputSchema):
   pass


class ContactDeletedSchema(DeletedSchema):
    pass
