from http import HTTPStatus
from typing import List
from quart import request
from quart_schema import validate_request, validate_response

from app.api.schemas.roles_schema import RolesDeletedSchema, RolesInputSchema, RolesOutputSchema
from app.core.repositories.roles.roles_create_repository import RolesCreateRepository
from app.core.repositories.roles.roles_delete_repository import RolesDeleteRepository
from app.core.repositories.roles.roles_get_repository import RolesGetRepository
from app.core.repositories.roles.roles_update_repository import RolesUpdateRepository
from app.core.services.roles.roles_create_service import RolesCreateService
from app.core.services.roles.roles_delete_service import RolesDeleteService
from app.core.services.roles.roles_get_service import RolesGetService
from app.core.services.roles.roles_update_service import RolesUpdateService


class RolesController:
    """
    Controller that handles roles-related HTTP requests.
    """

    @staticmethod
    @validate_request(RolesInputSchema)
    @validate_response(RolesOutputSchema)
    async def create_roles(
        data: RolesInputSchema
    ) -> RolesOutputSchema:
        """
        Creates a new roles from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the roles data and the
            HTTP status code.
        """
        repository = RolesCreateRepository()
        service = RolesCreateService(repository)
        roles = await service.create(data)
        return roles, HTTPStatus.CREATED

    @staticmethod
    @validate_response(RolesOutputSchema)
    async def get_roles(id: int):
        """
        Retrieves a roles by ID.

        Args:
            id (str): The ID of the roles to retrieve.

        Returns:
            Tuple: A tuple containing the roles data (or an error message)
            and the HTTP status code.
        """
        service = RolesGetService(RolesGetRepository())
        roles = service.get(id)
        return roles, HTTPStatus.OK

    @staticmethod
    @validate_response(List[RolesOutputSchema])
    async def get_all_roless():
        """
        Retrieves all roless using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of roless
            (or an error message)
            and the HTTP status code.
        """
        service = RolesGetService(RolesGetRepository())
        roless = service.get_all()
        return roless, HTTPStatus.OK

    @staticmethod
    @validate_request(RolesInputSchema)
    @validate_response(RolesOutputSchema)
    async def update_roles(id: int, data: RolesInputSchema):
        repository = RolesUpdateRepository()
        service = RolesUpdateService(repository)
        roles = service.update(id, data)
        return roles, HTTPStatus.OK

    @staticmethod
    @validate_response(RolesDeletedSchema)
    async def delete_roles(id: int):
        repository = RolesDeleteRepository()
        service = RolesDeleteService(repository)
        roles = service.delete(id)
        return roles, HTTPStatus.NO_CONTENT
