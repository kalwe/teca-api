from app.api.controllers.roles_controller import RolesController
from app.api.routes import roles_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

roles_bp.add_url_rule(
    '/',
    view_func=RolesController.create_roles,
    methods=["POST"]
)

roles_bp.add_url_rule(
    '/<int:id>',
    view_func=RolesController.get_roles,
    methods=["GET"]
)

roles_bp.add_url_rule(
    '/',
    view_func=RolesController.get_all_roless,
    methods=["GET"]
)

roles_bp.add_url_rule(
    '/<int:id>',
    view_func=RolesController.update_roles,
    methods=["POST"]
)

roles_bp.add_url_rule(
    '/<int:id>',
    view_func=RolesController.delete_roles,
    methods=["DELETE"]
)
