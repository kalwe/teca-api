from pydantic import BaseModel, Field, EmailStr
from app.api.schemas.base_schema import BaseSchema
from app.common.responses.response_types import DataBodyType


class UserSchema(BaseSchema):
    """
    Schema for serializing and deserializing the User model using Pydantic.
    """
    id: int = Field(..., description="The unique identifier of the user", gt=0)
    username: str = Field(..., description="The username of the user",
                          min_length=3, max_length=100)
    email: EmailStr = Field(..., description="The email address of the user")
    password_hash: str = Field(...,
                               description="The hashed password of the user",
                               min_length=6)
    roles: list[str] = Field(default_factory=list,
                             description="List of roles assigned to the user")

    def get_fields(self) -> DataBodyType:
        """
        Returns the fields of the schema as a dictionary.
        """
        return self.model_dump()
