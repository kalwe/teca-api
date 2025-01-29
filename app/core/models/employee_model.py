from tortoise import fields

from app.core.models.address_model import Address
from app.core.models.bank_account_model import BankAccount
from app.core.models.clothing_model import Clothing
from app.core.models.contact_model import Contact
from app.core.models.person_model import Person
from app.core.models.function_model import Function
from app.core.models.shared.base_model import BaseModel


class Employee(BaseModel, Person):
    """
    Model representing an employee with personal details.
    """

    name = fields.CharField(
        max_length=80,
        description="First name of employee"
    )
    registration = fields.CharField(
        max_length=4,
        description="Registration number of employee"
    )
    supervisor = fields.BooleanField(
        default=False,
        description="Indicates if employee is a supervisor"
    )
    manager = fields.BooleanField(
        default=False,
        description="Indicates if employee is a manager"
    )
    salary = fields.IntField(
        description="Salary of employee"
    )
    contract_date = fields.DateField(
        description="Date when employee has contracted"
    )
    function: fields.ForeignKeyRelation[Function] = fields.ForeignKeyField(
        "models.Function",
        related_name="function"
    )
    address: fields.ReverseRelation["Address"]
    contact: fields.ReverseRelation["Contact"]
    bank: fields.ReverseRelation["BankAccount"]
    clothing: fields.ReverseRelation["Clothing"]

    def __str__(self):
        return self.full_name

    def as_supervisor(self):
        self.supervisor = True

    def as_manager(self):
        self.manager = True
