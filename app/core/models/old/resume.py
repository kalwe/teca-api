from tortoise import fields

from app.core.models.shared.base_model import BaseModel


class Resume(BaseModel):
    """
    Model for storing resumes of job candidates.
    """
    applicant_name = fields.CharField(
        max_length=255,
        description="Name of the applicant"
    )
    desired_position = fields.CharField(
        max_length=100,
        description="Position the applicant is applying for"
    )
    experience = fields.TextField(
        description="Summary of the applicant's experience"
    )
    resume_file_path = fields.CharField(
        max_length=255,
        description="Path to the resume file"
    )
    submission_date = fields.DatetimeField(
        auto_now_add=True,
        description="Date when the resume was submitted"
    )

    def __str__(self):
        return f"Resume of {self.applicant_name} for {self.desired_position}"
