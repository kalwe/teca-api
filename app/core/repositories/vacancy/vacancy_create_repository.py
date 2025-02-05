from app.core.models.vacancy_model import Vacancy
from app.core.repositories.shared.create_repository import CreateRepository


class VacancyCreateRepository(CreateRepository):
    """
    Repository for managing vacancy-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Vacancy model_class.

        Args:
            model_class: The Vacancy model_class class
            to be managed by
            the repository.
        """
        super().__init__(Vacancy())
