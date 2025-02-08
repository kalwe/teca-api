from app.core.models.roles_model import Role
from app.core.repositories.shared.update_repository import UpdateRepository


class RolesUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Role())
