from typing import Any, Generic, List, TypeVar
from app.core.services.shared.get_service import GetService

T = TypeVar("T")


class FetchStrategy(Generic[T]):
    """
    Base interface for fetch strategies.

    This class provides a template for strategies that fetch data
    using a specific `BaseService`. Subclasses must implement the `fetch`
    method to define their specific behavior.

    Attributes:
        T (TypeVar): The type of data expected to be fetched by the strategy.
    """

    async def fetch(self, service: GetService, *args, **kwargs) -> Any:
        """
        Fetch data using the given service.

        This method must be implemented in subclasses to define the specific
        logic for fetching data.

        Args:
            service (BaseService): The service used to fetch data.
            *args: Positional arguments for the fetch logic.
            **kwargs: Keyword arguments for the fetch logic.

        Returns:
            Any: The fetched data, as defined by the subclass.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError(
            "Implement the 'fetch' method in subclasses.")

    async def _validate_result(self, result: Any, error_message: str) -> T:
        """
        Validate the result, raising an error if it's None or empty.

        This helper method ensures that the fetched result is valid. If the
        result is `None` or empty, it raises a `ValueError` with the provided
        error message.

        Args:
            result (Any): The result to validate.
            error_message (str): The error message to raise if validation fails.

        Returns:
            T: The validated result.

        Raises:
            ValueError: If the result is None or empty.
        """
        if not result:
            raise ValueError(error_message)
        return result


class FetchItemStrategy(FetchStrategy):
    """
    Strategy for fetching a single item.

    This strategy uses the `get` method of the `BaseService` to fetch
    a single item by its ID.

    Methods:
        fetch: Fetches a single item by its ID.
    """

    async def fetch(self, service: GetService, item_id: int) -> Any:
        """
        Fetch a single item by its ID using the provided service.

        Args:
            service (BaseService): The service used to fetch the item.
            item_id (int): The ID of the item to fetch.

        Returns:
            Any: The fetched item.

        Raises:
            ValueError: If the item is not found (result is None).
        """
        item = await service.get(item_id)
        return await self._validate_result(item, "Item not found.")


class FetchAllItemsStrategy(FetchStrategy):
    """
    Strategy for fetching all items.

    This strategy uses the `get_all` method of the `BaseService` to fetch
    all available items.

    Methods:
        fetch: Fetches all items.
    """

    async def fetch(self, service: GetService) -> List[Any]:
        """
        Fetch all items using the provided service.

        Args:
            service (BaseService): The service used to fetch all items.

        Returns:
            List[Any]: A list of fetched items.

        Raises:
            ValueError: If no items are found (result is empty or None).
        """
        items = await service.get_all()
        return await self._validate_result(items, "No items found.")
