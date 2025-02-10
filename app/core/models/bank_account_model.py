from tortoise import fields
from tortoise.validators import Validator, ValidationError

from app.core.models.shared.base_model import ModelBase
from app.core.models.shared.foreign_related import ForeignRelated

# TODO: Move to an appropriate place
# TODO: Evaluate if validation in the schema (bank_account_schema) is better, because it occurs before database processing
class AccountTypeValidator(Validator):
    def __init__(self, valid_types):
        self.valid_types = [t.lower() for t in valid_types]

    def __call__(self, value):
        if not isinstance(value, str):
            raise ValidationError("Account type must be a string.")
        if not value:
            raise ValidationError("Account type cannot be empty.")
        if value.lower() not in self.valid_types:
            raise ValidationError(
                f"Invalid account type: {value}. "
                f"Valid types are: {', '.join(self.valid_types)}"
            )


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
        validators=[AccountTypeValidator(valid_types=["corrente", "poupança"])]
    )
    employee = ForeignRelated.foreign_related("Employee", "bank")
