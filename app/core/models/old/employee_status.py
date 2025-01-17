from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel
from app.core.models.enums import EmploymentStatus

class EmployeeStatus(EmployeeRelatedModel):
    """
    Model to manage the current status of an employee.
    """
    current_status = fields.CharEnumField(
        EmploymentStatus,
        description="Current employment status"
    )

    def __str__(self):
        return f"Status of {self.employee.full_name}: {self.current_status.value}"

    @classmethod
    async def get_status(cls, employee_id: int) -> "EmployeeStatus":
        """
        Retrieves the current employment status for an employee.
        Args:
            employee_id (int): The ID of the employee.
        Returns:
            EmployeeStatus: The current employment status of the employee.
        """
        return await cls.get(employee_id=employee_id)
