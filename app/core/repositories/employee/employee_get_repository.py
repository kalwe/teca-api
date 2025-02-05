from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.employee_model import Employee
from app.core.repositories.shared.get_repository import GetRepository


class EmployeeGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Employee model_class.

        Args:
            model_class ([Employee): The Employee model_class class to be managed by
            the repository.
        """
        super().__init__(Employee())

    async def get_employee_by_name(self, name) -> Optional[Employee]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Employee]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed EmployeeGetRepository.get_employee_by_name: {e}") from e
