from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class PointAdjustmentHistory(EmployeeRelatedModel):
    """
    Represents the history of time adjustments made for an employee's point system.
    """
    reason = fields.CharField(
        max_length=255,
        description="Reason for the adjustment"
    )
    adjusted_hours = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0, description="Adjusted hours"
    )
    adjustment_timestamp = fields.DatetimeField(
        description="Timestamp of the adjustment"
    )

    def __str__(self) -> str:
        return (
            f"Adjustment for {self.employee.full_name} on "
            f"{self.adjustment_timestamp.strftime('%Y-%m-%d %H:%M:%S')} "
            f"(Reason: {self.reason})"
        )
