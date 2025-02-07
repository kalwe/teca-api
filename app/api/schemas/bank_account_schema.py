from pydantic import Field

from app.api.schemas.base_schema import BaseSchema, InputSchema, OutputSchema


class BankAccountSchema(BaseSchema):
    """
    Schema for serializing and deserializing the BankAccount model
    using Pydantic.
    """
    bank: str = Field(
        max_length=120,
        description="Name of bank"
    )
    agency: str = Field(
        max_length=120,
        description="Number of agency"
    )
    account: str = Field(
        max_length=120,
        description="Number of account"
    )
    # TODO: validate this field
    account_type: str = Field(
        max_length=120,
        description="Type of account"
    )



class BankAccountInputSchema(BankAccountSchema, InputSchema):
   pass

class BankAccountOutputSchema(BankAccountSchema, OutputSchema):
   pass
