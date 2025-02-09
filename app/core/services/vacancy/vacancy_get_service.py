from typing import List, Optional

from app.api.schemas.vacancy_schema import VacancyOutputSchema
from app.core.repositories.vacancy.vacancy_get_repository import VacancyGetRepository
from app.core.services.shared.get_service import GetService


class VacancyGetService(GetService):
    """
    Service for managing vacancy-related business logic, leveraging generic
    methods from GetService.

    This service adds vacancy-specific business logic on top of the generic
    functionality provided by GetService.
    """

    def __init__(self, repository: VacancyGetRepository):
        """
        Initialize the service with a Vacancy-specific repository.

        Args:
            repository (VacancyGetRepository): Repository for vacancy
            data retrieval.
        """
        super().__init__(repository)
        self._get_repository = repository

    async def get(self, id: int) -> Optional[VacancyOutputSchema]:
        vacancy = self.get_by_id(id)
        return VacancyOutputSchema.validate(vacancy)

    async def get_all(
        self, filters: Optional[dict] = None
    ) -> Optional[List[VacancyOutputSchema]]:
        vacancies = await self.get_all_records(filters)
        return [VacancyOutputSchema.validate(vacancy) for vacancy in vacancies]

    async def get_by_name(self, name: str) -> Optional[VacancyOutputSchema]:
        vacancy = self._get_repository.get_vacancy_by_name(name)
        return VacancyOutputSchema.validate(vacancy)
