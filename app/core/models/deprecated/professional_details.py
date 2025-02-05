from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class ProfessionalDetails(EmployeeRelatedModel):
    """
    Model for storing professional details of an employee.
    """
    job_title = fields.CharField(
        max_length=100,
        description="Job title of the employee"
    )
    department_name = fields.CharField(
        max_length=100,
        description="Name of the department"
    )
    employment_start_date = fields.DateField(
        description="Start date of employment"
    )
    current_salary = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        description="Current salary"
    )

    def __str__(self):
        return f"{self.job_title} - {self.employee.full_name}"
