from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel
from app.core.models.enums import EmploymentStatus

class EmployeeStatus(EmployeeRelatedModel):
    """
    Model to manage the current status of an employee.
    """
    current_status = fields.CharEnumField(
        EmploymentStatus,
        description="Current employment status"
    )

    def __str__(self):
        return f"Status of {self.employee.full_name}: {self.current_status.value}"
