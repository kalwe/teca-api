from flask import jsonify, request
from app.api.common.fetch.fetch_helpers import FetchHelper
from app.api.decorators.response_decorator import ApiResponseDecorator
from app.core.services.user_service import UserService
from app.decorators.route_validations_decorator import validate_input


class UserController:
    """
    Controller that handles user-related HTTP requests.
    """
    @staticmethod
    @validate_input()
    @ApiResponseDecorator.standardize_response
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
            return user, None, 201
        except Exception as e:
            return None, f"An error occurred: {str(e)}", 500

    @staticmethod
    @ApiResponseDecorator.standardize_response
    async def get_user(user_id):
        """
        Retrieves a user by ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            Tuple: A tuple containing the user data (or an error message) and the HTTP status code.
        """
        user_service = UserService()

        # Use FetchHelper to fetch the user and handle errors
        user = await FetchHelper.fetch_item(
            user_service, user_id
        )

        # Return user data if found, otherwise return the error response
        return user, error_message, status_code

    @staticmethod
    @ApiResponseDecorator.standardize_response
    async def get_all_users():
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        user_service = UserService()

        # Use FetchHelper to fetch all users and handle errors
        users = await FetchHelper.fetch_all_items(
            user_service
        )

        # Return users if found, otherwise return the error response
        return users, error_message, status_code
