from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.bank_account_model import Bank_account
from app.core.repositories.shared.get_repository import GetRepository


class Bank_accountGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Bank_account model_class.

        Args:
            model_class ([Bank_account): The Bank_account model_class class to be managed by
            the repository.
        """
        super().__init__(Bank_account())


    async def get_bank_account_by_name(self, name) -> Optional[Bank_account]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Bank_account]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed Bank_accountGetRepository.get_bank_account_by_name: {e}") from e
