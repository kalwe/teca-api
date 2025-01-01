from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class ActiveEmployee(EmployeeRelatedModel):
    """
    Model to represent active employees, encapsulating their active status.
    """
    contract_expiry_date = fields.DateField(null=True, description="Contract expiry date for the employee")
    is_currently_active = fields.BooleanField(
        default=True,
        description="Indicates if the employee is currently active or not"
    )

    def __str__(self):
        return f"{self.employee.full_name} is {'active' if self.is_currently_active else 'inactive'}"
