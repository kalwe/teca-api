from tortoise import fields


from app.core.models.employee_related import EmployeeRelated
from app.core.models.shared.base_model import BaseModel


class Contact(BaseModel, EmployeeRelated):
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
