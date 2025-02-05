from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.address_model import Address
from app.core.repositories.shared.get_repository import GetRepository


class AddressGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Address model_class.

        Args:
            model_class ([Address): The Address model_class class to be managed by
            the repository.
        """
        super().__init__(Address())


    async def get_address_by_name(self, name) -> Optional[Address]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Address]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed AddressGetRepository.get_address_by_name: {e}") from e
