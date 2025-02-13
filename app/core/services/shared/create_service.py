from typing import Optional

from app.api.schemas.base_schema import SchemaT
from app.api.schemas.employee_schema import EmployeeOutputSchema
from app.core.models.shared.base_model import ModelT
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.repositories.shared.create_repository import CreateRepositoryT
from app.core.services.employee.employee_get_service import EmployeeGetService


class CreateService:
    """
    Generic service layer for creating new records using a repository.
    """

    def __init__(self, repository: CreateRepositoryT):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[CreateRepository[T]]): The repository
                class used for data creation.
        """
        self._repository = repository
        self._employee_get_service = EmployeeGetService(EmployeeGetRepository())

    async def create_record(self, data_fields: SchemaT) -> Optional[ModelT]:
        """
        Create a new record in the repository.

        Args:
            **fields_data: The fields and their values for the new record.

        Returns:
            T: The newly created record.
        """
        dumped_fields = data_fields.dump(exclude_unset=True)
        created_record = await self._repository.model_create(dumped_fields)
        return created_record

    async def _validate_employee(self, employee_id: int) -> EmployeeOutputSchema:
        """
        Validate the employee ID and return the employee data.

        Args:
            employee_id (int): The ID of the employee to validate.

        Returns:
            EmployeeOutputSchema: The validated employee data.

        Raises:
            ValueError: If the employee with the given ID does not exist.
        """
        employee = await self._employee_get_service.get(employee_id)
        if not employee:
            raise ValueError(f"Employee with id {employee_id} does not exist")
        return employee
