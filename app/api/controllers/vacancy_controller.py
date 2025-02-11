from http import HTTPStatus
from typing import List

from quart_schema import validate_request, validate_response

from app.api.schemas.vacancy_schema import (
    VacancyDeletedSchema,
    VacancyInputSchema,
    VacancyOutputSchema,
)
from app.core.repositories.vacancy.vacancy_create_repository import (
    VacancyCreateRepository,
)
from app.core.repositories.vacancy.vacancy_delete_repository import (
    VacancyDeleteRepository,
)
from app.core.repositories.vacancy.vacancy_get_repository import VacancyGetRepository
from app.core.repositories.vacancy.vacancy_update_repository import (
    VacancyUpdateRepository,
)
from app.core.services.vacancy.vacancy_create_service import VacancyCreateService
from app.core.services.vacancy.vacancy_delete_service import VacancyDeleteService
from app.core.services.vacancy.vacancy_get_service import VacancyGetService
from app.core.services.vacancy.vacancy_update_service import VacancyUpdateService
from quart_schema import tag

class VacancyController:
    """
    Controller that handles vacancy-related HTTP requests.
    """

    @staticmethod
    @validate_request(VacancyInputSchema)
    @validate_response(VacancyOutputSchema)
    @tag(["Vacancy"])
    async def create_vacancy(data: VacancyInputSchema) -> VacancyOutputSchema:
        """
        Creates a new vacancy from the incoming JSON data.

        Returns:
            Tuple: A tuple containing the vacancy data and the
            HTTP status code.
        """
        repository = VacancyCreateRepository()
        service = VacancyCreateService(repository)
        vacancy = await service.create(data)
        return vacancy, HTTPStatus.CREATED

    @staticmethod
    @validate_response(VacancyOutputSchema)
    @tag(["Vacancy"])
    async def get_vacancy(id: int) -> VacancyOutputSchema:
        """
        Retrieves a vacancy by ID.

        Args:
            id (str): The ID of the vacancy to retrieve.

        Returns:
            Tuple: A tuple containing the vacancy data (or an error message)
            and the HTTP status code.
        """
        repository = VacancyGetRepository()
        service = VacancyGetService(repository)
        vacancy = await service.get(id)
        return vacancy, HTTPStatus.OK

    @staticmethod
    @validate_response(List[VacancyOutputSchema])
    @tag(["Vacancy"])
    async def get_all_vacancies() -> List[VacancyOutputSchema]:
        """
        Retrieves all vacancies using FetchHelper to standardize
        error handling.

        Returns:
            Tuple: A tuple containing the list of vacancies
            (or an error message)
            and the HTTP status code.
        """
        repository = VacancyGetRepository()
        service = VacancyGetService(repository)
        vacancies = await service.get_all()
        return vacancies, HTTPStatus.OK

    @staticmethod
    @validate_request(VacancyInputSchema)
    @validate_response(VacancyOutputSchema)
    @tag(["Vacancy"])
    async def update_vacancy(id: int, data: VacancyInputSchema) -> VacancyOutputSchema:
        repository = VacancyUpdateRepository()
        service = VacancyUpdateService(repository)
        vacancy = await service.update(id, data)
        return vacancy, HTTPStatus.OK

    @staticmethod
    @validate_response(VacancyDeletedSchema)
    @tag(["Vacancy"])
    async def delete_vacancy(id: int) -> VacancyDeletedSchema:
        repository = VacancyDeleteRepository()
        service = VacancyDeleteService(repository)
        vacancy = await service.delete(id)
        return vacancy, HTTPStatus.NO_CONTENT
