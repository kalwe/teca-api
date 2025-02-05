from tortoise import fields

from app.core.enums.gender_enum import Gender
from app.core.enums.marital_status_enum import MaritalStatus


class PersonAbs:
    """
    Abstract model for person-related details.
    """
    full_name = fields.CharField(
        max_length=255,
        description="Full name of the person"
    )
    tax_id = fields.CharField(
        max_length=14,
        unique=True,
        description="Tax identification number (CPF)",
    )
    national_id = fields.CharField(
        max_length=20,
        unique=True,
        description="National identification number (RG)",
    )
    date_of_birth = fields.DateField(
        description="Date of birth of the person",
    )
    # Orgao Emissor
    issuing_body = fields.CharField(
        max_length=120,
        description="Indicate issuing body from RG",
    )
    gender: Gender = fields.CharEnumField(
        Gender,
        description="Gender male or female",
    )
    marital_status: MaritalStatus = fields.CharEnumField(
        MaritalStatus,
        description="Current marital status of person",
    )

    class Meta:
        abstract = True
