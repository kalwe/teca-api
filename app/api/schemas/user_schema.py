from pydantic import Field, EmailStr
from app.api.schemas.base_schema import (BaseInputSchema,
                                         BaseOutputSchema, BaseSchema)
from app.common.responses.response_types import DataBodyType


class UserBaseSchema(BaseSchema):
    """
    Schema for serializing and deserializing the User model using Pydantic.
    """

    username: str = Field(
        ...,
        description="The username of the user",
        min_length=5,
        max_length=80,
    )
    email: EmailStr = Field(
        ...,
        description="The email address of the user",
        max_length=255,
    )
    roles: list[str] = Field(
        default_factory=list,
        description="List of roles assigned to the user",
    )

    def get_fields(self) -> DataBodyType:
        """
        Returns the fields of the schema as a dictionary.
        """
        return self.dump()


class UserInputSchema(UserBaseSchema, BaseInputSchema):
    password_hash: str = Field(
        ...,
        description="The hashed password of the user",
        min_length=6,
    )


class UserOutputSchema(UserBaseSchema, BaseOutputSchema):
    pass
