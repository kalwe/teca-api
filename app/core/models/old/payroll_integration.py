from tortoise import fields

from app.core.models.shared.base_model import BaseModel

# TODO: verify if this class is necessary


class PayrollIntegration(BaseModel):
    """
    Represents the integration settings for the payroll system,
    such as API keys or URLs.
    """
    api_url = fields.CharField(
        max_length=255,
        description="API URL for payroll system integration"
    )
    api_key = fields.CharField(
        max_length=255,
        description="API key for accessing the payroll system"
    )

    def __str__(self):
        return f"Payroll integration with API at {self.api_url}"
