from http import HTTPStatus
from quart import request
from quart_schema import validate_request

from app.api.decorators.response_decorator import ResponseDecorator
from app.api.schemas.user_schema import UserInputSchema
from app.core.services.user.create_user_service import UserCreateService
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
        service = UserCreateService()
        user = service.create_user(**data.dump())
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
        user_get_service = UserGetService()
        user = user_get_service.repository.get_by_id(id)
        return user, HTTPStatus.OK

    @staticmethod
    @ResponseDecorator.build_response()
    async def get_all_users():
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        user_get_service = UserGetService()
        users = user_get_service.repository.get_all()
        return users, HTTPStatus.OK

    @staticmethod
    @validate_request(UserInputSchema)
    @ResponseDecorator.build_response()
    async def update_user(user: UserInputSchema):
        user_update_service = UserUpdateService()
        user_update_service.update()
