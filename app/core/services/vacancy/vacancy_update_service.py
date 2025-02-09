from typing import Optional

from app.api.schemas.vacancy_schema import VacancyInputSchema, VacancyOutputSchema
from app.core.repositories.vacancy.vacancy_update_repository import (
    VacancyUpdateRepository,
)
from app.core.services.shared.update_service import UpdateService


class VacancyUpdateService(UpdateService):
    """
    Service for managing vacancy-related business logic.
    """

    def __init__(self, repository: VacancyUpdateRepository):
        super().__init__(repository)

    async def update(
        self, id: int, vacancy_data: VacancyInputSchema
    ) -> Optional[VacancyOutputSchema]:
        updated_vacancy = await self.update_data(id, vacancy_data)
        return VacancyOutputSchema.validate(updated_vacancy)
