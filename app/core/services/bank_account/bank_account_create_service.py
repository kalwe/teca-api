from typing import Optional
from app.api.schemas.bank_account_schema import Bank_accountInputSchema, Bank_accountOutputSchema
from app.core.repositories.bank_account.bank_account_create_repository import (
    Bank_accountCreateRepository)
from app.core.services.shared.create_service import CreateService


class Bank_accountCreateService(CreateService):
    """
    Service for managing bank_account-related business logic.
    Handles creation of new bank_accounts with role assignment and password hashing.
    """

    def __init__(self, repository: Bank_accountCreateRepository):
        """
        Initialize the service with a repository for bank_account operations.

        Args:
            repository (Bank_accountCreateRepository): An instance of
                Bank_accountCreateRepository
                to handle data persistence for the Bank_account model.
        """
        super().__init__(repository)
        # self._get_service = Bank_accountGetService(Bank_accountGetRepository(Bank_account()))

    async def create(
        self,
        bank_account_data: Bank_accountInputSchema,
    ) -> Optional[Bank_accountOutputSchema]:
        """
        Create a new bank_account with additional business logic.

        Args:
            name (str): The name of the bank_account.
            email (str): The email of the bank_account.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the bank_account.

        Returns:
            Bank_accountOutputSchema: Serialized data of the created bank_account.

        Raises:
            Bank_accountAlreadyExistsException: If a bank_account with the given email
            already exists.
        """        """
        Create a new bank_account with additional business logic.

        Args:
            name (str): The name of the bank_account.
            email (str): The email of the bank_account.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the bank_account.

        Returns:
            Bank_accountOutputSchema: Serialized data of the created bank_account.

        Raises:
            Bank_accountAlreadyExistsException: If a bank_account with the given email
            already exists.
        """
        created_bank_account = await self.create_record(bank_account_data)
        return Bank_accountOutputSchema().validate(created_bank_account)
