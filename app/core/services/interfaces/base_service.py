from abc import ABC, abstractmethod
from typing import Any, List, Optional

class BaseService(ABC):
    """
    Abstract base class defining the interface for service implementations.
    """

    @abstractmethod
    async def get(self, item_id: int) -> Optional[Any]:
        """
        Retrieve a single item by its ID.

        Args:
            item_id (str): The ID of the item to fetch.

        Returns:
            Optional[Any]: The item if found, or None.
        """
        pass


    @abstractmethod
    async def get_all(self) -> List[Any]:
        """
        Retrieve all items.

        Returns:
            List[Any]: A list of all items.
        """
        pass
