from http import HTTPStatus
from typing import List

from quart_schema import validate_request, validate_response

from app.api.schemas.address_schema import (
    AddressDeletedSchema,
    AddressInputSchema,
    AddressOutputSchema,
)
from app.core.repositories.address.address_create_repository import (
    AddressCreateRepository,
)
from app.core.repositories.address.address_delete_repository import (
    AddressDeleteRepository,
)
from app.core.repositories.address.address_get_repository import AddressGetRepository
from app.core.repositories.address.address_update_repository import (
    AddressUpdateRepository,
)
from app.core.services.address.address_create_service import AddressCreateService
from app.core.services.address.address_delete_service import AddressDeleteService
from app.core.services.address.address_get_service import AddressGetService
from app.core.services.address.address_update_service import AddressUpdateService
from quart_schema import tag


class AddressController:
    """
    Controller that handles address-related HTTP requests.
    """

    @staticmethod
    @validate_request(AddressInputSchema)
    @validate_response(AddressOutputSchema)
    @tag(["Address"])
    async def create_address(data: AddressInputSchema) -> AddressOutputSchema:
        """
        Creates a new address from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the address data and the
            HTTP status code.
        """
        repository = AddressCreateRepository()
        service = AddressCreateService(repository)
        address = await service.create(data)
        return address, HTTPStatus.CREATED

    @staticmethod
    @validate_response(AddressOutputSchema)
    @tag(["Address"])
    async def get_address(id: int) -> AddressOutputSchema:
        """
        Retrieves a address by ID.

        Args:
            id (str): The ID of the address to retrieve.

        Returns:
            Tuple: A tuple containing the address data (or an error message)
            and the HTTP status code.
        """
        repository = AddressGetRepository()
        service = AddressGetService(repository)
        address = await service.get(id)
        return address, HTTPStatus.OK

    @staticmethod
    @validate_response(List[AddressOutputSchema])
    @tag(["Address"])
    async def get_all_addresses() -> List[AddressOutputSchema]:
        """
        Retrieves all address using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of address
            (or an error message)
            and the HTTP status code.
        """
        repository = AddressGetRepository()
        service = AddressGetService(repository)
        address = await service.get_all()
        return address, HTTPStatus.OK

    @staticmethod
    @validate_request(AddressInputSchema)
    @validate_response(AddressOutputSchema)
    @tag(["Address"])
    async def update_address(id: int, data: AddressInputSchema) -> AddressOutputSchema:
        repository = AddressUpdateRepository()
        service = AddressUpdateService(repository)
        address = await service.update(id, data)
        return address, HTTPStatus.OK

    @staticmethod
    @validate_response(AddressDeletedSchema)
    @tag(["Address"])
    async def delete_address(id: int) -> AddressDeletedSchema:
        repository = AddressDeleteRepository()
        service = AddressDeleteService(repository)
        address = await service.delete(id)
        return address, HTTPStatus.NO_CONTENT
