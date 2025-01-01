from tortoise import fields

from app.core.models.base_entity import BaseEntity

# TODO: verified is this class is necessary
class PayrollExportRecord(BaseEntity):
    """
    Represents the export of reports for payroll.
    """
    employee = fields.ForeignKeyField(
        "models.Employee",
        related_name="payroll_exports"
    )
    export_date = fields.DateField(
        description="Date of payroll export"
    )
    gross_salary = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        description="Total gross salary"
    )
    deductions = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        description="Total deductions"
    )
    net_salary = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        description="Net salary after deductions"
    )

    def __str__(self) -> str:
        return f"Payroll export for {self.employee.full_name} on {self.export_date}"

    @property
    def has_deductions(self) -> bool:
        """
        Indicates if there are any deductions.
        """
        return self.deductions > 0
