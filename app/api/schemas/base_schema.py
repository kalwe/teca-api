from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from app.common.responses.response_types import DataBodyType


class TimestampsMixin(BaseModel):
    created_at: datetime = Field(
        ...,
        description="Timestamp when the record was created."
    )
    updated_at: datetime = Field(
        ...,
        description="Timestamp when the record was last updated."
    )


class SoftDeleteMixin(BaseModel):
    is_active: bool = Field(
        default=True,
        description="Indicates whether the record is active or not."
    )
    deleted_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the record was soft-deleted."
    )


class BaseSchema(TimestampsMixin, SoftDeleteMixin):
    """
    Base class for defining generic fields for models using Quart-Schema and Pydantic.
    """
    id: int = Field(
        ...,
        description="Primary key for the record.",
        gt=0,
    )
    version: int = Field(
        default=1,
        description="Version of the record for optimistic concurrency."
    )

    # def get_fields(self) -> DataBodyType:
    #     """
    #     Each subclass should implement this method to define model-specific fields.
    #     """
    #     raise NotImplementedError(
    #         "Subclasses must implement get_fields method.")

    def dump(self) -> DataBodyType:
        """
        Serializes the model instance into a dictionary.
        """
        return self.model_dump()

    # Allows parsing from ORM instances
    model_config = ConfigDict(from_attributes=True)

    class Config:
        orm_mode = True  # Enable compatibility with ORM objects


class BaseInputSchema(BaseSchema):
    id: int | None = Field(
        ...,
        description="Primary key for the record.",
    )


class BaseOutputSchema(BaseSchema):
    pass
