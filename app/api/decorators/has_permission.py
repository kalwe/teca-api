from functools import wraps
from quart import jsonify

def has_permission(permission):
    def decorator(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            # Lógica de verificação de permissão
            if not check_user_permission(permission):
                return jsonify({"message": "Forbidden"}), 403
            return func(*args, **kwargs)
        return decorated_view
    return decorator
