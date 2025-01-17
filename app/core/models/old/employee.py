from tortoise import fields

from app.core.models.person_model import PersonModel


class Employee(PersonModel):
    """
    Model representing an employee with personal details.
    """
    tax_id = fields.CharField(
        max_length=14,
        unique=True,
        description="Tax identification number (CPF)")
    national_id = fields.CharField(
        max_length=20,
        unique=True,
        description="National identification number (RG)")

    def __str__(self):
        return self.full_name
