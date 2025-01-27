from typing import Optional
from app.api.schemas.employee_schema import EmployeeOutputSchema
from app.core.models.employee_model import Employee
from app.core.repositories.employee.employee_delete_repository import (
    EmployeeDeleteRepository)
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.services.shared.delete_service import DeleteService
from app.core.services.employee.employee_get_service import EmployeeGetService


class EmployeeDeleteService(DeleteService[Employee]):
    """
    Service for managing employee-related delete business logic.
    """

    def __init__(self, repository: EmployeeDeleteRepository):
        """
        Initialize the employee delete service.
        :param repository: The employee delete repository instance.
        """
        super().__init__(repository)
        self.get_service = EmployeeGetService(
            EmployeeGetRepository(Employee()))

    async def delete(self, id: int) -> Optional[EmployeeOutputSchema]:
        """
        Delete a employee by ID.
        :param id: The ID of the employee to delete.
        :return: The deleted employee as a schema, or None if not found.
        """
        try:
            employee = await self.get_service.get_by_id(id)
            if not employee:
                return None

            # self.repository.
            deleted_employee = await self.soft_delete(employee)
            return EmployeeOutputSchema.validate(deleted_employee)
        except Exception as e:
            raise Exception(f"Failed employee service delete: {e}") from e
