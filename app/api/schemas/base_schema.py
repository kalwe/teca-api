from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, ValidationError


class IdMandatoryMixin:
    id: int = Field(
        description="Primary key for the record.",
        gt=0,
    )


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


class UnionDatetimesMixins(TimestampMixin, SoftDeleteMixin):
    pass


class UnionIdMandatoryWithTimesMixin(IdMandatoryMixin, UnionDatetimesMixins):
    pass


class BaseSchema(BaseModel):
    """
    Base class for defining generic fields for models using Quart-Schema
    and Pydantic.
    """

    version: int = Field(default=1)

    def validate(self, model):
        """
        Validate a pydantic model instance.
        Ex:
            user_orm = UserOrm(id=123, name="John", password="pass123")
            user_validated = UserSchema().model_validate(user_orm)

            * user_validated is instance of UserSchema

        Return: The validated model instance.
        """
        try:
            return self.model_validate(model)
        except ValidationError as e:
            raise ValidationError(f"model_validate() e: {e}")

    def validate_json(self, json_data):
        """
        Validate the given JSON data against the Pydantic model.

        Args:
            model: str | bytes | bytearray

        Returns:
            The validated Pydantic model.
        """
        try:
            return self.model_validate_json(json_data)
        except ValidationError as e:
            raise ValidationError(f"model_validate_json() e: {e}")

    def dump(self, **kwargs) -> dict[str, Any]:
        """
        Serializes the model instance into a dictionary.

        Ex:
            user_data = UserFromRequest(id=123, name="John", password="pass123")
            u = UserSchema(user_data)
            u_dump = u.dump()
            UserOrm.create(u_dump)

        Return dict[str, Any]
        """
        try:
            return self.model_dump(**kwargs)
        except ValidationError as e:
            raise ValidationError(f"model_dump() e: {e}")

    def dump_json(self, **kwargs) -> str:
        try:
            return self.model_dump_json(**kwargs)
        except ValidationError as e:
            raise ValidationError(f"model_dump_json() e: {e}")


class InputSchema(BaseSchema):
    version: int = Field(default=1, exclude=True)


class OutputSchema(BaseSchema, UnionIdMandatoryWithTimesMixin):
    pass


class DeletedSchema(BaseSchema, IdMandatoryMixin, SoftDeleteMixin):
    pass


type SchemaT = BaseSchema
