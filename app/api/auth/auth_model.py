from tortoise import fields, Model


class UserAuth(Model):
    name = fields.CharField(
        max_length=80,
        unique=True,
        description="The user_name for login."
    )
    password_hash = fields.CharField(
        max_length=255,
        description="The hashed password for the user."
    )

    def __str__(self) -> str:
        """
        Returns the string representation of the User object.

        Returns:
            str: The user_name of the user.
        """
        return self.name
