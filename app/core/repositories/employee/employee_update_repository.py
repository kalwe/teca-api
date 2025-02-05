from app.api.schemas.employee_schema import EmployeeInputSchema
from app.core.models.employee_model import Employee
from app.core.repositories.shared.update_repository import UpdateRepository


class EmployeeUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Employee)
