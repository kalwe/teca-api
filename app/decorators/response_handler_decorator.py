from functools import wraps
from app.common.custom_exceptions import CustomValidationError
from app.common.response_handler import ResponseHandler
from http import HTTPStatus

class ResponseHandlerDecorator:
    """Decorator class for handling standardized API responses."""

    @staticmethod
    def handle(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                data, message, status_code = await func(*args, **kwargs)
                response = ResponseHandler.process_response(data, message, status_code)
                return response, status_code

            except CustomValidationError as validation_error:
                return ResponseHandler.create_error_response(
                    HTTPStatus.BAD_REQUEST, str(validation_error)
                ), HTTPStatus.BAD_REQUEST

            except Exception as general_error:
                return ResponseHandler.create_error_response(
                    HTTPStatus.INTERNAL_SERVER_ERROR, str(general_error)
                ), HTTPStatus.INTERNAL_SERVER_ERROR

        return wrapper
