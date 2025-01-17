from enum import Enum

class EmploymentStatus(Enum):
    """
    Enum to represent the employment status of an employee.
    """
    ACTIVE = "Active"
    ON_LEAVE = "On Leave"
    TERMINATED = "Terminated"
