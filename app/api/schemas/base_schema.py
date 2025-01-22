from datetime import datetime
from typing import Any, Optional, Self
from pydantic import BaseModel, ConfigDict, Field

from app.common.datetime_utils import aware_utcnow
from app.common.responses.response_types import DictType


class TimestampsMixin():
    created_at: datetime = Field(
        ...,
        description="Timestamp when the record was created.",
        # default_factory=aware_utcnow()
    )
    updated_at: datetime = Field(
        ...,
        description="Timestamp when the record was last updated."
    )


class SoftDeleteMixin():
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
    id: int = Field(
        ...,
        description="Primary key for the record.",
        # gt=0,
    )
    version: int = Field(
        default=1,
        description="Version of the record for optimistic concurrency."
    )

    def validate_json(self, json):
        return self.model_validate_json(json)

    def validate(self, model: Any) -> Self:
        return self.model_validate(model)

    def dump(self) -> DictType:
        """
        Serializes the model instance into a dictionary.
        """
        return self.model_dump()

    def dump_json(self) -> str:
        return self.model_dump_json()

    # Allows parsing from ORM instances
    model_config = ConfigDict(from_attributes=True)


class BaseInputSchema(BaseSchema):
    id: Optional[int] = Field(
        ...,
        description="Primary key for the record.",
    )


class BaseOutputSchema(BaseSchema):
    pass
