from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class ContactInformation(EmployeeRelatedModel):
    """
    Model to store contact details of an employee.
    """
    phone_number = fields.CharField(
        max_length=15,
        description="Phone number"
    )
    email_address = fields.CharField(
        max_length=255,
        description="Email address"
    )
    physical_address = fields.TextField(
        description="Physical address"
    )

    def __str__(self):
        return f"Contact Information for {self.employee.full_name}"
