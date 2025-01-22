from http import HTTPStatus
from quart_schema import validate_request

from app.api.decorators.response_decorator import ResponseDecorator
from app.api.schemas.user_schema import UserInputSchema
from app.core.models.user_model import UserModel
from app.core.repositories.user.user_create_repository import UserCreateRepository
from app.core.repositories.user.user_delete_repository import UserDeleteRepository
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.user.user_create_service import UserCreateService
from app.core.services.user.user_delete_service import UserDeleteService
from app.core.services.user.user_get_service import UserGetService
from app.core.services.user.user_update_service import UserUpdateService
from app.api.routes import api


class UserController:
    """
    Controller that handles user-related HTTP requests.
    """
    @staticmethod
    @validate_request(UserInputSchema)
    @ResponseDecorator.build_response()
    @api.route('/user', methods=['POST'])
    async def create_user(data: UserInputSchema):
        """
        Creates a new user from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the user data and the HTTP status code.
        """
        service = UserCreateService(UserCreateRepository(UserModel))
        user = service.create(**data)
        return user, HTTPStatus.CREATED

    @staticmethod
    @ResponseDecorator.build_response()
    async def get_user(id: int):
        """
        Retrieves a user by ID.

        Args:
            id (str): The ID of the user to retrieve.

        Returns:
            Tuple: A tuple containing the user data (or an error message)
            and the HTTP status code.
        """
        service = UserGetService(UserGetRepository())
        user = service.get_user(id)
        return user, HTTPStatus.OK

    @staticmethod
    @ResponseDecorator.build_response()
    @api.route('/user', methods=['GET'])
    async def get_all_users():
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        service = UserGetService(UserGetRepository())
        users = service.get_all_users()
        return users, HTTPStatus.OK

    @staticmethod
    @validate_request(UserInputSchema)
    @ResponseDecorator.build_response()
    @api.route('/user', methods=['POST'])
    async def update_user(id: int, data: UserInputSchema):
        service = UserUpdateService(UserUpdateRepository())
        user = service.update(id, **data.dump)
        return user, HTTPStatus.OK

    @staticmethod
    @ResponseDecorator.build_response()
    @api.route('/user', methods=['DELETE'])
    async def delete_user(id: int):
        service = UserDeleteService(UserDeleteRepository())
        user = service.delete(id)
        return user, HTTPStatus.OK
