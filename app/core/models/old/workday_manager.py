from tortoise import fields
from datetime import timedelta

from app.core.models.shared.base_model import BaseModel
from app.core.models.employee_related import EmployeeRelatedModel


class WorkdayState:
    """
    Abstract base class for different workday states.
    """

    def handle(self, workday: 'Workday') -> None:
        raise NotImplementedError(
            "Each state must implement the 'handle' method.")


class WorkingState(WorkdayState):
    """
    Represents the state when the workday is in progress.
    """

    def handle(self, workday: 'Workday') -> None:
        # Increment workday by 8 hours (standard workday duration)
        workday.total_hours_worked += timedelta(hours=8)
        workday.state = CompletedState()  # Transition to completed state


class CompletedState(WorkdayState):
    """
    Represents the state when the workday is completed.
    """

    def handle(self, workday: 'Workday') -> None:
        # No action needed for completed workdays
        workday.total_hours_worked += timedelta(hours=0)


class Workday(EmployeeRelatedModel):
    """
    Represents a workday for an employee, including the state management
    and total hours worked.
    This model will utilize WorkSchedule for standard working hours.
    """
    work_schedule = fields.ForeignKeyField(
        "models.WorkSchedule",
        related_name="workdays"
    )
    total_hours_worked = fields.DurationField(
        default=timedelta()
    )
    state = fields.CharField(
        max_length=100,
        default="working"
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state_mapping = {
            "working": WorkingState(),
            "completed": CompletedState(),
        }
        self._state = self.state_mapping.get(self.state, WorkingState())

    def complete_workday(self) -> None:
        """
        Completes the current workday and transitions to the 'completed' state.
        """
        self._state.handle(self)
        self.save()

    def calculate_overtime(self) -> timedelta:
        """
        Calculate overtime by comparing total worked hours and scheduled hours.
        """
        if self.total_hours_worked > self.work_schedule.total_scheduled_hours:
            return self.total_hours_worked - self.work_schedule.total_scheduled_hours
        return timedelta()

    def __str__(self):
        return f"Workday for {self.employee.full_name} - Total Hours Worked: {self.total_hours_worked}"


class WorkSchedule(BaseModel):
    """
    Represents the standard work schedule, including start time, end time, and break duration.
    This schedule defines the expected working hours for employees.
    """
    start_time = fields.TimeField(
        description="Standard start time of the workday"
    )
    end_time = fields.TimeField(
        description="Standard end time of the workday"
    )
    break_duration = fields.TimeField(
        description="Duration of the break during the workday"
    )

    @property
    def total_scheduled_hours(self) -> timedelta:
        """
        Calculate the total scheduled work hours based on start time,
        end time, and break duration.
        """
        work_duration = timedelta(
            hours=self.end_time.hour,
            minutes=self.end_time.minute
        ) - \
            timedelta(
            hours=self.start_time.hour,
            minutes=self.start_time.minute
        )
        return work_duration - timedelta(
            hours=self.break_duration.hour,
            minutes=self.break_duration.minute
        )

    def __str__(self):
        return f"Work schedule from {self.start_time} to {self.end_time}"


"""Explicações e Melhorias

    Estados do Workday: Os estados WorkingState e CompletedState continuam com o padrão de transição de estado (State Pattern). Quando o dia de trabalho é completado, a transição para o estado "completed" ocorre automaticamente.

    Cálculo de Overtime: A função calculate_overtime compara as horas trabalhadas com as horas programadas na WorkSchedule e calcula as horas extras (overtime), se houver.

    Propriedade total_scheduled_hours: A WorkSchedule agora tem um método total_scheduled_hours, que calcula as horas de trabalho programadas com base no horário de início, término e a duração do intervalo.

    Workday agora depende de WorkSchedule: A classe Workday agora tem uma referência a WorkSchedule, permitindo calcular as horas de trabalho esperadas e as horas extras de forma mais clara e reutilizável.

    __str__ e Melhoria de Legibilidade: O método __str__ foi adicionado tanto em Workday quanto em WorkSchedule para uma melhor legibilidade e para fornecer informações detalhadas sobre o estado do objeto.

Conclusões e Benefícios

    Desacoplamento: A classe Workday agora depende de WorkSchedule para calcular os horários de trabalho, o que facilita a manutenção e a escalabilidade.
    Extensibilidade: A abordagem com o padrão de projeto de State Pattern torna fácil adicionar novos estados de trabalho no futuro (por exemplo, "on_break", "paused", etc.).
    Leitura e Manutenção: O código agora está mais claro, com funções específicas e bem nomeadas. Isso facilita a manutenção e a adição de novas funcionalidades, como cálculo de horas extras ou integração com outros sistemas de gestão de tempo.
    """
