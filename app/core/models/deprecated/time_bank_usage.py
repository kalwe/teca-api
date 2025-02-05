from tortoise import fields
from typing import List, Protocol

from app.core.models.employee_related import EmployeeRelatedModel

class TimeBankObserver(Protocol):
    """ Observer interface for time bank changes. """
    def update(self, hours: float) -> None:
        """ Update method to be called when the time bank changes """
        pass

class TimeBank(EmployeeRelatedModel):
    """
    Model for recording and managing an employee's time bank usage.
    """
    hours_used = fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        description="Hours used from the time bank"
        )
    remaining_balance = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        description="Remaining balance in the time bank"
        )
    usage_date = fields.DateField(description="Date of the time bank usage")

    observers: List[TimeBankObserver] = []

    def add_observer(self, observer: TimeBankObserver) -> None:
        """ Register an observer to be notified of changes """
        self.observers.append(observer)

    def remove_observer(self, observer: TimeBankObserver) -> None:
        """ Remove an observer """
        self.observers.remove(observer)

    def update_balance(self) -> None:
        """ Update the remaining balance and notify observers """
        self.remaining_balance -= self.hours_used
        self._notify_observers()

    def _notify_observers(self) -> None:
        """ Notify all observers about the change in balance """
        for observer in self.observers:
            observer.update(self.remaining_balance)

    def __str__(self):
        return f"Time bank usage for {self.employee.full_name} on {self.usage_date}"
