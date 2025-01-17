from tortoise import fields

from app.core.models.person_model import PersonModel


class Employee(PersonModel):
    """
    Model representing an employee with personal details.
    """
    role = fields.ForeignKeyField(
        "model.Role",
        related_name="employees"
    )
    registration = fields.CharField(
        max_length=255,
        description="Registration number of employee"
    )
    supervisor = fields.BooleanField(
        default=False,
        description="Indicates if employee is a supervisor"
    )
    manager = fields.BooleanField(
        default=False,
        description="Indicates if employee is a manager"
    )

    def __str__(self):
        return self.full_name
