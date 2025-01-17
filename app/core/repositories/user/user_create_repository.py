from app.api.auth.user_model import User
from app.core.repositories.shared.create_repository import CreateRepository


class UserCreateRepository(CreateRepository[User]):
    pass
