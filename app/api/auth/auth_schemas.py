from pydantic import BaseModel, Field

from app.api.schemas.user_schema import UserPasswordMixin


class UseAuthInputSchema(BaseModel, UserPasswordMixin):
    name: str = Field(
        min_length=5,
        max_length=80,
    )


class UserAuthOutputSchema(BaseModel):
    current_user_id: int = Field()
    name: str
    is_authenticated: bool = Field()
    token: str = Field()
