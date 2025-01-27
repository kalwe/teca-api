from typing import Type, TypeVar
from app.core.models.employee_model import Employee
from app.core.repositories.shared.update_repository import UpdateRepository

T = TypeVar("T", bound=Employee)


class EmployeeUpdateRepository(UpdateRepository[Employee]):
    def __init__(self, model_class: Type[Employee]):
        super().__init__(model_class)
