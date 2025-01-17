from app.core.models.user_model import User
from app.core.repositories.shared.update_repository import UpdateRepository


class UserUpdateRepository(UpdateRepository[User]):
    def __init__(self, model: type[User]):
        super().__init__(model)
