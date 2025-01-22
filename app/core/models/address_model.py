from tortoise import fields


from app.core.models.shared.base_model import BaseModel


class Address(BaseModel):
    """
    Represents a address
    """
    street = fields.CharField(
        max_length=255,
        description="Name of street",
    )
    neighborhood = fields.CharField(
        max_length=120,
        description="Name of neighborhood",
    )
    zip_code = fields.CharField(
        max_length=12,
        description="CEP of street"
    )
    state = fields.CharField(
        max_length=60,
        description="Name of state",
    )
    municipality = fields.CharFields(
        max_length=60,
        description="Name of municipality",
    )
