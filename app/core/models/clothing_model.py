from tortoise import fields
from app.core.models.shared.base_model import BaseModel


class Clothing(BaseModel):
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
