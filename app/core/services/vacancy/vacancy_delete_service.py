from typing import Optional

from app.api.schemas.base_schema import DeletedSchema
from app.api.schemas.vacancy_schema import VacancyOutputSchema
from app.core.repositories.vacancy.vacancy_delete_repository import (
    VacancyDeleteRepository,
)
from app.core.services.shared.delete_service import DeleteService


class VacancyDeleteService(DeleteService):
    """
    Service for managing vacancy-related delete business logic.
    """

    def __init__(self, repository: VacancyDeleteRepository):
        """
        Initialize the vacancy delete service.
        :param repository: The vacancy delete repository instance.
        """
        super().__init__(repository)

    async def delete(self, id: int) -> Optional[VacancyOutputSchema]:
        """
        Delete a vacancy by ID.
        :param id: The ID of the vacancy to delete.
        :return: The deleted vacancy as a schema, or None if not found.
        """
        deleted_vacancy = await self.soft_delete(id)
        return DeletedSchema().validate(deleted_vacancy)
