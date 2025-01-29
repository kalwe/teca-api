from typing import List, Optional
from app.api.schemas.employee_schema import EmployeeOutputSchema
from app.core.models.employee_model import Employee
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.services.shared.get_service import GetService


class EmployeeGetService(GetService[Employee]):
    """
    Service for managing employee-related business logic, leveraging generic
    methods from GetService.

    This service adds employee-specific business logic on top of the generic
    functionality provided by GetService.
    """

    def __init__(self, repository: EmployeeGetRepository):
        """
        Initialize the service with a Employee-specific repository.

        Args:
            repository (EmployeeGetRepository): Repository for employee
            data retrieval.
        """
        super().__init__(repository)
        self.repository = repository
        # self.model_class = self.repository.model_class

    async def get(self, id: int) -> Optional[EmployeeOutputSchema]:
        try:
            self.repository.model_class.id = id
            employee = self.get_by_id()
            if not employee:
                return None

            return EmployeeOutputSchema.validate(employee)
        except Exception as e:
            raise Exception(
                f"Failed EmployeeGetService().get(): {e}") from e

    async def get_all(self, filters: Optional[dict] = None
                      ) -> Optional[List[EmployeeOutputSchema]]:
        try:
            employees = self.get_all_records(filters)
            if not employees:
                return None

            return [EmployeeOutputSchema.validate(employee) for employee in employees]
        except Exception as e:
            raise Exception(
                f"Failed EmployeeGetService().get_all(): {e}") from e

    async def get_by_email(self, email: str) -> Optional[EmployeeOutputSchema]:
        """
        Retrieve a employee by their email address.

        Args:
            email (str): The email of the employee to retrieve.

        Returns:
            Optional[EmployeeOutputSchema]: The serialized employee data or None
            if not found.
        """
        try:
            employee = await self.repository.get_employee_by_email(email)
            if not employee:
                return None

            return EmployeeOutputSchema.validate(employee)
        except Exception as e:
            raise Exception(
                f"Failed EmployeeGetService().get_by_email(): {e}") from e

    async def get_by_role(self, role: str) -> List[EmployeeOutputSchema]:
        """
        Retrieve employees by their role.

        Args:
            role (str): The role to filter employees by.

        Returns:
            List[EmployeeOutputSchema]: A list of serialized employees with the
            specified role.
        """
        try:
            employees = await self.repository.get_employees_by_role(role)
            if not employees:
                return None

            return [EmployeeOutputSchema.validate(employee) for employee in employees]
        except Exception as e:
            raise Exception(
                f"Failed EmployeeGetService().get_by_role(): {e}") from e
