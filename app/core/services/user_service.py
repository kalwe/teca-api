from app.core.repositories.user_respository import UserRepository
from app.core.validators.user_validator import UserValidator


class UserService:
    """
    Service for managing user-related business logic.
    """

    def __init__(self):
        self.user_repository = UserRepository()
        self.user_validator = UserValidator()

    def create(self, data):
        self.user_validator.validate_user(data)
        return self.user_repository.create_user(data)

    def get(self, id):
        return self.user_repository.get_by_id(id)

    def get_all(self):
        return self.user_repository.get_all()
