from http import HTTPStatus
from typing import List

from quart_schema import tag, validate_request, validate_response

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

    # @staticmethod
    @validate_request(UserInputSchema)
    @validate_response(UserOutputSchema, 201)
    @tag(["User"])
    async def create_user(data: UserInputSchema) -> tuple[UserOutputSchema, int]:
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
    @validate_response(UserOutputSchema, 200)
    @tag(["User"])
    async def get_user(id: int) -> tuple[UserOutputSchema, int]:
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
        user = await service.get(id)
        return user, HTTPStatus.OK

    @staticmethod
    @validate_response(List[UserOutputSchema], 200)
    @tag(["User"])
    async def get_all_users() -> tuple[List[UserOutputSchema], int]:
        """
        Retrieves all users using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of users (or an error message) and the HTTP status code.
        """
        repository = UserGetRepository()
        service = UserGetService(repository)
        users = await service.get_all()
        return users, HTTPStatus.OK

    # @staticmethod
    @validate_request(UserInputSchema)
    @validate_response(UserOutputSchema, 200)
    @tag(["User"])
    async def update_user(
        id: int, data: UserInputSchema
    ) -> tuple[UserOutputSchema, int]:
        repository = UserUpdateRepository()
        service = UserUpdateService(repository)
        user = await service.update(id, data)
        return user, HTTPStatus.OK

    # @staticmethod
    @validate_response(UserDeletedSchema, 204)
    @tag(["User"])
    async def delete_user(id: int) -> tuple[UserDeletedSchema, int]:
        repository = UserDeleteRepository()
        service = UserDeleteService(repository)
        user = await service.delete(id)
        return user, HTTPStatus.NO_CONTENT
