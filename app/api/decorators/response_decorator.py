from functools import wraps
from http import HTTPStatus
from app.common.responses.enum import ResponseStatus
from app.common.responses.response_strategy import ErrorResponseStrategy, UnifiedResponseStrategy


class ApiResponseDecorator:
    """
    Decorator to standardize API responses with specific formatting strategies.
    """

    STRATEGY_MAP = {
        ResponseStatus.SUCCESS: UnifiedResponseStrategy(),
        ResponseStatus.FAIL: UnifiedResponseStrategy(),
        ResponseStatus.ERROR: ErrorResponseStrategy(),
    }

    @staticmethod
    def standardize_response(handler_function):
        """
        Wraps API handler functions to ensure standardized response formatting and exception handling.
        Uses the Strategy pattern for formatting the response.
        """
        @wraps(handler_function)
        async def wrapper(*args, **kwargs):
            # Determine which strategy to use based on the HTTP status code
            response_data, response_message, status_code = await handler_function(*args, **kwargs)
            status = ApiResponseDecorator.get_response_status(status_code)

            strategy = ApiResponseDecorator.STRATEGY_MAP.get(status)
            return strategy.create_response(handler_function, *args, **kwargs), status_code

        return wrapper

    @staticmethod
    def get_response_status(status_code):
        """
        Determine the response status type based on the HTTP status code.
        """
        if status_code in range(HTTPStatus.OK, HTTPStatus.MULTIPLE_CHOICES):
            return ResponseStatus.SUCCESS
        if status_code in range(
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.INTERNAL_SERVER_ERROR
        ):
            return ResponseStatus.FAIL
        return ResponseStatus.ERROR
