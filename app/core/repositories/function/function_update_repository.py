from app.core.models.function_model import Function
from app.core.repositories.shared.update_repository import UpdateRepository


class FunctionUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Function)
