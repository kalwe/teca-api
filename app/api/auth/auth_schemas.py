from pydantic import BaseModel, Field

from app.api.schemas.user_schema import UserPasswordMixin


class UseAuthInputSchema(BaseModel, UserPasswordMixin):
    name: str = Field(
        min_length=5,
        max_length=80,
    )


class UserAuthOutputLoginSchema(BaseModel):
    current_user_id: int = Field()
    id_authenticated: bool = Field()
    token: str = Field()
