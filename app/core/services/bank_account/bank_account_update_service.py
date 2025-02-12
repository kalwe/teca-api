from typing import Optional

from app.api.schemas.bank_account_schema import (
    BankAccountInputSchema,
    BankAccountOutputSchema,
)
from app.core.repositories.bank_account.bank_account_update_repository import (
    BankAccountUpdateRepository,
)
from app.core.services.shared.update_service import UpdateService


class BankAccountUpdateService(UpdateService):
    """
    Service for managing bank_account-related business logic.
    """

    def __init__(self, repository: BankAccountUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, bank_account_data: BankAccountInputSchema
    ) -> Optional[BankAccountOutputSchema]:
        updated_bank_account = await self.update_data(id, bank_account_data)
        return BankAccountOutputSchema().validate(updated_bank_account)


# FIXME: <p>Failed to decode JSON: Expecting property name enclosed in double quotes: line 7 column 1 (char 114)</p>
