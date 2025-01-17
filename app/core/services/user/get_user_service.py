from app.core.repositories.user.user_get_repository import UserGetRepository
from app.core.services.shared.get_service import GetService


class UserGetService():
    """
    Service for managing user-related business logic.
    """

    def __init__(self):
        self.repository = UserGetRepository()
