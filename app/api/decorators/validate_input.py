from functools import wraps
from flask import jsonify

def validate_input(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = args[0]  # Supondo que o primeiro argumento seja os dados
            if not schema.validate(data):
                return jsonify({"message": "Invalid input"}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator
