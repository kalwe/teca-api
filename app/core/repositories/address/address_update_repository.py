from app.core.models.address_model import Address
from app.core.repositories.shared.update_repository import UpdateRepository


class AddressUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Address)
