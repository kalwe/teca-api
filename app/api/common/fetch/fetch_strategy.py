from typing import Any, List
from app.core.services.interfaces.base_service import BaseService

class FetchStrategy:
    """
    Base interface for fetch strategies.
    """
    async def fetch(self, service: BaseService, *args, **kwargs) -> Any:
        raise NotImplementedError("Implement the 'fetch' method in subclasses.")

class FetchItemStrategy(FetchStrategy):
    """
    Strategy for fetching a single item.
    """
    async def fetch(self, service: BaseService, item_id: int) -> Any:
        item = await service.get(item_id)
        if not item:
            raise ValueError("Item not found.")
        return item


class FetchAllItemsStrategy(FetchStrategy):
    """
    Strategy for fetching all items.
    """
    async def fetch(self, service: BaseService) -> List[Any]:
        items = await service.get_all()
        if not items:
            raise ValueError("No items found.")
        return items
