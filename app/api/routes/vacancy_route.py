from app.api.controllers.vacancy_controller import VacancyController
from app.api.routes import vacancy_bp

# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

vacancy_bp.add_url_rule(
    '/',
    view_func=VacancyController.create_vacancy,
    methods=["POST"]
)

vacancy_bp.add_url_rule(
    '/<int:id>',
    view_func=VacancyController.get_vacancy,
    methods=["GET"]
)

vacancy_bp.add_url_rule(
    "/", view_func=VacancyController.get_all_vacancies, methods=["GET"]
)

vacancy_bp.add_url_rule(
    '/<int:id>',
    view_func=VacancyController.update_vacancy,
    methods=["POST"]
)

vacancy_bp.add_url_rule(
    '/<int:id>',
    view_func=VacancyController.delete_vacancy,
    methods=["DELETE"]
)
