from pydantic import BaseModel, EmailStr, Field, SecretStr

from app.api.schemas.user_schema import UserBaseSchema, UserPasswordSchema


class UserLoginSchema(BaseModel, UserPasswordSchema):
    email: EmailStr = Field(
        ...,
        description="Email as username to login.",
        max_length=255,
    )


class RegisterSchema(UserBaseSchema, UserPasswordSchema):
