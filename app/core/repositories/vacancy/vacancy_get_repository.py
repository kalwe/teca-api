from typing import Optional
from app.common.custom_exceptions import RepositoryError
from app.core.models.vacancy_model import Vacancy
from app.core.repositories.shared.get_repository import GetRepository


class VacancyGetRepository(GetRepository):
    def __init__(self):
        """
        Initialize the repository with the Vacancy model_class.

        Args:
            model_class ([Vacancy): The Vacancy model_class class to be managed by
            the repository.
        """
        super().__init__(Vacancy())


    async def get_vacancy_by_name(self, name) -> Optional[Vacancy]:
        """
        Retrieve a record by its name if it is active.

        Args:
            record_name (str): The name of the record to retrieve.

        Returns:
            Optional[Vacancy]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(name, is_active=True)

            return record
        except Exception as e:
            raise RepositoryError(
                f"Failed VacancyGetRepository.get_vacancy_by_name: {e}") from e
