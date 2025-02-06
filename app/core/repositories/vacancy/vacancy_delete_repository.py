from app.core.models.vacancy_model import Vacancy
from app.core.repositories.shared.delete_repository import DeleteRepository


class VacancyDeleteRepository(DeleteRepository):
    """
    Repository for managing vacancy-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the vacancy-specific delete repository.
        :param model_class: The Vacancy class.
        """
        super().__init__(Vacancy())
