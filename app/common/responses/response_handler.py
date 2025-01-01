from http import HTTPStatus
from app.common.responses.enum import ResponseStatus
from app.common.responses.response_formatter import UnifiedResponseFormatter, ErrorResponseFormatter
from app.common.responses.response_model import ApiResponse


class ApiResponseHandler:
    """
    Entry point for response creation. Utilizes Strategy pattern to delegate response formatting.
    """

    FORMATTERS = {
        ResponseStatus.SUCCESS: UnifiedResponseFormatter(),
        ResponseStatus.FAIL: UnifiedResponseFormatter(),
        ResponseStatus.ERROR: ErrorResponseFormatter(),
    }

    @staticmethod
    def create_response(data=None, message=None, status_code=HTTPStatus.OK):
        """
        Creates a response by selecting the appropriate formatter.
        """
        status = ApiResponseHandler.determine_status_type(status_code)

        # Delegate to the appropriate response formatter (strategy)
        formatter = ApiResponseHandler.FORMATTERS[status]

        if status == ResponseStatus.ERROR:
            return {
                "error": {
                    "status_code": status_code,
                    "message": message or "An unexpected error occurred."
                }
            }

        return formatter.format(data, message, status_code)

    @staticmethod
    def determine_status_type(status_code):
        """
        Determines the type of response formatter to use based on the status code.
        """
        if status_code in range(HTTPStatus.OK, HTTPStatus.MULTIPLE_CHOICES):
            return ResponseStatus.SUCCESS
        if status_code in range(HTTPStatus.BAD_REQUEST, HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS):
            return ResponseStatus.FAIL
        return ResponseStatus.ERROR
