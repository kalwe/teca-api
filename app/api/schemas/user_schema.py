from pydantic import AliasGenerator, ConfigDict, EmailStr, Field, SecretStr

from app.api.schemas.base_schema import (
    BaseSchema,
    InputBaseSchema,
    OutputBaseSchema,
    SoftDeleteMixin,
)


class UserPasswordMixin:
    password: SecretStr = Field(
        description="The hashed password of the user",
        min_length=6,
        max_length=255,
    )


class UserEmailMixin:
    email: EmailStr = Field(
        description="The email address of the user",
        max_length=255,
    )


class UserBaseSchema():
    """
    Schema for serializing and deserializing the User model using Pydantic.
    """
    name: str = Field(
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
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=lambda field: {"password": "password_hash"}.get(
                field, field
            )
        ),
        by_alias=True,
    )


class UserOutputSchema(
    UserBaseSchema,
    OutputBaseSchema,
    UserEmailMixin
):
    pass


# TODO: create generic DeletedSchema
class UserDeletedSchema(BaseSchema, SoftDeleteMixin):
    pass
