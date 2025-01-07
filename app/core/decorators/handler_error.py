from functools import wraps
from quart import jsonify

def handle_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"message": str(e)}), 500
    return wrapper
