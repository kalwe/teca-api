from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class EmployeeDocumentation(EmployeeRelatedModel):
    """
    Model for storing documentation related to an employee.
    """
    document_type = fields.CharField(
        max_length=100,
        description="Type of document (e.g., contract, certificate)"
    )
    document_path = fields.CharField(
        max_length=255,
        description="Path or URL to the document file"
    )

    def __str__(self):
        return f"{self.document_type} - {self.employee.full_name}"
