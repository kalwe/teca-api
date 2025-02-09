from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.clothing_model import Clothing
from app.core.repositories.shared.get_repository import GetRepository


class ClothingGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Clothing model_class.

        Args:
            model_class ([Clothing): The Clothing model_class class to be managed by
            the repository.
        """
        super().__init__(Clothing())


    async def get_clothing_by_name(self, name) -> Optional[Clothing]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Clothing]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed ClothingGetRepository.get_clothing_by_name: {e}") from e
