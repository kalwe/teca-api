from app.core.models.user_model import User
from app.core.repositories.shared.update_repository import UpdateRepository


class UserUpdateRepository(UpdateRepository[User]):
    def __init__(self, model_class: User):
        super().__init__(model_class=model_class)
