from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.contact_model import Contact
from app.core.repositories.shared.get_repository import GetRepository


class ContactGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Contact model_class.

        Args:
            model_class ([Contact): The Contact model_class class to be managed by
            the repository.
        """
        super().__init__(Contact())


    async def get_contact_by_name(self, name) -> Optional[Contact]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Contact]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed ContactGetRepository.get_contact_by_name: {e}") from e
