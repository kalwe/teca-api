from typing import Type, TypeVar
from app.core.models.user_model import UserModel
from app.core.repositories.shared.update_repository import UpdateRepository

T = TypeVar("T", bound=UserModel)


class UserUpdateRepository(UpdateRepository[UserModel]):
    def __init__(self, model_class: Type[UserModel]):
        super().__init__(model_class)
