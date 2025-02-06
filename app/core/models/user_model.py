from tortoise import fields

from app.common.hash_utils import hash_provider
from app.core.models.shared.base_model import ModelBase


class EmailMixin:
    email = fields.CharField(
        max_length=255,
        unique=True,
        index=True,
        description="The unique email address of the user."
    )


class PasswordMixin:
    password_hash = fields.CharField(
        max_length=255,
        description="The hashed password for the user."
    )


class User(ModelBase, EmailMixin, PasswordMixin):
    """
    Represents a user in the system, who can have one or more roles.

    A user can have one or more roles, each granting different permissions.
    """
    name = fields.CharField(
        max_length=80,
        unique=True,
        description="The unique user name for the user."
    )
    # TODO: create enum
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
            str: The name of the user.
        """
        return self.name

    # def gen_hashed_password(schema: SchemaT):
    #     hash = hash_provider(self.password_hash)
    #     self.password_hash = hash
    #     return hash
