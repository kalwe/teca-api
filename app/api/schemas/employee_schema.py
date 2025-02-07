from datetime import date

from pydantic import Field

from app.api.schemas.address_schema import AddressSchema
from app.api.schemas.bank_account_schema import BankAccountSchema
from app.api.schemas.base_schema import (
    BaseSchema,
    InputSchema,
    OutputSchema,
)
from app.api.schemas.clothing_schema import ClothingSchema
from app.api.schemas.function_schema import FunctionSchema


class PersonSchema:
    full_name: str = Field(
        ...,
        description="The complete name of person",
        min_length=5,
        max_length=255,
    )
    tax_id: str = Field(
        ...,
        description="Tax identification number (CPF)",
        max_length=14,
    )
    national_id: str = Field(
        ...,
        max_length=20,
        description="National identification number (RG)",
    )
    date_of_birth: date = Field(description="Timestamp when the record was created.")
    issuing_body: str = Field(
        ...,
        max_length=120,
        description="Indicate issuing body from RG",
    )


class EmployeeSchema(BaseSchema, PersonSchema):
    """
    Schema for serializing and deserializing the Employee model using Pydantic.
    """

    name: str = Field(
        description="The first name of employee ",
        min_length=3,
        max_length=80,
    )
    registration: str = Field(
        max_length=4, description="Registration number of employee"
    )
    supervisor: bool = Field(
        default=False, description="Indicates if employee is a supervisor"
    )
    manager: bool = Field(
        default=False, description="Indicates if employee is a manager"
    )
    salary: int = Field(description="Salary of employee")
    contract_date: date = Field(description="Date when employee has contracted")
    function: FunctionSchema
    address: AddressSchema
    bank_account: BankAccountSchema
    clothing: ClothingSchema


class EmployeeInputSchema(InputSchema, EmployeeSchema):
    pass


class EmployeeOutputSchema(OutputSchema, EmployeeSchema):
    pass
