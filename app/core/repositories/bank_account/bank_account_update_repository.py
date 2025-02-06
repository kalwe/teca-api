from app.core.models.bank_account_model import Bank_account
from app.core.repositories.shared.update_repository import UpdateRepository


class Bank_accountUpdateRepository(UpdateRepository):
    def __init__(self):
        super().__init__(Bank_account)
