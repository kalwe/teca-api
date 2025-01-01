from functools import wraps
from quart import request
from http import HTTPStatus
from app.utils.response import error_response
from app.utils.utils import validate_schema
from tortoise.exceptions import DoesNotExist, ValidationError


def handle_errors(f):
    """
    Capture and treat generic errors on routes
    """
    @wraps(f)
    async def decorated_function(*args, **kwargs):
        try:
            return await f(*args, **kwargs)
        except Exception as e:
            return error_response(f"An error occurred: {str(e)}", HTTPStatus.INTERNAL_SERVER_ERROR)
    return decorated_function

def handle_repository_errors(repo_name):
    """
    A decorator to handle common repository errors for asynchronous functions.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except ValidationError as e:
                raise ValueError(f"Invalid data provided for {repo_name}: {str(e)}")
            except DoesNotExist:
                raise ValueError(f"{repo_name} not found")
            except Exception as e:
                raise Exception(f"Failed to perform operation on {repo_name}: {str(e)}")
        return wrapper
    return decorator

def handle_service_errors(service_name):
    """
    A decorator to handle exceptions for a given service function.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except ValidationError as e:
                raise ValueError(f"Invalid data provided for {service_name}: {str(e)}")
            except DoesNotExist:
                raise ValueError(f"{service_name} not found")
            except Exception as e:
                raise Exception(f"Failed to perform operation on {service_name}: {str(e)}")
        return wrapper
    return decorator
