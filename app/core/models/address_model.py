from tortoise import fields


from app.core.models.shared.base_model import BaseModel
from app.core.models.shared.employee_related import EmployeeRelated


class Address(BaseModel, EmployeeRelated):
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
