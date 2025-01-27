from http import HTTPStatus
from typing import List
from quart_schema import validate_request, validate_response

from app.api.schemas.employee_schema import EmployeeInputSchema, EmployeeOutputSchema
from app.core.models.employee_model import Employee
from app.core.repositories.employee.employee_create_repository import EmployeeCreateRepository
from app.core.repositories.employee.employee_delete_repository import EmployeeDeleteRepository
from app.core.repositories.employee.employee_get_repository import EmployeeGetRepository
from app.core.repositories.employee.employee_update_repository import EmployeeUpdateRepository
from app.core.services.employee.employee_create_service import EmployeeCreateService
from app.core.services.employee.employee_delete_service import EmployeeDeleteService
from app.core.services.employee.employee_get_service import EmployeeGetService
from app.core.services.employee.employee_update_service import EmployeeUpdateService
from app.api.routes import api


class EmployeeController:
    """
    Controller that handles employee-related HTTP requests.
    """
    @staticmethod
    @validate_request(EmployeeInputSchema)
    @api.route('/employee', methods=['POST'])
    @validate_response(EmployeeOutputSchema)
    async def create_employee(data: Employee):
        """
        Creates a new employee from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the employee data and the HTTP status code.
        """
        service = EmployeeCreateService(EmployeeCreateRepository(Employee()))
        employee = service.create(data)
        return employee, HTTPStatus.CREATED

    @staticmethod
    @validate_response(EmployeeOutputSchema)
    @api.route('/')
    async def get_employee(id: int):
        """
        Retrieves a employee by ID.

        Args:
            id (str): The ID of the employee to retrieve.

        Returns:
            Tuple: A tuple containing the employee data (or an error message)
            and the HTTP status code.
        """
        service = EmployeeGetService(EmployeeGetRepository(Employee()))
        employee = service.get(id)
        return employee, HTTPStatus.OK

    @staticmethod
    @api.route('/employee', methods=['GET'])
    @validate_response(List[EmployeeOutputSchema])
    async def get_all_employees():
        """
        Retrieves all employees using FetchHelper to standardize error handling.

        Returns:
            Tuple: A tuple containing the list of employees (or an error message) and the HTTP status code.
        """
        service = EmployeeGetService(EmployeeGetRepository(Employee()))
        employees = service.get_all()
        return employees, HTTPStatus.OK

    @staticmethod
    @validate_request(EmployeeInputSchema)
    @api.route('/employee', methods=['POST'])
    @validate_response(EmployeeOutputSchema)
    async def update_employee(id: int, data: Employee):
        service = EmployeeUpdateService(EmployeeUpdateRepository(Employee))
        employee = service.update(id, data)
        return employee, HTTPStatus.OK

    @staticmethod
    @api.route('/employee', methods=['DELETE'])
    async def delete_employee(id: int):
        service = EmployeeDeleteService(EmployeeDeleteRepository(Employee()))
        employee = service.delete(id)
        return employee, HTTPStatus.NO_CONTENT
