from app.core.models.contact_model import Contact
from app.core.repositories.shared.update_repository import UpdateRepository


class ContactUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Contact())
