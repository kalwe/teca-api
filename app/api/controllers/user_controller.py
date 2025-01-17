from http import HTTPStatus
from quart import request
from quart_schema import validate_request

from app.api.decorators.response_decorator import ResponseDecorator
from app.api.schemas.user_schema import UserInputSchema
from app.core.services.user.create_user_service import UserCreateService


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
    async def get_user(id):
        """
        Retrieves a user by ID.

        Args:
            id (str): The ID of the user to retrieve.

        Returns:
            Tuple: A tuple containing the user data (or an error message)
            and the HTTP status code.
        """
        # user_service = UserService()
        return await FetchHandler.fetch_item(user_service, id)

    @staticmethod
    async def get_all_users():
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        # user_service = UserService()
        return await FetchHandler.fetch_all(user_service)
