from functools import wraps
from quart import request, jsonify
from app.api.auth.utils import TokenUtils

def login_required(func):
    @wraps(func)
    async def decorated_view(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or not TokenUtils.verify_token(token):
            return jsonify({"message": "Unauthorized"}), 401
        return await func(*args, **kwargs)
    return decorated_view
