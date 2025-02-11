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
from quart_schema import tag

class EmployeeController:
    """
    Controller that handles employee-related HTTP requests.
    """

    @staticmethod
    @validate_request(EmployeeInputSchema)
    @validate_response(EmployeeOutputSchema)
    @tag(["Employee"])
    async def create_employee(data: EmployeeInputSchema) -> EmployeeOutputSchema:
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
    @tag(["Employee"])
    async def get_employee(id: int) -> EmployeeOutputSchema:
        """
        Retrieves a employee by ID.

        Args:
            id (str): The ID of the employee to retrieve.

        Returns:
            Tuple: A tuple containing the employee data (or an error message)
            and the HTTP status code.
        """
        repository = EmployeeGetRepository()
        service = EmployeeGetService(repository)
        employee = await service.get(id)
        return employee, HTTPStatus.OK

    @staticmethod
    @validate_response(List[EmployeeOutputSchema])
    @tag(["Employee"])
    async def get_all_employees() -> List[EmployeeOutputSchema]:
        """
        Retrieves all employees using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of employees
            (or an error message)
            and the HTTP status code.
        """
        repository = EmployeeGetRepository()
        service = EmployeeGetService(repository)
        employees = await service.get_all()
        return employees, HTTPStatus.OK

    @staticmethod
    @validate_request(EmployeeInputSchema)
    @validate_response(EmployeeOutputSchema)
    @tag(["Employee"])
    async def update_employee(
        id: int, data: EmployeeInputSchema
    ) -> EmployeeOutputSchema:
        repository = EmployeeUpdateRepository()
        service = EmployeeUpdateService(repository)
        employee = await service.update(id, data)
        return employee, HTTPStatus.OK

    @staticmethod
    @validate_response(EmployeeDeletedSchema)
    @tag(["Employee"])
    async def delete_employee(id: int) -> EmployeeDeletedSchema:
        repository = EmployeeDeleteRepository()
        service = EmployeeDeleteService(repository)
        employee = await service.delete(id)
        return employee, HTTPStatus.NO_CONTENT
