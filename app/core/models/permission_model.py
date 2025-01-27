from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class Permission(BaseModel):
    """
    Represents a permission in the system
    (e.g., 'can_edit_employee', 'can_view_reports').

    Permissions define the actions that can be performed within the system.
    """
    name = fields.CharField(
        max_length=120,
        unique=True,
        description="The unique name of the permission."
    )
    description = fields.TextField(
        description="A detailed description of what the permission allows."
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the Permission object.

        Returns:
            str: The name of the permission.
        """
        return self.name
