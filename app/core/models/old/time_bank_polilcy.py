from tortoise import fields

from app.core.models.shared.base_entity import BaseEntity


class TimeBankPolicy(BaseEntity):
    """
    Represents the time bank policy, such as limits for using overtime
    or how compensations are calculated.
    """
    max_balance = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        description="Maximum balance in the time bank (in hours)"
    )
    allowed_usage_percentage = fields.FloatField(
        description="Percentage of time bank balance that can be used at once"
    )

    def __str__(self):
        return f"Max balance: {self.max_balance} hours, Allowed usage: {self.allowed_usage_percentage}%"
