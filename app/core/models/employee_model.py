from tortoise import fields

from app.core.models.address_model import Address
from app.core.models.bank_account_model import BankAccount
from app.core.models.clothing_model import Clothing
from app.core.models.contact_model import Contact
from app.core.models.shared.foreign_related import ForeignRelated
from app.core.models.shared.person_abstract import PersonAbs
from app.core.models.function_model import Function
from app.core.models.shared.base_model import ModelBase


class Employee(ModelBase, PersonAbs):
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
    admission_date = fields.DateField(
        description="Date when employee has contracted"
    )
    removal_date = fields.DateField(
        null=True,
        description="Date when employee has fired"
    )
    function: fields.ForeignKeyRelation[Function] = (
        ForeignRelated.foreign_key('Function', 'function')
    )
    address: fields.ReverseRelation["Address"]
    contacts: fields.ReverseRelation["Contact"]
    bank: fields.ReverseRelation["BankAccount"]
    clothings: fields.ReverseRelation["Clothing"]

    def __str__(self):
        self.__
        return self.full_name

    def as_supervisor(self):
        self.supervisor = True

    def as_manager(self):
        self.manager = True

    def revoke_supervisor(self):
        self.supervisor = False

    def revoke_manager(self):
        self.manager = False
