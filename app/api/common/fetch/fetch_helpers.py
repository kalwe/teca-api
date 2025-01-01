from typing import Any, List
from app.core.services.interfaces.base_service import BaseService

class FetchHelper:
    @staticmethod
    async def fetch_item(service: BaseService, item_id: int) -> Any:
        """
        Fetches a single item by its ID.

        Args:
            service (object): The service responsible for retrieving data.
            item_id (str): The ID of the item to fetch.

        Returns:
            dict: The item if found.

        Raises:
            ValueError: If the item is not found.
            Exception: For other errors.
        """
        try:
            item = await service.get(item_id)
            if item is None:
                raise ValueError("Item not found")
            return item
        except Exception as e:
            raise RuntimeError(f"Error fetching item: {str(e)}")

    @staticmethod
    async def fetch_all_items(service: BaseService) -> List[Any]:
        """
        Fetches all items.

        Args:
            service (object): The service responsible for retrieving data.

        Returns:
            list: The list of items.

        Raises:
            ValueError: If no items are found.
            Exception: For other errors.
        """
        try:
            items = await service.get_all()

            if not items:
                raise ValueError("No items found")
            return items
        except Exception as e:
            raise RuntimeError(f"Error fetching items: {str(e)}")
