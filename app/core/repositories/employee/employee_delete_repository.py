from app.core.models.employee_model import Employee
from app.core.repositories.shared.delete_repository import DeleteRepository


class EmployeeDeleteRepository(DeleteRepository):
    """
    Repository for managing employee-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the employee-specific delete repository.
        :param model_class: The Employee class.
        """
        super().__init__(Employee())
