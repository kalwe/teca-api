from functools import wraps
from quart import jsonify

def validate_input(schema):
    """
    Decorator for validating input data using the provided schema.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Assume the first argument is the input data
            input_data = args[0]
            # Validate the data and respond with error if invalid
            validation_errors = schema.validate(input_data)
            if validation_errors:
                return jsonify({"message": "Invalid input", "errors": validation_errors}), 400
            return func(*args, **kwargs)
        return wrapper
    return decorator
