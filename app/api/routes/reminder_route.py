from app.api.controllers.reminder_controller import ReminderController
from app.api.routes import reminder_bp
from app.api.routes.base_route import BaseRoute
from quart import Blueprint

class ReminderRoute(BaseRoute):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, ReminderController, 'reminder', 'reminders')

ReminderRoute(reminder_bp)
