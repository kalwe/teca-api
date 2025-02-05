from app.core.models.employee_model import Employee
from app.core.repositories.shared.create_repository import CreateRepository


class EmployeeCreateRepository(CreateRepository):
    """
    Repository for managing employee-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Employee model_class.

        Args:
            model_class: The Employee model_class class
            to be managed by
            the repository.
        """
        super().__init__(Employee())
