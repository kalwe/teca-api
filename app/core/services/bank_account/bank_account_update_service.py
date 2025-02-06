from typing import Optional
from app.api.schemas.bank_account_schema import Bank_accountInputSchema, Bank_accountOutputSchema
from app.core.repositories.bank_account.bank_account_update_repository import (Bank_accountUpdateRepository)
from app.core.services.shared.update_service import UpdateService


class Bank_accountUpdateService(UpdateService):
    """
    Service for managing bank_account-related business logic.
    """
    def __init__(self, repository: Bank_accountUpdateRepository):
        super().__init__(repository)

    async def update(
        self,
        id: int,
        bank_account_data: Bank_accountInputSchema
    ) -> Optional[Bank_accountOutputSchema]:
        updated_bank_account = await self.update_data(id, bank_account_data)
        return Bank_accountOutputSchema.validate(updated_bank_account)
