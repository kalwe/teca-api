from typing import Type, TypeVar
from app.core.models.employee_model import Employee
from app.core.repositories.shared.create_repository import CreateRepository

T = TypeVar("T", bound=Employee)


class EmployeeCreateRepository(CreateRepository[Employee]):
    """
    Repository for managing employee-related create .
    """

    def __init__(self, model_class: Type[Employee]):
        """
        Initialize the repository with the Employee model_class.

        Args:
            model_class: The Employee model_class class
            to be managed by
            the repository.
        """
        super().__init__(model_class)
