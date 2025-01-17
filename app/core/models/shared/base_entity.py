from tortoise import fields, Model
from datetime import datetime
from typing import Type, TypeVar

T = TypeVar("T", bound="BaseEntity")


class BaseEntity(Model):
    """
    Abstract base model containing common fields and utility methods
    for other models.
    All models should inherit from this class to share the same
    base functionality.
    """
    id = fields.IntField(
        pk=True,
        description="Primary key for the record.",
    )
    created_at = fields.DatetimeField(
        auto_now_add=True,
        description="Timestamp when the record was created.",
    )
    updated_at = fields.DatetimeField(
        auto_now=True,
        description="Timestamp when the record was last updated.",
    )
    is_active = fields.BooleanField(
        default=True,
        description="Indicates whether the record is active or not.",
    )
    deleted_at = fields.DatetimeField(
        null=True,
        description="Timestamp when the record was soft-deleted.",
    )
    version = fields.IntField(
        default=1,
        description="Version of the record for optimistic concurrency.",
    )

    class Meta:
        abstract = True

    async def deactivate_record(self: T) -> T:
        """
        Soft deletes the record by setting 'is_active' to False and recording the deletion time.

        Args:
            self (T): The instance of the model.

        Returns:
            T: The instance of the model after deactivation.
        """
        self.is_active = False
        self.deleted_at = datetime.now()
        await self.save()
        return self

    async def restore_record(self: T) -> T:
        """
        Restores a soft-deleted record by setting 'is_active' to True and
        clearing 'deleted_at'.

        Args:
            self (T): The instance of the model.

        Returns:
            T: The instance of the model after restoration.
        """
        self.is_active = True
        self.deleted_at = None
        await self.save()
        return self

    def __str__(self: T) -> str:
        """
        String representation of the object.

        Returns:
            str: A string representation of the object, including its ID
            and active status.
        """
        return f"ID: {self.id}, Active: {self.is_active}"

    @classmethod
    async def get_active_records(cls: Type[T]) -> Type[T]:
        """
        Retrieves all active records of the model.

        Args:
            cls (Type[T]): The class of the model.

        Returns:
            Type[T]: A queryset of all active records.
        """
        return await cls.filter(is_active=True)

    @classmethod
    async def get_deleted_records(cls: Type[T]) -> Type[T]:
        """
        Retrieves all soft-deleted records of the model.

        Args:
            cls (Type[T]): The class of the model.

        Returns:
            Type[T]: A queryset of all soft-deleted records.
        """
        return await cls.filter(is_active=False)

    @classmethod
    async def soft_delete_record(cls: Type[T], record_id: int) -> Type[T]:
        """
        Soft deletes a record by its ID.

        Args:
            cls (Type[T]): The class of the model.
            record_id (int): The ID of the record to be soft deleted.

        Returns:
            Type[T]: The soft-deleted record.
        """
        record = await cls.get(id=record_id)
        await record.deactivate_record()
        return record
