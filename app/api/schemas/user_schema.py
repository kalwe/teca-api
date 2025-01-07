from marshmallow import fields, validate
from app.api.schemas.base_schema import BaseSchema
# from app.core.models.user import User

# class UserSchema(BaseSchema):
#     """
#     Schema for serializing and deserializing the User model.
#     """
#     id = fields.Int(dump_only=True)  # The primary key, auto-generated by the database
#     username = fields.Str(
#         required=True,
#         validate=validate.Length(min=3, max=100),
#         description="The unique username for the user."
#     )
#     email = fields.Str(
#         required=True,
#         validate=validate.Email(),
#         description="The unique email address of the user."
#     )
#     password_hash = fields.Str(
#         load_only=True,  # This field will not be included in the output serialization
#         required=True,
#         validate=validate.Length(min=6),
#         description="The hashed password for the user."
#     )
#     roles = fields.List(
#         fields.Str(),
#         description="The roles assigned to the user."
#     )

#     class Meta:
#         # This ensures that the fields are serialized in the correct order
#         fields = ("id", "username", "email", "password_hash", "roles")

# # Schema for a list of users
# class UserListSchema(Schema):
#     users = fields.List(fields.Nested(UserSchema))

class UserSchema(BaseSchema):
    """
    Schema for serializing and deserializing the User model.
    """
    def get_fields(self) -> dict:
        return {
            "id": fields.Int(dump_only=True),
            "username": fields.Str(required=True, validate=validate.Length(min=3, max=100)),
            "email": fields.Str(required=True, validate=validate.Email()),
            "password_hash": fields.Str(load_only=True, required=True, validate=validate.Length(min=6)),
            "roles": fields.List(fields.Str())
        }
