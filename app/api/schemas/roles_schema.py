from pydantic import Field

from app.api.schemas.base_schema import (
    BaseSchema,
    DeletedSchema,
    InputSchema,
    OutputSchema,
)


class RolesSchema(BaseSchema):
    """
    Schema for serializing and deserializing the Roles model using Pydantic.
    """

    name: str = Field()
    description: str = None

class RolesInputSchema(RolesSchema, InputSchema):
   pass


class RolesOutputSchema(RolesSchema, OutputSchema):
   pass


class RolesDeletedSchema(DeletedSchema):
    pass
