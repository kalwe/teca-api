from tortoise import fields

from app.core.models.base_entity import BaseEntity

class PersonModel(BaseEntity):
    """
    Abstract model for person-related details.
    """
    full_name = fields.CharField(
        max_length=255,
        description="Full name of the person"
    )
    date_of_birth = fields.DateField(
        description="Date of birth of the person"
    )

    class Meta:
        abstract = True
