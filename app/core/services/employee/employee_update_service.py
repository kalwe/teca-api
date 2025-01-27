from typing import Optional
from app.api.schemas.employee_schema import EmployeeInputSchema, EmployeeOutputSchema
from app.core.models.employee_model import Employee
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.repositories.employee.employee_update_repository import EmployeeUpdateRepository
from app.core.services.shared.update_service import UpdateService
from app.core.services.employee.employee_get_service import EmployeeGetService


class EmployeeUpdateService(UpdateService[Employee]):
    """
    Service for managing employee-related business logic.
    """

    def __init__(self, repository: EmployeeUpdateRepository):
        super().__init__(repository)
        self.get_service = EmployeeGetService(EmployeeGetRepository())

    async def update(self, id, data: Employee
                     ) -> Optional[EmployeeOutputSchema]:
        try:
            employee = self.get_service.get_by_id(id)
            if not employee:
                return None

            updated_employee = self.update_data(employee, data)
            return EmployeeOutputSchema.validate(updated_employee)
            # return EmployeeOutputSchema.validate(updated_employee)
        except Exception as e:
            raise Exception(
                f"Failed EmployeeUpdateService().update(): {e}") from e
