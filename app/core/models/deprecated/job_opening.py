from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class JobOpening(BaseModel):
    """
    Model to represent a job opening within the company.
    """
    job_position = fields.CharField(
        max_length=255,
        description="The title of the job position that is currently open"
    )
    department_name = fields.CharField(
        max_length=100,
        description="The department where the job position is located"
    )
    available_positions = fields.IntField(
        description="The number of available positions for this job"
    )
    application_deadline = fields.DateField(
        description="The last date applicants can submit their applications"
    )

    def __str__(self):
        return f"Opening for {self.job_position} in {self.department_name}, {self.available_positions} positions"
