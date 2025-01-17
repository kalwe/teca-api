from typing import Generic, Type, TypeVar


T = TypeVar("T")


class CreateRepository(Generic[T]):
    """
    Abstract repository that defines common database operations.
    """

    def __init__(self, model: Type[T]):
        self.model = model

    async def create_record(self, **fields_data) -> T:
        """
        Create a new record in the database.

        Args:
            **fields_data: The data to create the record with.

        Returns:
            T: The created record.
        """
        record = await self.model.create(**fields_data)
        return record
