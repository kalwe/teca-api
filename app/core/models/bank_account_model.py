from tortoise import fields
from app.core.models.shared.base_model import ModelBase
from app.core.models.shared.foreign_related import ForeignRelated

class BankAccount(ModelBase):
    """
    Model representing a bank account with details.
    """

    bank = fields.CharField(
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
    account_type = fields.CharField(
        max_length=120,
        description="Type of account",
    )
    employee = ForeignRelated.foreign_related("Employee", "bank")
