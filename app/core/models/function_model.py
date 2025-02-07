from tortoise import fields

from app.core.models.shared.base_model import ModelBase


class Function(ModelBase):
    """
    Represents a function of the employee

    """
    name = fields.CharField(
        max_length=120,
        unique=True,
        description="Name of function",
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the Role object.

        Returns:
            str: The name of the role.
        """
        return self.name
