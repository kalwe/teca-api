from app.api.controllers.clothing_controller import ClothingController
from app.api.routes import clothing_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

clothing_bp.add_url_rule(
    '/',
    view_func=ClothingController.create_clothing,
    methods=["POST"]
)

clothing_bp.add_url_rule(
    '/<int:id>',
    view_func=ClothingController.get_clothing,
    methods=["GET"]
)

clothing_bp.add_url_rule(
    '/',
    view_func=ClothingController.get_all_clothings,
    methods=["GET"]
)

clothing_bp.add_url_rule(
    '/<int:id>',
    view_func=ClothingController.update_clothing,
    methods=["POST"]
)

clothing_bp.add_url_rule(
    '/<int:id>',
    view_func=ClothingController.delete_clothing,
    methods=["DELETE"]
)
