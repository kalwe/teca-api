from typing import List, Optional, Type, TypeVar
from app.core.models.employee_model import Employee
from app.core.repositories.shared.get_repository import GetRepository

T = TypeVar("T", bound=Employee)


class EmployeeGetRepository(GetRepository[Employee]):
    def __init__(self, model_class: Type[Employee]):
        """
        Initialize the repository with the Employee model_class.

        Args:
            model_class (type[Employee]): The Employee model_class class to be managed by
            the repository.
        """
        super().__init__(model_class)

    # async def get_employee_by_email(
    #     self,
    #     email: str
    # ) -> Optional[Employee]:
    #     """
    #     Retrieve a employee by their email address.

    #     Args:
    #         email (str): The email of the employee to retrieve.

    #     Returns:
    #         Optional[Employee]: The serialized employee data or None if not found.
    #     """
    #     try:
    #         employee = await self.get_all_records(email=email)
    #         if not employee:
    #             return None

    #         return employee
    #     except Exception as e:
    #         raise Exception(
    #             f"Failed repository get_employee_by_email(): {e}") from e

    # async def get_employees_by_role(self, role: str) -> List[Employee]:
    #     """
    #     Fetch employees by their role and return serialized data.

    #     Args:
    #         role (str): The role to filter employees by.

    #     Returns:
    #         List[Employee]: A list of serialized employees with the specified role.
    #     """
    #     try:
    #         employees = await self.get_all_records(roles__contains=[role])
    #         if not employees:
    #             return None

    #         return employees
    #     except Exception as e:
    #         raise Exception(
    #             f"Failed repository get_employees_by_role(): {e}") from e
