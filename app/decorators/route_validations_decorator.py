from functools import wraps
from quart import request
from http import HTTPStatus
from app.common.validation_helpers import validate_schema
from app.common.response_helpers import create_error_response

# DEPRECATED


def validate_input(schema_class):
    """
    DEPRECATED
    Decorator to validate route input against a schema.

    :param schema_class: Marshmallow schema class for validation.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            data = await request.get_json()
            validated_data, errors = validate_schema(schema_class, data)
            if errors:
                return errors
            return await func(*args, **kwargs, data=validated_data)
        return wrapper
    return decorator


def handle_route_errors(func):
    """
    Decorator to handle errors in route handlers.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as error:
            return create_error_response(
                HTTPStatus.INTERNAL_SERVER_ERROR, f"Unexpected error: {
                    str(error)}"
            )
    return wrapper
