from typing import Optional

from app.api.schemas.vacancy_schema import VacancyInputSchema, VacancyOutputSchema
from app.core.repositories.vacancy.vacancy_create_repository import (
    VacancyCreateRepository,
)
from app.core.services.shared.create_service import CreateService


class VacancyCreateService(CreateService):
    """
    Service for managing vacancy-related business logic.
    Handles creation of new vacancies with role assignment and password hashing.
    """

    def __init__(self, repository: VacancyCreateRepository):
        """
        Initialize the service with a repository for vacancy operations.

        Args:
            repository (VacancyCreateRepository): An instance of
                VacancyCreateRepository
                to handle data persistence for the Vacancy model.
        """
        super().__init__(repository)

    async def create(
        self,
        vacancy_data: VacancyInputSchema,
    ) -> Optional[VacancyOutputSchema]:
        (
            """
        Create a new vacancy with additional business logic.

        Args:
            name (str): The name of the vacancy.
            email (str): The email of the vacancy.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the vacancy.

        Returns:
            VacancyOutputSchema: Serialized data of the created vacancy.

        Raises:
            VacancyAlreadyExistsException: If a vacancy with the given email
            already exists.
        """
            """
        Create a new vacancy with additional business logic.

        Args:
            name (str): The name of the vacancy.
            email (str): The email of the vacancy.
            password (str): The plain-text password to be hashed.
            roles (Optional[List[str]]): List of roles to assign to the vacancy.

        Returns:
            VacancyOutputSchema: Serialized data of the created vacancy.

        Raises:
            VacancyAlreadyExistsException: If a vacancy with the given email
            already exists.
        """
        )
        created_vacancy = await self.create_record(vacancy_data)
        return VacancyOutputSchema().validate(created_vacancy)


# FIXME: pydantic_core._pydantic_core.ValidationError: 7 validation errors for VacancyOutputSchema
