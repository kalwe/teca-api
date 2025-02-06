from http import HTTPStatus
from typing import List
from quart import request
from quart_schema import validate_request, validate_response

from app.api.schemas.clothing_schema import ClothingDeletedSchema, ClothingInputSchema, ClothingOutputSchema
from app.core.repositories.clothing.clothing_create_repository import ClothingCreateRepository
from app.core.repositories.clothing.clothing_delete_repository import ClothingDeleteRepository
from app.core.repositories.clothing.clothing_get_repository import ClothingGetRepository
from app.core.repositories.clothing.clothing_update_repository import ClothingUpdateRepository
from app.core.services.clothing.clothing_create_service import ClothingCreateService
from app.core.services.clothing.clothing_delete_service import ClothingDeleteService
from app.core.services.clothing.clothing_get_service import ClothingGetService
from app.core.services.clothing.clothing_update_service import ClothingUpdateService


class ClothingController:
    """
    Controller that handles clothing-related HTTP requests.
    """

    @staticmethod
    @validate_request(ClothingInputSchema)
    @validate_response(ClothingOutputSchema)
    async def create_clothing(
        data: ClothingInputSchema
    ) -> ClothingOutputSchema:
        """
        Creates a new clothing from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the clothing data and the
            HTTP status code.
        """
        repository = ClothingCreateRepository()
        service = ClothingCreateService(repository)
        clothing = await service.create(data)
        return clothing, HTTPStatus.CREATED

    @staticmethod
    @validate_response(ClothingOutputSchema)
    async def get_clothing(id: int):
        """
        Retrieves a clothing by ID.

        Args:
            id (str): The ID of the clothing to retrieve.

        Returns:
            Tuple: A tuple containing the clothing data (or an error message)
            and the HTTP status code.
        """
        service = ClothingGetService(ClothingGetRepository())
        clothing = service.get(id)
        return clothing, HTTPStatus.OK

    @staticmethod
    @validate_response(List[ClothingOutputSchema])
    async def get_all_clothings():
        """
        Retrieves all clothings using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of clothings
            (or an error message)
            and the HTTP status code.
        """
        service = ClothingGetService(ClothingGetRepository())
        clothings = service.get_all()
        return clothings, HTTPStatus.OK

    @staticmethod
    @validate_request(ClothingInputSchema)
    @validate_response(ClothingOutputSchema)
    async def update_clothing(id: int, data: ClothingInputSchema):
        repository = ClothingUpdateRepository()
        service = ClothingUpdateService(repository)
        clothing = service.update(id, data)
        return clothing, HTTPStatus.OK

    @staticmethod
    @validate_response(ClothingDeletedSchema)
    async def delete_clothing(id: int):
        repository = ClothingDeleteRepository()
        service = ClothingDeleteService(repository)
        clothing = service.delete(id)
        return clothing, HTTPStatus.NO_CONTENT
