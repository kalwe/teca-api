from functools import wraps
from app.common.custom_exceptions import CustomValidationError

def handle_service_errors(service_name):
    """
    Decorator to handle exceptions for a given service function.

    :param service_name: Name of the service to include in error messages.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except CustomValidationError as e:
                raise ValueError(f"Validation failed in {service_name}: {str(e)}")
            except Exception as e:
                raise Exception(f"Error in {service_name}: {str(e)}")
        return wrapper
    return decorator
