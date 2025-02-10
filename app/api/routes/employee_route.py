from app.api.controllers.employee_controller import EmployeeController
from app.api.routes import employee_bp
from app.api.routes.base_route import BaseRoute
from quart import Blueprint

class EmployeeRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, EmployeeController, 'employee', 'employees')

EmployeeRoute(employee_bp)
