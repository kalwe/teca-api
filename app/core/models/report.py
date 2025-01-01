from tortoise import fields

from app.core.models.base_entity import BaseEntity
from app.core.models.employee_related import EmployeeRelatedModel

class Report(EmployeeRelatedModel):
    """
    Represents a point report for an employee or a specific period.
    """
    start_date = fields.DateField()
    end_date = fields.DateField()
    total_hours = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0
    )  # Total hours worked in the period
    total_overtime = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0
    )  # Total overtime in the period
    total_adjustments = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0
    )  # Total adjustments made

    def __str__(self):
        return f"Report for {self.employee.full_name} from {self.start_date} to {self.end_date}"
