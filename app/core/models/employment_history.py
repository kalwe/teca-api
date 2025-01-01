from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class EmploymentHistory(EmployeeRelatedModel):
    """
    Model to record significant events and changes in an employee's employment.
    """
    change_description = fields.TextField(description="Description of the change or event")

    def __str__(self):
        return f"History for {self.employee.full_name} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
