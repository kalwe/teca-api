from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class BankAccount(BaseModel):
    """
    Model representing an bank account with details.
    """
    name = fields.CharField(
        max_length=120,
        description="Name of bank",
    )
    agency = fields.CharField(
        max_length=120,
        description="Number of agency",
    )
    account = fields.CharField(
        max_length=120,
        description="Number of account",
    )
    # TODO: validate this field
    account_type = fields.CharField(
        max_length=120,
        description="Type of account",
    )
