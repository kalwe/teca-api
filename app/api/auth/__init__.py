from quart import Blueprint, request, jsonify
from app.api.auth.services import AuthService
from app.api.auth.schemas import LoginSchema, RegisterSchema
from app.api.auth.decorators import login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
async def register():
    data = await request.get_json()
    schema = RegisterSchema(**data)
    user = await AuthService.register_user(schema.email, schema.password)
    return jsonify({"message": f"User {user.email} created successfully."}), 201

@auth_bp.route('/login', methods=['POST'])
async def login():
    data = await request.get_json()
    schema = LoginSchema(**data)
    tokens = await AuthService.login_user(schema.email, schema.password)
    return jsonify(tokens), 200

@auth_bp.route('/protected', methods=['GET'])
@login_required
async def protected():
    return jsonify({"message": "You have access to this protected resource."}), 200
