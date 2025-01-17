from http import HTTPStatus
from quart import request
from quart_schema import validate_request

from app.api.decorators.response_decorator import ResponseDecorator
from app.api.schemas.user_schema import UserInputSchema
from app.core.repositories.user.user_create_repository import UserCreateRepository
from app.core.repositories.user.user_delete_repository import UserDeleteRepository
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.user.create_user_service import UserCreateService
from app.core.services.user.delete_user_service import UserDeleteService
from app.core.services.user.get_user_service import UserGetService
from app.core.services.user.update_user_service import UserUpdateService


class UserController:
    """
    Controller that handles user-related HTTP requests.
    """
    @staticmethod
    @validate_request(UserInputSchema)
    @ResponseDecorator.build_response()
    async def create_user(data: UserInputSchema):
        """
        Creates a new user from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the user data and the HTTP status code.
        """
        repository = UserCreateRepository()
        service = UserCreateService(repository)
        user = service.create(**data.dump())
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
        repository = UserGetRepository()
        service = UserGetService(repository)
        user = service.get_user(id)
        return user, HTTPStatus.OK

    @staticmethod
    @ResponseDecorator.build_response()
    async def get_all_users():
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        repository = UserGetRepository()
        service = UserGetService(repository)
        users = service.get_all_users()
        return users, HTTPStatus.OK

    @staticmethod
    @validate_request(UserInputSchema)
    @ResponseDecorator.build_response()
    async def update_user(id: int, data: UserInputSchema):
        repository = UserUpdateRepository()
        service = UserUpdateService(repository)
        user = service.update(id, **data.dump)
        return user, HTTPStatus.OK

    @staticmethod
    @ResponseDecorator.build_response()
    async def delete_user(id: int):
        repository = UserDeleteRepository()
        service = UserDeleteService(repository)
        user = service.delete(id)
        return user, HTTPStatus.OK
