from app.api.controllers.user_controller import UserController
from app.api.routes import user_bp

# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

user_bp.add_url_rule(
    '/',
    view_func=UserController.create_user,
    methods=["POST"]
)

user_bp.add_url_rule(
    '/<int:id>',
    view_func=UserController.get_user,
    methods=["GET"]
)

user_bp.add_url_rule(
    '/',
    view_func=UserController.get_all_users,
    methods=["GET"]
)

user_bp.add_url_rule(
    '/<int:id>',
    view_func=UserController.update_user,
    methods=["POST"]
)

user_bp.add_url_rule(
    '/<int:id>',
    view_func=UserController.delete_user,
    methods=["DELETE"]
)
