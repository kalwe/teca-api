from tortoise import fields

from app.core.models.employee_model import Employee


class EmployeeRelated:
    """
    Abstract model for data related to an employee.
    """
    employee: fields.ForeignKeyRelation[Employee] = fields.ForeignKeyField(
        "models.Employee",
        related_name="%(class)s%",
        description="Reference to the associated employee"
    )

    class Meta:
        abstract = True
