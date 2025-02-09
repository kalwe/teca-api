from app.api.controllers.contact_controller import ContactController
from app.api.routes import contact_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

contact_bp.add_url_rule(
    '/',
    view_func=ContactController.create_contact,
    methods=["POST"]
)

contact_bp.add_url_rule(
    '/<int:id>',
    view_func=ContactController.get_contact,
    methods=["GET"]
)

contact_bp.add_url_rule(
    '/',
    view_func=ContactController.get_all_contacts,
    methods=["GET"]
)

contact_bp.add_url_rule(
    '/<int:id>',
    view_func=ContactController.update_contact,
    methods=["POST"]
)

contact_bp.add_url_rule(
    '/<int:id>',
    view_func=ContactController.delete_contact,
    methods=["DELETE"]
)
