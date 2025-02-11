from http import HTTPStatus
from typing import List

from quart_schema import validate_request, validate_response

from app.api.schemas.bank_account_schema import (
    BankAccountDeletedSchema,
    BankAccountInputSchema,
    BankAccountOutputSchema,
)
from app.core.repositories.bank_account.bank_account_create_repository import (
    BankAccountCreateRepository,
)
from app.core.repositories.bank_account.bank_account_delete_repository import (
    BankAccountDeleteRepository,
)
from app.core.repositories.bank_account.bank_account_get_repository import (
    BankAccountGetRepository,
)
from app.core.repositories.bank_account.bank_account_update_repository import (
    BankAccountUpdateRepository,
)
from app.core.services.bank_account.bank_account_create_service import (
    BankAccountCreateService,
)
from app.core.services.bank_account.bank_account_delete_service import (
    BankAccountDeleteService,
)
from app.core.services.bank_account.bank_account_get_service import (
    BankAccountGetService,
)
from app.core.services.bank_account.bank_account_update_service import (
    BankAccountUpdateService,
)
from quart_schema import tag

class BankAccountController:
    """
    Controller that handles bank_account-related HTTP requests.
    """

    @staticmethod
    @validate_request(BankAccountInputSchema)
    @validate_response(BankAccountOutputSchema)
    @tag(["Bank Account"])
    async def create_bank_account(
        data: BankAccountInputSchema,
    ) -> BankAccountOutputSchema:
        """
        Creates a new bank_account from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the bank_account data and the
            HTTP status code.
        """
        repository = BankAccountCreateRepository()
        service = BankAccountCreateService(repository)
        bank_account = await service.create(data)
        return bank_account, HTTPStatus.CREATED

    @staticmethod
    @validate_response(BankAccountOutputSchema)
    @tag(["Bank Account"])
    async def get_bank_account(id: int) -> BankAccountOutputSchema:
        """
        Retrieves a bank_account by ID.

        Args:
            id (str): The ID of the bank_account to retrieve.

        Returns:
            Tuple: A tuple containing the bank_account data (or an error message)
            and the HTTP status code.
        """
        repository = BankAccountGetRepository()
        service = BankAccountGetService(repository)
        bank_account = await service.get(id)
        return bank_account, HTTPStatus.OK

    @staticmethod
    @validate_response(List[BankAccountOutputSchema])
    @tag(["Bank Account"])
    async def get_all_bank_accounts() -> List[BankAccountOutputSchema]:
        """
        Retrieves all bank_accounts using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of bank_accounts
            (or an error message)
            and the HTTP status code.
        """
        repository = BankAccountGetRepository()
        service = BankAccountGetService(repository)
        bank_accounts = await service.get_all()
        return bank_accounts, HTTPStatus.OK

    @staticmethod
    @validate_request(BankAccountInputSchema)
    @validate_response(BankAccountOutputSchema)
    @tag(["Bank Account"])
    async def update_bank_account(
        id: int, data: BankAccountInputSchema
    ) -> BankAccountOutputSchema:
        repository = BankAccountUpdateRepository()
        service = BankAccountUpdateService(repository)
        bank_account = await service.update(id, data)
        return bank_account, HTTPStatus.OK

    @staticmethod
    @validate_response(BankAccountDeletedSchema)
    @tag(["Bank Account"])
    async def delete_bank_account(id: int) -> BankAccountDeletedSchema:
        repository = BankAccountDeleteRepository()
        service = BankAccountDeleteService(repository)
        bank_account = await service.delete(id)
        return bank_account, HTTPStatus.NO_CONTENT
