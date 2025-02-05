from app.core.models.bank_account_model import Bank_account
from app.core.repositories.shared.create_repository import CreateRepository


class Bank_accountCreateRepository(CreateRepository):
    """
    Repository for managing bank_account-related create .
    """

    def __init__(self):
        """
        Initialize the repository with the Bank_account model_class.

        Args:
            model_class: The Bank_account model_class class
            to be managed by
            the repository.
        """
        super().__init__(Bank_account())
