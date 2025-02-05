from http import HTTPStatus
from typing import List
from quart import request
from quart_schema import validate_request, validate_response

from app.api.schemas.function_schema import FunctionDeletedSchema, FunctionInputSchema, FunctionOutputSchema
from app.core.repositories.function.function_create_repository import FunctionCreateRepository
from app.core.repositories.function.function_delete_repository import FunctionDeleteRepository
from app.core.repositories.function.function_get_repository import FunctionGetRepository
from app.core.repositories.function.function_update_repository import FunctionUpdateRepository
from app.core.services.function.function_create_service import FunctionCreateService
from app.core.services.function.function_delete_service import FunctionDeleteService
from app.core.services.function.function_get_service import FunctionGetService
from app.core.services.function.function_update_service import FunctionUpdateService


class FunctionController:
    """
    Controller that handles function-related HTTP requests.
    """

    @staticmethod
    @validate_request(FunctionInputSchema)
    @validate_response(FunctionOutputSchema)
    async def create_function(
        data: FunctionInputSchema
    ) -> FunctionOutputSchema:
        """
        Creates a new function from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the function data and the
            HTTP status code.
        """
        repository = FunctionCreateRepository()
        service = FunctionCreateService(repository)
        function = await service.create(data)
        return function, HTTPStatus.CREATED

    @staticmethod
    @validate_response(FunctionOutputSchema)
    async def get_function(id: int):
        """
        Retrieves a function by ID.

        Args:
            id (str): The ID of the function to retrieve.

        Returns:
            Tuple: A tuple containing the function data (or an error message)
            and the HTTP status code.
        """
        service = FunctionGetService(FunctionGetRepository())
        function = service.get(id)
        return function, HTTPStatus.OK

    @staticmethod
    @validate_response(List[FunctionOutputSchema])
    async def get_all_functions():
        """
        Retrieves all functions using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of functions
            (or an error message)
            and the HTTP status code.
        """
        service = FunctionGetService(FunctionGetRepository())
        functions = service.get_all()
        return functions, HTTPStatus.OK

    @staticmethod
    @validate_request(FunctionInputSchema)
    @validate_response(FunctionOutputSchema)
    async def update_function(id: int, data: FunctionInputSchema):
        repository = FunctionUpdateRepository()
        service = FunctionUpdateService(repository)
        function = service.update(id, data)
        return function, HTTPStatus.OK

    @staticmethod
    @validate_response(FunctionDeletedSchema)
    async def delete_function(id: int):
        repository = FunctionDeleteRepository()
        service = FunctionDeleteService(repository)
        function = service.delete(id)
        return function, HTTPStatus.NO_CONTENT
