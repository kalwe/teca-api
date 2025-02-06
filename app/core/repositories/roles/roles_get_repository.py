from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.roles_model import Roles
from app.core.repositories.shared.get_repository import GetRepository


class RolesGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Roles model_class.

        Args:
            model_class ([Roles): The Roles model_class class to be managed by
            the repository.
        """
        super().__init__(Roles())


    async def get_roles_by_name(self, name) -> Optional[Roles]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Roles]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed RolesGetRepository.get_roles_by_name: {e}") from e
