from app.core.models.vacancy_model import Vacancy
from app.core.repositories.shared.update_repository import UpdateRepository


class VacancyUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Vacancy())
