from typing import Optional

from app.api.schemas.employee_schema import EmployeeInputSchema, EmployeeOutputSchema
from app.core.repositories.employee.employee_update_repository import (
    EmployeeUpdateRepository,
)
from app.core.services.shared.update_service import UpdateService


class EmployeeUpdateService(UpdateService):
    """
    Service for managing employee-related business logic.
    """

    def __init__(self, repository: EmployeeUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, employee_data: EmployeeInputSchema
    ) -> Optional[EmployeeOutputSchema]:
        updated_employee = await self.update_data(id, employee_data)
        return EmployeeOutputSchema.validate(updated_employee)
