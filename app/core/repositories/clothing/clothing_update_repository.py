from app.core.models.clothing_model import Clothing
from app.core.repositories.shared.update_repository import UpdateRepository


class ClothingUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Clothing)
