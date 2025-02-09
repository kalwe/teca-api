from app.api.controllers.vacancy_controller import VacancyController
from app.api.routes import vacancy_bp
from app.api.routes.base_route import BaseRoute
from quart.blueprints import Blueprint

class VacancyRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, VacancyController, 'vacancy', 'vacancies')

VacancyRoute(vacancy_bp)
