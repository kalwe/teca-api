from typing import Protocol
from tortoise import fields

from app.core.models.employee_related import EmployeeRelatedModel

class OvertimeCalculationStrategy(Protocol):
    """
    A strategy interface to calculate overtime payment.
    """
    def calculate_overtime(self, hours: float, hourly_rate: float) -> float:
        """ Calculate the overtime payment """
        pass

class DefaultOvertimeStrategy(OvertimeCalculationStrategy):
    """
    Default strategy for overtime calculation.
    """
    def calculate_overtime(self, hours: float, hourly_rate: float) -> float:
        return hours * hourly_rate

class Overtime(EmployeeRelatedModel):
    """
    Model to store overtime worked by an employee,
    with flexible calculation strategies.
    """
    overtime_date = fields.DateField(
        description="Date of the overtime worked"
    )
    overtime_hours = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        description="Overtime hours worked"
    )
    department_name = fields.CharField(
        max_length=100,
        description="Department where overtime was worked"
    )
    hourly_rate = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        description="Hourly rate of the employee"
    )

    def calculate_overtime_payment(
        self,
        strategy: OvertimeCalculationStrategy) -> float:
        """
        Calculate overtime payment using a provided strategy.
        """
        return strategy.calculate_overtime(
            self.overtime_hours,
            self.hourly_rate
        )

    def __str__(self):
        return f"Overtime worked by {self.employee.full_name} on {self.overtime_date}"
