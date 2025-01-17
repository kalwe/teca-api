from app.core.models.user_model import User
from app.core.services.shared.get_service import GetService


class UserGetService(GetService[User]):
    """
    Service for managing user-related business logic.
    """

    def __init__(self, repository):
        super().__init__(repository)
