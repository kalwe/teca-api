from app.api.controllers.reminder_controller import ReminderController
from app.api.routes import reminder_bp


# TODO: maybe need use init_routes(bp: Blueprint) -> None:
# and call on init_bp() or __init__.create_app()

reminder_bp.add_url_rule(
    '/',
    view_func=ReminderController.create_reminder,
    methods=["POST"]
)

reminder_bp.add_url_rule(
    '/<int:id>',
    view_func=ReminderController.get_reminder,
    methods=["GET"]
)

reminder_bp.add_url_rule(
    '/',
    view_func=ReminderController.get_all_reminders,
    methods=["GET"]
)

reminder_bp.add_url_rule(
    '/<int:id>',
    view_func=ReminderController.update_reminder,
    methods=["POST"]
)

reminder_bp.add_url_rule(
    '/<int:id>',
    view_func=ReminderController.delete_reminder,
    methods=["DELETE"]
)
