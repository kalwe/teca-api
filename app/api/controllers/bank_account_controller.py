from http import HTTPStatus
from typing import List
from quart import request
from quart_schema import validate_request, validate_response

from app.api.schemas.bank_account_schema import Bank_accountDeletedSchema, Bank_accountInputSchema, Bank_accountOutputSchema
from app.core.repositories.bank_account.bank_account_create_repository import Bank_accountCreateRepository
from app.core.repositories.bank_account.bank_account_delete_repository import Bank_accountDeleteRepository
from app.core.repositories.bank_account.bank_account_get_repository import Bank_accountGetRepository
from app.core.repositories.bank_account.bank_account_update_repository import Bank_accountUpdateRepository
from app.core.services.bank_account.bank_account_create_service import Bank_accountCreateService
from app.core.services.bank_account.bank_account_delete_service import Bank_accountDeleteService
from app.core.services.bank_account.bank_account_get_service import Bank_accountGetService
from app.core.services.bank_account.bank_account_update_service import Bank_accountUpdateService


class Bank_accountController:
    """
    Controller that handles bank_account-related HTTP requests.
    """

    @staticmethod
    @validate_request(Bank_accountInputSchema)
    @validate_response(Bank_accountOutputSchema)
    async def create_bank_account(
        data: Bank_accountInputSchema
    ) -> Bank_accountOutputSchema:
        """
        Creates a new bank_account from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the bank_account data and the
            HTTP status code.
        """
        repository = Bank_accountCreateRepository()
        service = Bank_accountCreateService(repository)
        bank_account = await service.create(data)
        return bank_account, HTTPStatus.CREATED

    @staticmethod
    @validate_response(Bank_accountOutputSchema)
    async def get_bank_account(id: int):
        """
        Retrieves a bank_account by ID.

        Args:
            id (str): The ID of the bank_account to retrieve.

        Returns:
            Tuple: A tuple containing the bank_account data (or an error message)
            and the HTTP status code.
        """
        service = Bank_accountGetService(Bank_accountGetRepository())
        bank_account = service.get(id)
        return bank_account, HTTPStatus.OK

    @staticmethod
    @validate_response(List[Bank_accountOutputSchema])
    async def get_all_bank_accounts():
        """
        Retrieves all bank_accounts using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of bank_accounts
            (or an error message)
            and the HTTP status code.
        """
        service = Bank_accountGetService(Bank_accountGetRepository())
        bank_accounts = service.get_all()
        return bank_accounts, HTTPStatus.OK

    @staticmethod
    @validate_request(Bank_accountInputSchema)
    @validate_response(Bank_accountOutputSchema)
    async def update_bank_account(id: int, data: Bank_accountInputSchema):
        repository = Bank_accountUpdateRepository()
        service = Bank_accountUpdateService(repository)
        bank_account = service.update(id, data)
        return bank_account, HTTPStatus.OK

    @staticmethod
    @validate_response(Bank_accountDeletedSchema)
    async def delete_bank_account(id: int):
        repository = Bank_accountDeleteRepository()
        service = Bank_accountDeleteService(repository)
        bank_account = service.delete(id)
        return bank_account, HTTPStatus.NO_CONTENT
