from tortoise import fields

from app.core.models.shared.base_model import ModelBase
from app.core.models.shared.foreign_related import ForeignRelated


class Address(ModelBase):
    """
    Represents a address
    """
    street = fields.CharField(
        max_length=255,
        description="Name of street"
    )
    number = fields.CharField(
        max_length=8,
        description="Number of street"
    )
    neighborhood = fields.CharField(
        max_length=120,
        description="Name of neighborhood"
    )
    city = fields.CharField(
        max_length=255,
        description="Name of the city"
    )
    zip_code = fields.CharField(
        max_length=12,
        description="CEP of street"
    )
    state = fields.CharField(
        max_length=60,
        description="Name of state"
    )
    employee = ForeignRelated.foreign_related('Employee', 'address')
