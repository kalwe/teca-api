from typing import Optional
from app.core.repositories.shared.get_repository import GetRepository
from app.core.repositories.shared.update_repository import UpdateRepository
from app.core.services.shared.get_service import GetService


class UpdateService[T]():
    def __init__(self, repository: UpdateRepository[T]):
        """
        Initialize the service with the provided repository.

        Args:
            repository (Type[UpdateRepository[T]]): The repository
            class used for data update.
        """
        self.repository = repository
        self.get_service = GetService(GetRepository(repository.model_class))

    async def update_data(self, id, record) -> Optional[T]:
        try:
            record_exist = self.get_service.get_by_id(id)
            if not record_exist:
                return None

            self.repository.model_class = record
            updated_record = await self.repository.update_record()
            if not updated_record:
                return None

            return updated_record
        except Exception as e:
            raise Exception(
                f"Failed UpdateService.update_record(): {e}") from e
