from tortoise import fields

from app.core.models.shared.base_model import ModelBase


class Reminder(ModelBase):
    """
    Represents a reminder information's
    """

    date_time = fields.CharField(
        max_length=32,
        description="Number of phone of contact",
    )
    title = fields.CharField(
        max_length=255,
        description="Information about contact",
    )
    description = fields.TextField()
