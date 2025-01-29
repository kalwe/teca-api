from typing import Optional

from app.core.models.shared.base_model import BaseModel


class CreateRepository:
    """
    Abstract repository class providing common database operations for a
    specified model_class type.

    This generic repository is designed to operate with models that
    follow an asynchronous
    interface, typically seen in frameworks such as Tortoise ORM or
    similar libraries. It
    provides a standardized way to handle data persistence, ensuring
    a consistent interface
    for creating records in the database.

    Attributes:
        model_class (T): The model_class class associated with
        the repository.
        This model_class class
            should support asynchronous methods like `create`.

    Methods:
        create_record(**fields_data):
            Asynchronously create and persist a new record in the database
            using the provided
            field data.
    """

    def __init__(self, model_class: ):
        """
        Initialize the repository with a specific model_class class.

        Args:
            model_class (T): The model_class class to be managed by
            the repository.
        """
        self.model_class = model_class

    async def create_record[T: BaseModel](self, fields_data: T) -> Optional[T]:
        """
        Create a new record in the database.

        This method uses the `create` method of the associated model_class
        to persist
        a new record in the database. The field data provided as keyword
        arguments
        should match the fields defined in the model_class schema.

        Args:
            **fields_data: Arbitrary keyword arguments representing the
            field data
                required to create a new record. The keys should correspond to
                model_class field names.

        Returns:
            T: An instance of the created model_class, representing
            the newly persisted
            record in the database.

        Raises:
            ValueError: If the provided field data does not match the
            model_class schema.
            Exception: Any exception raised by the model_class's
            `create` method.
        """
        try:
            created_record = await self.model_class.create(**fields_data)
            return created_record
        except Exception as e:
            raise Exception(
                f"Failed CreateRepository().create_record(): {e}") from e
