from app.api.controllers.bank_account_controller import BankAccountController
from app.api.routes import bank_account_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

bank_account_bp.add_url_rule(
    '/',
    view_func=BankAccountController.create_bank_account,
    methods=["POST"]
)

bank_account_bp.add_url_rule(
    '/<int:id>',
    view_func=BankAccountController.get_bank_account,
    methods=["GET"]
)

bank_account_bp.add_url_rule(
    '/',
    view_func=BankAccountController.get_all_bank_accounts,
    methods=["GET"]
)

bank_account_bp.add_url_rule(
    '/<int:id>',
    view_func=BankAccountController.update_bank_account,
    methods=["POST"]
)

bank_account_bp.add_url_rule(
    '/<int:id>',
    view_func=BankAccountController.delete_bank_account,
    methods=["DELETE"]
)
