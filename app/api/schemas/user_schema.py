from pydantic import AliasGenerator, ConfigDict, EmailStr, Field, SecretStr

from app.api.schemas.base_schema import (
    DeletedSchema,
    InputSchema,
    OutputSchema,
)


class UserPasswordMixin:
    password_hash: SecretStr = Field(
        description="The hashed password of the user",
        min_length=6,
        max_length=255,
    )


class UserEmailMixin:
    email: EmailStr = Field(
        description="The email address of the user",
        max_length=255,
    )


class UserSchema(UserEmailMixin):
    """
    Schema for serializing and deserializing the User model using Pydantic.
    """
    name: str = Field(
        description="The name of the user",
        min_length=5,
        max_length=80,
    )
    # TODO: create List[Roles]
    roles: list[str] = None


class UserInputSchema(InputSchema, UserSchema, UserPasswordMixin):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field: {"password_hash": "password"}.get(
                field, field
            )
        ),
        by_alias=True,
    )


class UserOutputSchema(UserSchema, OutputSchema):
    pass


class UserDeletedSchema(DeletedSchema):
    pass
