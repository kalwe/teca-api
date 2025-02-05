from typing import Optional
from app.api.schemas.bank_account_schema import (
    Bank_accountDeletedSchema, Bank_accountOutputSchema)
from app.core.repositories.bank_account.bank_account_delete_repository import (
    Bank_accountDeleteRepository)
from app.core.services.shared.delete_service import DeleteService


class Bank_accountDeleteService(DeleteService):
    """
    Service for managing bank_account-related delete business logic.
    """

    def __init__(self, repository: Bank_accountDeleteRepository):
        """
        Initialize the bank_account delete service.
        :param repository: The bank_account delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[Bank_accountOutputSchema]:
        """
        Delete a bank_account by ID.
        :param id: The ID of the bank_account to delete.
        :return: The deleted bank_account as a schema, or None if not found.
        """
        deleted_bank_account = await self.soft_delete(id)
        return Bank_accountDeletedSchema.validate(deleted_bank_account)
