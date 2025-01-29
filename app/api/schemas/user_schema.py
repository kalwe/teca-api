from pydantic import Field, EmailStr, SecretStr
from app.api.schemas.base_schema import (
    InputBaseSchema, OutputBaseSchema, BaseSchema, SoftDeleteMixin)


class UserPasswordMixin:
    password_hash: SecretStr = Field(
        ...,
        description="The hashed password of the user",
        min_length=6,
        max_length=255,
    )


class UserEmailMixin:
    email: EmailStr = Field(
        ...,
        description="The email address of the user",
        max_length=255,
    )


class UserBaseSchema(BaseSchema):
    """
    Schema for serializing and deserializing the User model using Pydantic.
    """
    name: str = Field(
        ...,
        description="The name of the user",
        min_length=5,
        max_length=80,
    )

    # TODO: create List[Roles]
    roles: list[str] | None = Field(
        # default_factory=list,
        description="List of roles assigned to the user",
    )


class UserInputSchema(
    InputBaseSchema,
    UserBaseSchema,
    UserEmailMixin,
    UserPasswordMixin
):
    pass


class UserOutputSchema(
    UserBaseSchema,
    OutputBaseSchema,
    UserEmailMixin
):
    pass


class UserDeletedSchema(BaseSchema, SoftDeleteMixin):
    pass
