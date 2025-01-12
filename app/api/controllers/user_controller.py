from http import HTTPStatus
from quart import request

from app.api.common.fetch.fetch_handler import FetchHandler
from app.api.schemas.user_schema import UserSchema
from app.core.services.user_service import UserService


class UserController:
    """
    Controller that handles user-related HTTP requests.
    """
    @staticmethod
    @input_validation(UserSchema)
    def create_user():
        """
        Creates a new user from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the user data and the HTTP status code.
        """
        data = request.get_json()
        user_service = UserService()

        try:
            user = user_service.create_user(data)
            return user, ResponseMessages.CREATED_SUCCESS.value, HTTPStatus.CREATED
        except Exception as e:
            return None, f"{ResponseMessages.INTERNAL_SERVER_ERROR}: {str(e)}", HTTPStatus.INTERNAL_SERVER_ERROR

    @staticmethod
    async def get_user(user_id):
        """
        Retrieves a user by ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            Tuple: A tuple containing the user data (or an error message) and the HTTP status code.
        """
        user_service = UserService()
        return await FetchHandler.fetch_item(user_service, user_id)

    @staticmethod
    async def get_all_users():
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        user_service = UserService()
        return await FetchHandler.fetch_all(user_service)
