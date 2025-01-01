from app.core.repositories.user_repository import UserRepository
from app.core.validators.user_validator import UserValidator

class UserService:
    """
    Service for managing user-related business logic.
    """
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_validator = UserValidator()

    def create_user(self, data):
        self.user_validator.validate_user(data)
        return self.user_repository.create_user(data)

    def get_user(self, user_id):
        return self.user_repository.get_user_by_id(user_id)
