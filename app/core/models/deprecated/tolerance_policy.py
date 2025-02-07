from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class TolerancePolicy(BaseModel):
    """
    Represents the tolerance policy for delays and compensations.
    """
    max_delay = fields.IntField(
        description="Maximum allowed delay in minutes"
    )
    compensation_allowed = fields.BooleanField(
        default=True,
        description="Whether delay can be compensated"
    )

    def __str__(self):
        return f"Max delay: {self.max_delay} minutes, Compensation allowed: {self.compensation_allowed}"
