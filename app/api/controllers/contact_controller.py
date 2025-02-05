from http import HTTPStatus
from typing import List
from quart import request
from quart_schema import validate_request, validate_response

from app.api.schemas.contact_schema import ContactDeletedSchema, ContactInputSchema, ContactOutputSchema
from app.core.repositories.contact.contact_create_repository import ContactCreateRepository
from app.core.repositories.contact.contact_delete_repository import ContactDeleteRepository
from app.core.repositories.contact.contact_get_repository import ContactGetRepository
from app.core.repositories.contact.contact_update_repository import ContactUpdateRepository
from app.core.services.contact.contact_create_service import ContactCreateService
from app.core.services.contact.contact_delete_service import ContactDeleteService
from app.core.services.contact.contact_get_service import ContactGetService
from app.core.services.contact.contact_update_service import ContactUpdateService


class ContactController:
    """
    Controller that handles contact-related HTTP requests.
    """

    @staticmethod
    @validate_request(ContactInputSchema)
    @validate_response(ContactOutputSchema)
    async def create_contact(
        data: ContactInputSchema
    ) -> ContactOutputSchema:
        """
        Creates a new contact from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the contact data and the
            HTTP status code.
        """
        repository = ContactCreateRepository()
        service = ContactCreateService(repository)
        contact = await service.create(data)
        return contact, HTTPStatus.CREATED

    @staticmethod
    @validate_response(ContactOutputSchema)
    async def get_contact(id: int):
        """
        Retrieves a contact by ID.

        Args:
            id (str): The ID of the contact to retrieve.

        Returns:
            Tuple: A tuple containing the contact data (or an error message)
            and the HTTP status code.
        """
        service = ContactGetService(ContactGetRepository())
        contact = service.get(id)
        return contact, HTTPStatus.OK

    @staticmethod
    @validate_response(List[ContactOutputSchema])
    async def get_all_contacts():
        """
        Retrieves all contacts using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of contacts
            (or an error message)
            and the HTTP status code.
        """
        service = ContactGetService(ContactGetRepository())
        contacts = service.get_all()
        return contacts, HTTPStatus.OK

    @staticmethod
    @validate_request(ContactInputSchema)
    @validate_response(ContactOutputSchema)
    async def update_contact(id: int, data: ContactInputSchema):
        repository = ContactUpdateRepository()
        service = ContactUpdateService(repository)
        contact = service.update(id, data)
        return contact, HTTPStatus.OK

    @staticmethod
    @validate_response(ContactDeletedSchema)
    async def delete_contact(id: int):
        repository = ContactDeleteRepository()
        service = ContactDeleteService(repository)
        contact = service.delete(id)
        return contact, HTTPStatus.NO_CONTENT
