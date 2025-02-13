from typing import List, Optional

from app.api.schemas.bank_account_schema import (
    BankAccountOutputSchema,
)
from app.core.repositories.bank_account.bank_account_get_repository import (
    BankAccountGetRepository,
)
from app.core.services.shared.get_service import GetService


class BankAccountGetService(GetService):
    """
    Service for managing bank_account-related business logic, leveraging generic
    methods from GetService.

    This service adds bank_account-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = bank_accountGetRepository

    def __init__(self, repository: BankAccountGetRepository):
        """
        Initialize the service with a bank_account-specific repository.

        Args:
            repository (bankAccountGetRepository): Repository for bank_account
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[BankAccountOutputSchema]:
        bank_account = await self.get_by_id(id)
        return BankAccountOutputSchema().validate(bank_account)

    # FIXME: pydantic_core._pydantic_core.ValidationError: 5 validation errors for BankAccountOutputSchema

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[BankAccountOutputSchema]]:
        bank_accounts = await self.get_all_records(filters)
        return [
            BankAccountOutputSchema().validate(bank_account)
            for bank_account in bank_accounts
        ]
        # With no records, returns an empty list
