from app.api.schemas.user_schema import UserInputSchema
from app.core.models.user_model import User
from app.core.repositories.shared.get_repository import GetRepository
from app.core.repositories.shared.update_repository import UpdateRepository


class UserUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(User)
