from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field, ValidationError, ValidationInfo



class TimestampsMixin:
    created_at: datetime = Field(
        description="Timestamp when the record was created.",
        # default_factory=aware_utcnow()
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the record was last updated."
    )


class SoftDeleteMixin:
    is_active: bool = Field(
        default=True,
        description="Indicates whether the record is active or not."
    )
    deleted_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the record was soft-deleted."
    )


class BaseSchema(BaseModel, TimestampsMixin, SoftDeleteMixin):
    """
    Base class for defining generic fields for models using Quart-Schema
    and Pydantic.
    """
    # Allows parsing from ORM instances
    # model_config = ConfigDict(from_attributes=True)
    version: int = Field(
        default=1,
        description="Version of the record for optimistic concurrency."
    )

    def validate(self, model):
        try:
            return self.model_validate(model)
        except ValidationError as e:
            raise ValidationError(f"model_validate() e: {e}") from e

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
            raise ValidationError(f"model_validate_json() e: {e}") from e

    def dump(self, by_alias: bool = False) -> dict[str, Any]:
        """
        Serializes the model instance into a dictionary.
        """
        try:
            return self.model_dump(by_alias=by_alias)
        except ValidationError as e:
            raise ValidationError(f"model_dump() e: {e}") from e

    def dump_json(self, by_alias: bool = False) -> str:
        try:
            return self.model_dump_json(by_alias=by_alias)
        except ValidationError as e:
            raise ValidationError(f"model_dump_json() e: {e}") from e


# TODO: remove TimestampsMixin, SoftDeleteMixin from InputBaseSchema
class InputBaseSchema(BaseSchema):
    id: int = Field()


class OutputBaseSchema(BaseSchema):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int = Field(
        description="Primary key for the record.",
        gt=0,
    )
    id: int = Field(
        description="Primary key for the record.",
    )

type SchemaT = BaseSchema
