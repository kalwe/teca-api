from http import HTTPStatus
from typing import List

from quart_schema import validate_request, validate_response

from app.api.schemas.user_schema import (
    UserDeletedSchema,
    UserInputSchema,
    UserOutputSchema,
)
from app.core.repositories.user.user_create_repository import UserCreateRepository
from app.core.repositories.user.user_delete_repository import UserDeleteRepository
from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.repositories.user.user_update_repository import UserUpdateRepository
from app.core.services.user.user_create_service import UserCreateService
from app.core.services.user.user_delete_service import UserDeleteService
from app.core.services.user.user_get_service import UserGetService
from app.core.services.user.user_update_service import UserUpdateService


class UserController:
    """
    Controller that handles user-related HTTP requests.
    """

    @staticmethod
    @validate_request(UserInputSchema)
    @validate_response(UserOutputSchema)
    async def create_user(data: UserInputSchema) -> UserOutputSchema:
        """
        Creates a new user from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the user data and the HTTP status code.
        """
        repository = UserCreateRepository()
        service = UserCreateService(repository)
        user = await service.create(data)
        return user, HTTPStatus.CREATED

    @staticmethod
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
        user = service.get(id)
        return user, HTTPStatus.OK

    @staticmethod
    @validate_response(List[UserOutputSchema])
    async def get_all_users():
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        service = UserGetService(UserGetRepository())
        users = service.get_all()
        return users, HTTPStatus.OK

    @staticmethod
    @validate_request(UserInputSchema)
    @validate_response(UserOutputSchema)
    async def update_user(id: int, data: UserInputSchema):
        repository = UserUpdateRepository()
        service = UserUpdateService(repository)
        user = service.update(id, data)
        return user, HTTPStatus.OK

    @staticmethod
    @validate_response(UserDeletedSchema)
    async def delete_user(id: int):
        repository = UserDeleteRepository()
        service = UserDeleteService(repository)
        user = service.delete(id)
        return user, HTTPStatus.NO_CONTENT
