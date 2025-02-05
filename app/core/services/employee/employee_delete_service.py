from typing import Optional
from app.api.schemas.employee_schema import (
    EmployeeDeletedSchema, EmployeeOutputSchema)
from app.core.repositories.employee.employee_delete_repository import (
    EmployeeDeleteRepository)
from app.core.services.shared.delete_service import DeleteService


class EmployeeDeleteService(DeleteService):
    """
    Service for managing employee-related delete business logic.
    """

    def __init__(self, repository: EmployeeDeleteRepository):
        """
        Initialize the employee delete service.
        :param repository: The employee delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[EmployeeOutputSchema]:
        """
        Delete a employee by ID.
        :param id: The ID of the employee to delete.
        :return: The deleted employee as a schema, or None if not found.
        """
        deleted_employee = await self.soft_delete(id)
        return EmployeeDeletedSchema.validate(deleted_employee)
