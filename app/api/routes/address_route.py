from app.api.controllers.address_controller import AddressController
from app.api.routes import address_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

address_bp.add_url_rule(
    '/',
    view_func=AddressController.create_address,
    methods=["POST"]
)

address_bp.add_url_rule(
    '/<int:id>',
    view_func=AddressController.get_address,
    methods=["GET"]
)

address_bp.add_url_rule(
    '/',
    view_func=AddressController.get_all_addresss,
    methods=["GET"]
)

address_bp.add_url_rule(
    '/<int:id>',
    view_func=AddressController.update_address,
    methods=["POST"]
)

address_bp.add_url_rule(
    '/<int:id>',
    view_func=AddressController.delete_address,
    methods=["DELETE"]
)
