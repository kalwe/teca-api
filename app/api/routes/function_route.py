from app.api.controllers.function_controller import FunctionController
from app.api.routes import function_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

function_bp.add_url_rule(
    '/',
    view_func=FunctionController.create_function,
    methods=["POST"]
)

function_bp.add_url_rule(
    '/<int:id>',
    view_func=FunctionController.get_function,
    methods=["GET"]
)

function_bp.add_url_rule(
    '/',
    view_func=FunctionController.get_all_functions,
    methods=["GET"]
)

function_bp.add_url_rule(
    '/<int:id>',
    view_func=FunctionController.update_function,
    methods=["POST"]
)

function_bp.add_url_rule(
    '/<int:id>',
    view_func=FunctionController.delete_function,
    methods=["DELETE"]
)
