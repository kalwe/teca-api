from tortoise import fields
from app.core.models.shared.base_entity import BaseEntity


class Clothing(BaseEntity):
    """
    Model representing an clothing with details.
    """
    shirt_size = fields.CharField(
        max_length=120,
    )
    pants_size = fields.CharField(
        max_length=120,
    )
    shoe_size = fields.CharField(
        max_length=120,
    )
