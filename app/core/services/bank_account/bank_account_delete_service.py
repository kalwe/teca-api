from typing import Optional

from app.api.schemas.bank_account_schema import BankAccountDeletedSchema
from app.core.repositories.bank_account.bank_account_delete_repository import (
    BankAccountDeleteRepository,
)
from app.core.services.shared.delete_service import DeleteService


class BankAccountDeleteService(DeleteService):
    """
    Service for managing bank_account-related delete business logic.
    """

    def __init__(self, repository: BankAccountDeleteRepository):
        """
        Initialize the bank_account delete service.
        :param repository: The bank_account delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[BankAccountDeletedSchema]:
        """
        Delete a bank_account by ID.
        :param id: The ID of the bank_account to delete.
        :return: The deleted bank_account as a schema, or None if not found.
        """
        # TypeError: BaseSchema.validate() missing 1 required positional argument: 'model', (Resolved) with ()
        deleted_bank_account = await self.soft_delete(id)
        return BankAccountDeletedSchema().validate(deleted_bank_account)

    # FIXME: pydantic_core._pydantic_core.ValidationError: 1 validation error for BankAccountDeletedSchema
