from app.api.controllers.bank_account_controller import BankAccountController
from app.api.routes import bank_account_bp
from app.api.routes.base_route import BaseRoute
from quart.blueprints import Blueprint

class BankAccountRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, BankAccountController, 'bank_account', 'bank_accounts')

BankAccountRoute(bank_account_bp)
