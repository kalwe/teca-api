from tortoise import fields

from app.core.models.shared.base_entity import BaseEntity


class EmployeeResume(BaseEntity):
    """
    Model to represent a comprehensive summary of an employee's key information.
    """
    employment_status = fields.CharField(
        max_length=100,
        description="Current employment status (e.g., Active, On Leave)"
    )
    current_job_title = fields.CharField(
        max_length=255,
        description="The current job title held by the employee"
    )
    last_alert_type = fields.CharField(
        max_length=255,
        description="The most recent type of alert received by the employee"
    )

    def __str__(self):
        return f"Resume for {self.employee.full_name}: {self.current_job_title} - {self.employment_status}"

    def generate_summary(self) -> str:
        """
        Generate a comprehensive summary of the employee's status and job.
        """
        return f"{self.employee.full_name} - {self.current_job_title}, Status: {self.employment_status}"
