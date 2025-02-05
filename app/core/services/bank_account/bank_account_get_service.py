from typing import List, Optional
from app.api.schemas.bank_account_schema import bank_accountOutputSchema
from app.core.repositories.bank_account.bank_account_get_repository import (
    bank_accountGetRepository)
from app.core.services.shared.get_service import GetService


class Bank_accountGetService(GetService):
    """
    Service for managing bank_account-related business logic, leveraging generic
    methods from GetService.

    This service adds bank_account-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = bank_accountGetRepository

    def __init__(self, repository: bank_accountGetRepository):
        """
        Initialize the service with a bank_account-specific repository.

        Args:
            repository (bank_accountGetRepository): Repository for bank_account
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[bank_accountOutputSchema]:
        bank_account = self.get_by_id(id)
        return bank_accountOutputSchema.validate(bank_account)

    async def get_all(self, filters: Optional[dict] = None
                      ) -> Optional[List[bank_accountOutputSchema]]:
        bank_accounts = self.get_all_records(filters)
        return [bank_accountOutputSchema.validate(bank_account) for bank_account in bank_accounts]

    async def get_by_name(self, name: str) -> Optional[bank_accountOutputSchema]:
        bank_account = self._get_repository.get_bank_account_by_name(name)
        return bank_accountOutputSchema.validate(bank_account)
