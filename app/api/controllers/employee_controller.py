from http import HTTPStatus
from typing import List

from quart_schema import validate_request, validate_response

from app.api.schemas.employee_schema import (
    EmployeeDeletedSchema,
    EmployeeInputSchema,
    EmployeeOutputSchema,
)
from app.core.repositories.employee.employee_create_repository import (
    EmployeeCreateRepository,
)
from app.core.repositories.employee.employee_delete_repository import (
    EmployeeDeleteRepository,
)
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.repositories.employee.employee_update_repository import (
    EmployeeUpdateRepository,
)
from app.core.services.employee.employee_create_service import EmployeeCreateService
from app.core.services.employee.employee_delete_service import EmployeeDeleteService
from app.core.services.employee.employee_get_service import EmployeeGetService
from app.core.services.employee.employee_update_service import EmployeeUpdateService


class EmployeeController:
    """
    Controller that handles employee-related HTTP requests.
    """

    @staticmethod
    @validate_request(EmployeeInputSchema)
    @validate_response(EmployeeOutputSchema)
    async def create_employee(
        data: EmployeeInputSchema
    ) -> EmployeeOutputSchema:
        """
        Creates a new employee from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the employee data and the
            HTTP status code.
        """
        repository = EmployeeCreateRepository()
        service = EmployeeCreateService(repository)
        employee = await service.create(data)
        return employee, HTTPStatus.CREATED

    @staticmethod
    @validate_response(EmployeeOutputSchema)
    async def get_employee(id: int):
        """
        Retrieves a employee by ID.

        Args:
            id (str): The ID of the employee to retrieve.

        Returns:
            Tuple: A tuple containing the employee data (or an error message)
            and the HTTP status code.
        """
        service = EmployeeGetService(EmployeeGetRepository())
        employee = service.get(id)
        return employee, HTTPStatus.OK

    @staticmethod
    @validate_response(List[EmployeeOutputSchema])
    async def get_all_employees():
        """
        Retrieves all employees using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of employees
            (or an error message)
            and the HTTP status code.
        """
        service = EmployeeGetService(EmployeeGetRepository())
        employees = service.get_all()
        return employees, HTTPStatus.OK

    @staticmethod
    @validate_request(EmployeeInputSchema)
    @validate_response(EmployeeOutputSchema)
    async def update_employee(id: int, data: EmployeeInputSchema):
        repository = EmployeeUpdateRepository()
        service = EmployeeUpdateService(repository)
        employee = service.update(id, data)
        return employee, HTTPStatus.OK

    @staticmethod
    @validate_response(EmployeeDeletedSchema)
    async def delete_employee(id: int):
        repository = EmployeeDeleteRepository()
        service = EmployeeDeleteService(repository)
        employee = service.delete(id)
        return employee, HTTPStatus.NO_CONTENT
