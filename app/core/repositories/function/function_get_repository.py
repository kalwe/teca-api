from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.function_model import Function
from app.core.repositories.shared.get_repository import GetRepository


class FunctionGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Function model_class.

        Args:
            model_class ([Function): The Function model_class class to be managed by
            the repository.
        """
        super().__init__(Function())


    async def get_function_by_name(self, name) -> Optional[Function]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Function]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed FunctionGetRepository.get_function_by_name: {e}") from e
