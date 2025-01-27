from pydantic import BaseModel, Field

from app.api.schemas.user_schema import UserPasswordMixin


class UseAuthInputSchema(BaseModel, UserPasswordMixin):
    name: str = Field(
        ...,
        description="Username to login.",
        max_length=80,
    )


class UserAuthOutputLoginSchema(BaseModel):
    current_user_id: int
    name: str
    id_authenticated: bool
    token: str
