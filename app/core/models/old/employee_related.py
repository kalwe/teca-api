from tortoise import fields

from app.core.models.shared.base_entity import BaseEntity


class EmployeeRelatedModel(BaseEntity):
    """
    Abstract model for data related to an employee.
    """
    employee = fields.ForeignKeyField(
        "models.Employee",
        related_name="%(class)s_related",
        description="Reference to the associated employee"
    )

    class Meta:
        abstract = True
