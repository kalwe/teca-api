from tortoise import fields

from app.core.models.shared.base_model import BaseModel
from app.core.models.shared.employee_related import EmployeeRelated


class Clothing(BaseModel, EmployeeRelated):
    """
    Model representing an clothing with details.
    """
    shirt_size = fields.CharField(
        max_length=80,
    )
    pants_size = fields.CharField(
        max_length=80,
    )
    shoe_size = fields.CharField(
        max_length=80,
    )
