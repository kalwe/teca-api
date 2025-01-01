from functools import wraps
from http import HTTPStatus
from app.common.custom_exceptions import CustomValidationError
from app.common.responses.response_handler import ApiResponseHandler

class ApiResponseStrategy:
    """
    Strategy Pattern: Base strategy class for handling API responses.
    """

    async def create_response(self, handler_function, *args, **kwargs):
        """
        Template Method that handles the flow of calling the handler and formatting the response.
        """
        try:
            response_data, response_message, status_code = await handler_function(*args, **kwargs)
            return self.format_response(response_data, response_message, status_code), status_code

        except CustomValidationError as validation_error:
            # Handle validation exceptions with a custom message
            return self.format_response(
                data=None,
                message=f"Validation Error: {validation_error.message}",
                status_code=HTTPStatus.BAD_REQUEST
            ), HTTPStatus.BAD_REQUEST

        except Exception as unexpected_error:
            # Handle unexpected errors
            return self.format_response(
                data=None,
                message=f"Internal Server Error: {str(unexpected_error)}",
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR
            ), HTTPStatus.INTERNAL_SERVER_ERROR

    def format_response(self, data, message, status_code):
        """
        Abstract method for formatting response, to be implemented by concrete strategies.
        """
        raise NotImplementedError("This method should be implemented by concrete strategies.")

class UnifiedResponseStrategy(ApiResponseStrategy):
    """
    Concrete Strategy for unified success and failure responses.
    """

    def format_response(self, data, message, status_code):
        """
        Format the response using a unified structure for success and failure.
        """
        return ApiResponseHandler.create_response(data, message, status_code)

class ErrorResponseStrategy(ApiResponseStrategy):
    """
    Concrete Strategy for handling error responses.
    """

    def format_response(self, data, message, status_code):
        """
        Format the error response using a specific error structure.
        """
        return {
            "error": {
                "status_code": status_code,
                "message": message,
            }
        }
