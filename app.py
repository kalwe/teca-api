# import secrets
# from typing import Optional
# # from uuid import uuid4
# from quart import Blueprint
# from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr
# from quart import Quart
# from quart_schema import QuartSchema, validate_request, validate_response
# from tortoise.models import Model
# from tortoise import fields

# from app.common.hash_utils import hash_provider


# class RepoError(Exception):
#     pass


# class Config(object):
#     DEBUG = True
#     TESTING = False
#     QUART_AUTH_MODE = "bearer"
#     QUART_SCHEMA_CONVERSION_PREFERENCE = "pydantic"
#     SECRET_KEY = secrets.token_hex(128)
#     DB_USER = "docker"
#     DB_PASSWORD = "docker"
#     DB_NAME = "teca_coif"
#     DB_URI = "postgres://docker:docker@db:5432/teca_coif"


# app = Quart(__name__)
# app.config.from_object(Config)

# QuartSchema(app)


# class PasswordMixin:
#     password: SecretStr = Field(...)


# class UserBase(BaseModel):
#     email: EmailStr = Field(...)
#     name: str = Field(...)


# class UserSchemaIn(UserBase, PasswordMixin):
#     model_config = ConfigDict(
#         alias_generator=lambda field: {
#             'password': 'password_hash'
#         }.get(field, field),
#         populate_by_name=True,
#         by_alias=True,
#     )


# class UserOutSchema(UserBase):
#     model_config = ConfigDict(
#         extra="ignore",
#         from_attributes=True
#     )
#     id: int = Field()


# class User(Model):
#     id = fields.CharField(pk=True, max_length=255)
#     email = fields.CharField(unique=True, max_length=255)
#     name = fields.CharField(max_length=80, unique=True)
#     password_hash = fields.CharField(max_length=255)


# type ModelT = Model
# type SchemaT = BaseModel
# type CreateRepoT = CreateRepo


# # Repos

# class CreateRepo:
#     def __init__(self, model_class: ModelT):
#         self._model_class = model_class

#     async def model_create(self, data_model: SchemaT) -> Optional[ModelT]:
#         try:
#             # created_model = await self._model_class.create(
#             #     **data_model.model_dump()
#             # )
#             # return created_model
#             # Test
#             # user_dump = data_model.model_dump()
#             # self._model_class(**user_dump)
#             # print(f"CreateRepo - User create: {data_model}")
#             return User(id=44, **data_model.model_dump())
#             # return await self._model_class(user_dump)
#         except Exception as e:
#             raise RepoError(f"CreateRepository fail") from e


# class UserCreateRepo(CreateRepo):
#     def __init__(self):
#         super().__init__(User())


# # SERVICES

# class CreateService:
#     def __init__(self, repo: CreateRepoT):
#         self._repo = repo

#     async def create_model(self, data_fields: SchemaT) -> Optional[ModelT]:
#         data_fields = data_fields.model_dump()
#         # TODO: validate schema to transforma password name
#         # and gen id
#         validated_model = data_fields.model_validate(data_fields)
#         created_model = await self._repo.model_create(validated_model)
#         return created_model


# class UserCreateService(CreateService):

#     def __init__(self, repo: UserCreateRepo):
#         super().__init__(repo)
#         # self._repo = repo

#     async def create(self, user_data: UserSchemaIn) -> Optional[UserOutSchema]:
#         password = user_data.password.get_secret_value()
#         user_data.password = hash_provider(password)

#         created_user = await self.create_model(user_data)
#         return UserOutSchema.model_validate(created_user)


# class UserC:

#     # Create USer
#     @validate_request(UserSchemaIn)
#     @validate_response(UserOutSchema)
#     async def create_user(data: UserSchemaIn) -> UserOutSchema:
#         # user_data = data.model_dump()
#         # user = User(email=data.email, name=data.name, password=data.password)
#         # user = User(**data.model_dump())
#         # user = User(id=55, **user_data)
#         # user_out = UserOutSchema.model_validate(user)
#         repo = UserCreateRepo()
#         service = UserCreateService(repo)
#         user_out = await service.create(data)
#         return user_out, 201

#     # Delete User
#     async def delete_user(id: int):
#         user_deleted = {
#             "id": id,
#             "active": False,
#         }
#         return user_deleted, 200


# api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
# user_bp = Blueprint('user', __name__, url_prefix='/user')


# # def add_rules(bp: Blueprint) -> Blueprint:
# user_bp.add_url_rule(
#     '/', view_func=UserC.create_user, methods=["POST"])
# user_bp.add_url_rule(
#     '/<int:id>', view_func=UserC.delete_user, methods=["DELETE"])
# # return bp


# # def init_bp(app: Quart) -> None:
# # bp = add_rules(user_bp)
# api_bp.register_blueprint(user_bp)
# app.register_blueprint(api_bp)


# # init_bp(app)
# app.run()
