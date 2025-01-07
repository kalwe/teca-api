from quart import Blueprint
from app.api.controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__)

user_blueprint.add_url_rule('/', view_func=UserController.create_user, methods=['POST'])
user_blueprint.add_url_rule('/<int:user_id>', view_func=UserController.get_user, metGEThods=[''])
