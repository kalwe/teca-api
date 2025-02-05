from app.core.models.bank_account_model import Bank_account
from app.core.repositories.shared.delete_repository import DeleteRepository


class Bank_accountDeleteRepository(DeleteRepository):
    """
    Repository for managing bank_account-related soft deletes.
    """

    def __init__(self):
        """
        Initialize the bank_account-specific delete repository.
        :param model_class: The Bank_account class.
        """
        super().__init__(Bank_account())
