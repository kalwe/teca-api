
from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class EmployeeReport(EmployeeRelatedModel):
    """
    Represents a time report for an employee within a specific period.
    """
    start_date = fields.DateField(
        description="Start date of the reporting period"
    )
    end_date = fields.DateField(
        description="End date of the reporting period"
    )
    total_worked_hours = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0
    )
    total_overtime_hours = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0
    )
    total_adjusted_hours = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0
    )

    def __str__(self) -> str:
        return
