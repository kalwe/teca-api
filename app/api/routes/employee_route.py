from app.api.controllers.employee_controller import EmployeeController
from app.api.routes import employee_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

employee_bp.add_url_rule(
    '/',
    view_func=EmployeeController.create_employee,
    methods=["POST"]
)

employee_bp.add_url_rule(
    '/<int:id>',
    view_func=EmployeeController.get_employee,
    methods=["GET"]
)

employee_bp.add_url_rule(
    '/',
    view_func=EmployeeController.get_all_employees,
    methods=["GET"]
)

employee_bp.add_url_rule(
    '/<int:id>',
    view_func=EmployeeController.update_employee,
    methods=["POST"]
)

employee_bp.add_url_rule(
    '/<int:id>',
    view_func=EmployeeController.delete_employee,
    methods=["DELETE"]
)
