from typing import Generic, Optional, Type, TypeVar


T = TypeVar("T")


class CreateRepository(Generic[T]):
    """
    Abstract repository class providing common database operations for a
    specified model type.

    This generic repository is designed to operate with models that
    follow an asynchronous
    interface, typically seen in frameworks such as Tortoise ORM or
    similar libraries. It
    provides a standardized way to handle data persistence, ensuring
    a consistent interface
    for creating records in the database.

    Attributes:
        model (Type[T]): The model class associated with the repository.
        This model class
            should support asynchronous methods like `create`.

    Methods:
        create_record(**fields_data):
            Asynchronously create and persist a new record in the database
            using the provided
            field data.
    """

    def __init__(self, model: Type[T]):
        """
        Initialize the repository with a specific model class.

        Args:
            model (Type[T]): The model class to be managed by the repository.
        """
        self.model = model

    async def create_record(self, **fields_data) -> Optional[T]:
        """
        Create a new record in the database.

        This method uses the `create` method of the associated model to persist
        a new record in the database. The field data provided as keyword arguments
        should match the fields defined in the model schema.

        Args:
            **fields_data: Arbitrary keyword arguments representing the field data
                required to create a new record. The keys should correspond to
                model field names.

        Returns:
            T: An instance of the created model, representing the newly persisted
            record in the database.

        Raises:
            ValueError: If the provided field data does not match the model schema.
            Exception: Any exception raised by the model's `create` method.
        """
        try:
            created_record = await self.model.create(**fields_data)
            return created_record
        except Exception as e:
            raise Exception(f"Failed to create record: {e}")
