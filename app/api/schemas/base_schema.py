from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, ValidationError


class TimestampsMixin:
    created_at: datetime = Field(
        description="Timestamp when the record was created.",
        default_factory=datetime.now,
    )
    updated_at: datetime = None


class SoftDeleteMixin:
    is_active: bool = Field(
        default=True,
        description="Indicates whether the record is active or not."
    )
    deleted_at: datetime = None


class BaseSchema(BaseModel, TimestampsMixin, SoftDeleteMixin):
    """
    Base class for defining generic fields for models using Quart-Schema
    and Pydantic.
    """

    version: int

    def validate(self, model):
        try:
            return self.model_validate(model)
        except ValidationError as e:
            raise ValidationError(f"model_validate() e: {e}")

    def validate_json(self, model):
        """
        Validate the given JSON data against the Pydantic model.

        Args:
            model: str | bytes | bytearray

        Returns:
            The validated Pydantic model.
        """
        try:
            return self.model_validate_json(model)
        except ValidationError as e:
            raise ValidationError(f"model_validate_json() e: {e}")

    def dump_clean(self, exclude_fields: dict[str, Any]) -> dict[str, Any]:
        # exclude unnecessary fields for input request
        default_exclude = {
            "created_at": True,
            "updated_at": True,
            "deleted_at": True,
            "version": True,
        }

        if not exclude_fields:
            exclude_fields = default_exclude
        self.dump(exclude=exclude_fields)

    def dump(self, **kwargs) -> dict[str, Any]:
        """
        Serializes the model instance into a dictionary.
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


class InputBaseSchema(BaseSchema):
    id: int = None


class OutputBaseSchema(BaseSchema):
    id: int = Field(
        description="Primary key for the record.",
        gt=0,
    )

type SchemaT = BaseSchema
