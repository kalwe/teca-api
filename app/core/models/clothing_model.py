from tortoise import fields

from app.core.models.employee_model import Employee
from app.core.models.shared.base_model import ModelBase
from app.core.models.shared.employee_related import EmployeeRelated
from app.core.models.shared.foreign_related import ForeignRelated


class Clothing(ModelBase, EmployeeRelated):
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
    employee: fields.ForeignKeyRelation[Employee] = (
        ForeignRelated.foreign_key('Employee', 'clothings'))
