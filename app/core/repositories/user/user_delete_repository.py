from app.core.models.user_model import User
from app.core.repositories.shared.delete_repository import DeleteRepository


class UserDeleteRepository(DeleteRepository[User]):
    def __init__(self, model: type[User]):
        super().__init__(model)
