from app.core.models.user_model import User
from app.core.repositories.shared.delete_repository import DeleteRepository


class UserDeleteRepository(DeleteRepository):
    def __init__(self):
        super().__init__(User)
