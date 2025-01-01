from tortoise import fields

from app.core.models.base_entity import BaseEntity

class ManualAdjustment(BaseEntity):
    """
    Represents a manual adjustment made by a manager on an employee's hours.
    """
    employee = fields.ForeignKeyField(
        "models.Employee",
        related_name="manual_adjustments"
    )
    adjusted_hours = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        description="Manually adjusted hours"
    )
    reason = fields.TextField(description="Justification for the adjustment")
    manager = fields.CharField(
        max_length=255,
        description="Manager responsible for the adjustment"
    )

    def __str__(self) -> str:
        return f"Manual Adjustment for {self.employee.full_name} ({self.adjusted_hours} hours) by {self.manager}"
