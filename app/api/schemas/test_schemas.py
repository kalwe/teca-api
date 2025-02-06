from datetime import datetime

from pydantic import BaseModel, Field


class TimestampMixin:
    created_at: datetime = Field(
        description="Timestamp when the record was created.",
        default_factory=datetime.now,
    )
    updated_at: datetime = None


class SoftDeleteMixin:
    is_active: bool = Field(
        default=True, description="Indicates whether the record is active or not."
    )
    deleted_at: datetime = None


class BaseSchema(BaseModel, TimestampMixin, SoftDeleteMixin):
    version: int

    def dump(self, **kwargs):
        return self.model_dump(**kwargs)

    def validate(self, m):
        return self.model_validate(m)


exclude_keys = {
    "created_at": True,
    "updated_at": True,
    "deleted_at": True,
    "version": True,
}

data = {
    "name": "joehn",
    "email": "tes@email.com",
    "password": "senha123",
}


class In(BaseSchema):
    id: int


class User(In):
    name: str
    email: str
    password: str


user_in = User(
    id=1, version=1, name="joehn", email="este@gemail.com", password="senha123"
)

print(user_in.dump())
print(user_in.dump(exclude=exclude_keys))
