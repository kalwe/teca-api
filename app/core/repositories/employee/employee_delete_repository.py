from typing import Type, TypeVar
from app.core.models.employee_model import Employee
from app.core.repositories.shared.delete_repository import DeleteRepository

T = TypeVar("T", bound=Employee)


class EmployeeDeleteRepository(DeleteRepository[Employee]):
    """
    Repository for managing employee-related soft deletes.
    """

    def __init__(self, model_class: Type[Employee]):
        """
        Initialize the employee-specific delete repository.
        :param model_class: The Employee class.
        """
        super().__init__(model_class)
