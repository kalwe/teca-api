from app.core.repositories.user.user_delete_repository import UserDeleteRepository
from app.core.services.shared.delete_service import DeleteService


class DeleteUserService(DeleteService):
    """
    Service for managing user-related business logic.
    """

    def __init__(self):
        super().__init__(UserDeleteRepository)
