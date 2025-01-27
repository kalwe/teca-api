from tortoise import fields, Model
from typing import Optional, Self

from app.common.datetime_utils import aware_utcnow


class BaseModel(Model):
    """
    Abstract base model containing common fields and utility methods
    for other models.
    All models should inherit from this class to share the same
    base functionality.
    """

    id: Optional[int] = fields.IntField(
        pk=True,
        description="Primary key for the record.",
    )
    created_at = fields.DatetimeField(
        null=True,
        auto_now_add=True,
        description="Timestamp when the record was created."
    )
    updated_at = fields.DatetimeField(
        null=True,
        auto_now=True,
        description="Timestamp when the record was last updated."
    )
    is_active = fields.BooleanField(
        default=True,
        description="Indicates whether the record is active or not."
    )
    deleted_at = fields.DatetimeField(
        null=True,
        description="Timestamp when the record was soft-deleted."
    )
    version = fields.IntField(
        default=1,
        description="Version of the record for optimistic concurrency."
    )

    class Meta:
        abstract = True

    def deactivate_record(self: Self):
        """
        Setting 'is_active' to False.

        Args:
            self (Self): The instance of the model.
        """
        self.is_active = False
        self.deleted_at = aware_utcnow()

    async def restore_record(self: Self):
        """
        Setting 'is_active' to True and
        clearing 'deleted_at'.

        Args:
            self (Self): The instance of the model.
        """
        self.is_active = True
        self.deleted_at = None

    def __str__(self: Self) -> str:
        """
        String representation of the object.

        Returns:
            str: A string representation of the object, including its ID
            and active status.
        """
        return f"ID: {self.id}, Active: {self.is_active}"

    @classmethod
    async def get_active_records(cls: Self) -> Self:
        """
        Retrieves all active records of the model.

        Args:
            cls (Self): The class of the model.

        Returns:
            Self: A queryset of all active records.
        """
        return await cls.filter(is_active=True)

    @classmethod
    async def get_deleted_records(cls: Self) -> Self:
        """
        Retrieves all soft-deleted records of the model.

        Args:
            cls (Self): The class of the model.

        Returns:
            Self: A queryset of all soft-deleted records.
        """
        return await cls.filter(is_active=False)
