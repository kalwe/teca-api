from typing import List, Optional

from tortoise.expressions import Q

from app.common.custom_exceptions import RepositoryError
from app.core.models.shared.base_model import ModelT


class GetRepository:
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model_class: ModelT):
        """
        Initialize the repository with the model class.
        :param model_class: The model class to operate on.
        """
        self._model_class = model_class

    async def get_record_by_id(self, id: int) -> Optional[ModelT]:
        """
        Retrieve a record by its ID if it is active.

        Args:
            record_id (int): The ID of the record to retrieve.

        Returns:
            Optional[TModel]: The retrieved record if found and active,
            otherwise None.
        """
        try:
            record = await self._model_class.get_or_none(id=id, is_active=True)
            return record
        except RepositoryError as e:
            raise RepositoryError(f"Failed to retrieve record by ID {id}: {e}") from e

    async def get_all_records(
        self, filters: Optional[dict] = None
    ) -> Optional[List[ModelT]]:
        """
        Retrieve all records, optionally applying filters.

        Args:
            filters (Optional[dict]): Filters to apply when fetching records.

        Returns:
            List[TModel]: A list of all matching records.
        """
        #        try:
        #            # TODO: fix filter with 'OR', 'AND' / TypeError: object list can't be used in 'await' expression
        #           records = await (self._model_class.filter(filters) if filters
        #                             else await self._model_class.all())
        try:
            if filters:
                q_objects = [Q(**{key: value}) for key, value in filters.items()]
                records = await self._model_class.filter(*q_objects)
            else:
                records = await self._model_class.all()
            return records
        except RepositoryError as e:
            raise RepositoryError(f"Failed GetRepository.get_all_records(): {e}") from e


type GetRepositoryT = GetRepository
