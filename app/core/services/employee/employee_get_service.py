from typing import List, Optional

from app.api.schemas.employee_schema import EmployeeOutputSchema
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.services.shared.get_service import GetService


class EmployeeGetService(GetService):
    """
    Service for managing employee-related business logic, leveraging generic
    methods from GetService.

    This service adds employee-specific business logic on top of the generic
    functionality provided by GetService.
    """

    # Override the type for specialization
    # repository = EmployeeGetRepository

    def __init__(self, repository: EmployeeGetRepository):
        """
        Initialize the service with a Employee-specific repository.

        Args:
            repository (EmployeeGetRepository): Repository for employee
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[EmployeeOutputSchema]:
        employee = await self.get_by_id(id)
        return EmployeeOutputSchema.validate(employee)

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[EmployeeOutputSchema]]:
        employees = await self.get_all_records(filters)
        return [EmployeeOutputSchema.validate(employee) for employee in employees]

    async def get_by_name(self, name: str) -> Optional[EmployeeOutputSchema]:
        employee = await self._get_repository.get_employee_by_name(name)
        return EmployeeOutputSchema.validate(employee)
