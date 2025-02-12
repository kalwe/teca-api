from typing import Optional

from app.api.schemas.employee_schema import EmployeeInputSchema, EmployeeOutputSchema
from app.core.repositories.employee.employee_create_repository import (
    EmployeeCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class EmployeeCreateService(CreateService):
    """
    Service for managing employee-related business logic.
    Handles creation of new employees with role assignment and password hashing.
    """

    def __init__(self, repository: EmployeeCreateRepository):
        """
        Initialize the service with a repository for employee operations.

        Args:
            repository (EmployeeCreateRepository): An instance of
                EmployeeCreateRepository
                to handle data persistence for the Employee model.
        """
        super().__init__(repository)
        # self._get_service = EmployeeGetService(EmployeeGetRepository(Employee()))

    async def create(
        self,
        employee_data: EmployeeInputSchema,
    ) -> Optional[EmployeeOutputSchema]:
        (
            """
        Create a new employee with additional business logic.

        Args:
            name (str): The name of the employee.
            email (str): The email of the employee.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the employee.

        Returns:
            EmployeeOutputSchema: Serialized data of the created employee.

        Raises:
            EmployeeAlreadyExistsException: If a employee with the given email
            already exists.
        """
            """
        Create a new employee with additional business logic.

        Args:
            name (str): The name of the employee.
            email (str): The email of the employee.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the employee.

        Returns:
            EmployeeOutputSchema: Serialized data of the created employee.

        Raises:
            EmployeeAlreadyExistsException: If a employee with the given email
            already exists.
        """
        )
        created_employee = await self.create_record(employee_data)
        return EmployeeOutputSchema().validate(created_employee)


# FIXME: AttributeError: 'dict' object has no attribute '_saved_in_db'
