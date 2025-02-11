from tortoise import Model, fields

from app.core.models.shared.base_model import ModelBase


class EmailMixin:
    email = fields.CharField(
        max_length=255,
        unique=True,
        index=True,
        description="The unique email address of the user.",
    )


class PasswordMixin:
    password_hash = fields.CharField(
        max_length=255, description="The hashed password for the user."
    )


class User(ModelBase, EmailMixin, PasswordMixin):
    """
    Represents a user in the system, who can have one or more roles.

    A user can have one or more roles, each granting different permissions.
    """

    name = fields.CharField(
        max_length=80, unique=True, description="The unique user name for the user."
    )
    # TODO: create enum
    roles = fields.ManyToManyField(
        "models.Role",
        related_name="users",
        # through="user_roles",
        description="The roles assigned to the user.",
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


class Node(Model):
    name = fields.CharField(max_length=255)


class O2oPkModelWithM2m(Model):
    user: fields.OneToOneRelation[User] = fields.OneToOneField(
        "models.User",
        on_delete=fields.CASCADE,
        primary_key=True,
    )
    nodes: fields.ManyToManyRelation["Node"] = fields.ManyToManyField("models.Node")

    async def test_o2o_fk_model_with_m2m_field(self):
        user = await User.create(name="John")
        obj = await O2oPkModelWithM2m.create(user=user)
        node = await Node.create(name="can_edit_employee")  # role.name
        await obj.nodes.add(node)


############################
class M2mWithO2oPk(Model):
    name = fields.CharField(max_length=64)
    address: fields.ManyToManyRelation["Address"] = fields.ManyToManyField(
        "models.Address"
    )

    async def test_many2many_field_with_o2o_fk(self):
        role = await Role.create(name="can_edit_employee")
        event = await User.create(name="e", role=role)
        address = await Address.create(city="c", street="s", event=event)
        obj = await M2mWithO2oPk.create(name="m")
        self.assertEqual(await obj.address.all(), [])
        await obj.address.add(address)
        self.assertEqual(await obj.address.all(), [address])
