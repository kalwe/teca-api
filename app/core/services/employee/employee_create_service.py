from typing import List, Optional, TypeVar
from app.api.schemas.employee_schema import EmployeeOutputSchema, EmployeeInputSchema
from app.common.hash_utils import hash_password
from app.common.custom_exceptions import EmployeeAlreadyExistsException
from app.core.models.employee_model import Employee
from app.core.repositories.employee.employee_create_repository import (
    EmployeeCreateRepository)
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.services.shared.create_service import CreateService
from app.core.services.employee.employee_get_service import EmployeeGetService


class EmployeeCreateService(CreateService[Employee]):
    """
    Service for managing employee-related business logic.
    Handles creation of new employees with role assignment and password hashing.
    """

    def __init__(self, repository: EmployeeCreateRepository):
        """
        Initialize the service with a repository for employee operations.

        Args:
            repository (EmployeeCreateRepository): An instance of EmployeeCreateRepository
                to handle data persistence for the Employee model.
        """
        super().__init__(repository)
        self.get_service = EmployeeGetService(
            EmployeeGetRepository(Employee()))

    async def create(self, employee: Employee) -> Optional[EmployeeOutputSchema]:
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
            EmployeeAlreadyExistsException: If a employee with the given email already exists.
        """        """
        Create a new employee with additional business logic.

        Args:
            name (str): The name of the employee.
            email (str): The email of the employee.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the employee.

        Returns:
            EmployeeOutputSchema: Serialized data of the created employee.

        Raises:
            EmployeeAlreadyExistsException: If a employee with the given email already exists.
        """
        roles = employee.roles or [
            "employee"]  # Assign default role if none provided

        try:
            # Check if a employee with the email already exists
            existing_employee = await self.get_service.get_by_email(
                employee.email
            )
            if existing_employee:
                raise EmployeeAlreadyExistsException(
                    f"Employee with email {employee.email} already exists."
                )

            password_hash = hash_password(employee.password_hash)

            created_employee = await self.create_record(
                name=employee.name,
                email=employee.email,
                password_hash=password_hash,
                roles=roles
            )
            return EmployeeOutputSchema().validate(created_employee)
        except Exception as e:
            raise Exception(
                f"Failed EmployeeCreateService().create(): {e}") from e
