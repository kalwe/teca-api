from app.core.models.user_model import User
from app.core.repositories.shared.update_repository import UpdateRepository


class UserUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(User())
