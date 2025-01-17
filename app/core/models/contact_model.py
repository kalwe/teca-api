from tortoise import fields


from app.core.models.shared.base_entity import BaseEntity


class Contact(BaseEntity):
    """
    Represents a contact information's
    """
    type = fields.CharField(
        max_length=120,
        description="Type of contact",
    )
    information = fields.CharField(
        max_length=255,
        description="Information about contact",
    )
