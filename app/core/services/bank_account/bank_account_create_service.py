from typing import Optional

from app.api.schemas.bank_account_schema import (
    BankAccountInputSchema,
    BankAccountOutputSchema,
)
from app.core.repositories.bank_account.bank_account_create_repository import (
    BankAccountCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class BankAccountCreateService(CreateService):
    """
    Service for managing bank_account-related business logic.
    Handles creation of new bank_accounts with role assignment and password hashing.
    """

    def __init__(self, repository: BankAccountCreateRepository):
        """
        Initialize the service with a repository for bank_account operations.

        Args:
            repository (BankAccountCreateRepository): An instance of
                BankAccountCreateRepository
                to handle data persistence for the Bank_account model.
        """
        super().__init__(repository)

    async def create(
        self,
        bank_account_data: BankAccountInputSchema,
    ) -> Optional[BankAccountOutputSchema]:
        """
        Create a new bank_account with additional business logic.

        Args:
            bank_account_data (BankAccountInputSchema): The data for the new bank_account.

        Returns:
            BankAccountOutputSchema: Serialized data of the created bank_account.

        Raises:
            ValueError: If the employee with the given ID does not exist.
        """
        employee = await self._validate_employee(bank_account_data.employee)
        bank_account_data.employee = employee

        created_bank_account = await self.create_record(bank_account_data)
        return BankAccountOutputSchema().validate(created_bank_account)


# FIXME: pydantic_core._pydantic_core.ValidationError: validation errors for EmployeeOutputSchema
