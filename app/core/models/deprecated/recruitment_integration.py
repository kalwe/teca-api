from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class RecruitmentIntegration(BaseModel):
    """
    Represents the integration settings for the recruitment system,
    such as API keys or URLs.
    """
    api_url = fields.CharField(
        max_length=255,
        description="API URL for recruitment system integration"
    )
    api_key = fields.CharField(
        max_length=255,
        description="API key for accessing the recruitment system"
    )

    def __str__(self):
        return f"Recruitment integration with API at {self.api_url}"
