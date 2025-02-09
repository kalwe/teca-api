from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in the system, who can have one or more roles.

    A user can have one or more roles, each granting different permissions.
    """
    username = fields.CharField(
        max_length=80,
        unique=True,
        description="The unique username for the user."
    )
    email = fields.CharField(
        max_length=255,
        unique=True,
        description="The unique email address of the user."
    )
    password_hash = fields.CharField(
        max_length=255,
        description="The hashed password for the user."
    )
    roles = fields.ManyToManyField(
        "models.Role",
        related_name="users",
        through="user_roles",
        description="The roles assigned to the user."
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the User object.

        Returns:
            str: The username of the user.
        """
        return self.username
