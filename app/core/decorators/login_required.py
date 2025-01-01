from functools import wraps
from flask import request, jsonify

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return jsonify({"message": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return decorated_view
