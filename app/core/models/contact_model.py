from tortoise import fields


from app.core.models.employee_model import Employee
from app.core.models.shared.base_model import ModelBase
from app.core.models.shared.employee_related import EmployeeRelated
from app.core.models.shared.foreign_related import ForeignRelated


class Contact(ModelBase):
    """
    Represents a contact information's
    """
    phone_number = fields.CharField(
        max_length=120,
        description="Number of phone of contact",
    )
    email = fields.CharField(
        max_length=255,
        description="Information about contact",
    )
    website = fields.CharField(max_length=255)
    employee: fields.ForeignKeyRelation[Employee] = (
        ForeignRelated.foreign_key('Employee', 'contacts'))
