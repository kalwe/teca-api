from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, ConfigDict, Field



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

    id: int = Field(
        ...,
        description="Primary key for the record.",
        gt=0,
    )
    version: int = Field(
        default=1,
        description="Version of the record for optimistic concurrency."
    )

    def validate(self, model):
        return self.model_validate(model)

    def validate_json(self, model):
        """
        Validate the given JSON data against the Pydantic model.

        Args:
            model: str | bytes | bytearray

        Returns:
            The validated Pydantic model.
        """
        return self.model_validate_json(model)

    def dump(self) -> dict[str, Any]:
        """
        Serializes the model instance into a dictionary.
        """
        return self.model_dump()

    def dump_json(self) -> str:
        return self.model_dump_json()


# TODO: remove TimestampsMixin, SoftDeleteMixin from InputBaseSchema
class InputBaseSchema(BaseSchema):
    id: Optional[int] = Field(
        description="Primary key for the record.",
    )


class OutputBaseSchema(BaseSchema):
    model_config = ConfigDict(
        from_attributes=True
    )


type SchemaT = BaseSchema
