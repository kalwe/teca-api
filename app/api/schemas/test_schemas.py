from datetime import datetime
from typing import Optional

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
    deleted_at: Optional[datetime] = None


class UnioMixins(TimestampMixin, SoftDeleteMixin):
    pass


class BaseSchema(BaseModel):
    version: Optional[int] = None

    def dump(self, **kwargs):
        return self.model_dump(**kwargs)

    def validate(self, m):
        return self.model_validate(m)


class In(BaseSchema):
    id: Optional[int] = None


class Out(BaseSchema, UnioMixins):
    id: int


class Passw:
    password: str


class User(BaseSchema):
    name: str
    email: str


class UserIn(User, Passw):
    pass


class UserOut(User, UnioMixins, Passw):
    pass


user_in = UserIn(name="joehn", email="este@gemail.com", password="senha123")
uin_d = user_in.dump()
print(uin_d)


user_out = UserOut(
    version=1, id=1, name="joehn", email="este@gemail.com", password="senha123"
)
uout_val = user_out.validate(user_out)
print(uout_val)


exclude_keys = {
    "created_at": True,
    "updated_at": True,
    "deleted_at": True,
    "version": True,
}

print(user_in.dump())
print(user_in.dump(exclude=exclude_keys))


class Op(BaseModel):
    opt: Optional[int]
    opt_or_none: Optional[int] = None
    str_eq_none: str = None
    default_none: str = Field(default=None)
    str_or_none_eq_none: str | None = None
    str_or_none: str | None


op = Op(opt=None, str_eq_none="t", default_none="teste", str_or_none_eq_none="te")


data = {
    "name": "joehn",
    "email": "tes@email.com",
    "password": "senha123",
}

##############
# class NotNullable:
#     def __get_pydantic_core_schema__(
#         self, source: Type[Any], handler: GetCoreSchemaHandler
#     ) -> core_schema.CoreSchema:
#         schema = handler(source)
#         assert schema["type"] == "nullable"
#         return schema["schema"]


# T = TypeVar("T")
# Omissible = Annotated[Optional[T], NotNullable()]


# class Testing(BaseModel):
#     omitted: Omissible[int] = None  # type hinting will work


# Testing.model_json_schema()
# => {"properties": {"omitted": {"default": null, "title": "Omitted", "type": "integer"}}, "title": "Testing", "type": "object"}


#####################
# T = TypeVar("T")

# def not_none(v: Optional[Any], info: ValidationInfo):
#     if v is None:
#         raise ValueError(f"{info.field_name} is not nullable")
# ​
#     return v

# Omissible = Annotated[Optional[T], BeforeValidator(not_none), Field(default=None)]

# class Testing(BaseModel):
#     omitted: Omissible[int]

# # no explicit None set, but it's value is None
# empty = Testing()
# empty.omitted # => None
# empty.model_dump_json(exclude_unset=True) # => {}

# try:
#     explicit = Testing(omitted=None)
# except ValidationError:
#     # Fails validation, because when omitted is explicitly set, it must be an int


########################
# class Model(base):
#     a: Optional[int]  # this field is required bit can be given None (to be CHANGED in v2)
#     b: Optional[int] = None  # field is not required, can be given None or an int (current behaviour)
#     c: int = None  # this field isn't required but must be an int if it is provided (current behaviour)


##############################################
# class ParentBase(BaseModel):
#     """Shared properties."""

#     name: str
#     email: str


# class ParentCreate(ParentBase):
#     """Properties to receive on item creation."""

#     # dont need id here if your db autocreates it
#     pass


# class ParentUpdate(ParentBase):
#     """Properties to receive on item update."""

#     # dont need id as you are likely PUTing to /parents/{id}
#     # other fields should not be optional in a PUT
#     # maybe what you are wanting is a PATCH schema?
#     pass


# class ParentInDBBase(ParentBase):
#     """Properties shared by models stored in DB - !exposed in create/update."""

#     # primary key exists in db, but not in base/create/update
#     id: int


# class Parent(ParentInDBBase):
#     """Properties to return to client."""

#     # optionally include things like relationships returned to consumer
#     # related_things: List[Thing]
#     pass


# class ParentInDB(ParentInDBBase):
#     """Additional properties stored in DB."""

#     # could be secure things like passwords?
#     pass
