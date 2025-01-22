from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class Role(BaseModel):
    """
    Represents a role in the system, grouping a set of permissions
    (e.g., 'Admin', 'Manager').

    A role defines a collection of permissions that a user can have.
    """
    name = fields.CharField(
        max_length=100,
        unique=True,
        description="The unique name of the role."
    )
    permissions = fields.ManyToManyField(
        "models.Permission",
        related_name="roles",
        through="role_permissions",
        description="The permissions associated with the role."
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the Role object.

        Returns:
            str: The name of the role.
        """
        return self.name
