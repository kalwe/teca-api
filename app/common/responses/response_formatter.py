from abc import ABC, abstractmethod
from http import HTTPStatus
from app.common.responses.enum import ResponseStatus
from app.common.responses.response_model import ApiResponse
from app.common.responses.response_serializer import ApiResponseSerializer


class ResponseFormatter(ABC):
    """
    Abstract base class defining the structure for formatting responses.
    Implements the Template Method pattern.
    """

    def format(self, data=None, message=None, status_code=HTTPStatus.OK):
        """
        Template method that orchestrates response formatting.
        """
        response_status = self.determine_status(status_code)
        return self.build_response(data, message, status_code, response_status)

    @abstractmethod
    def determine_status(self, status_code):
        """Determine the response status based on the HTTP status code."""
        pass

    @abstractmethod
    def build_response(self, data, message, status_code, response_status):
        """Build the response payload."""
        pass


class UnifiedResponseFormatter(ResponseFormatter):
    """
    Formatter for unified success and fail responses.
    """

    HTTP_STATUS_RANGES = {
        ResponseStatus.SUCCESS: range(HTTPStatus.OK, HTTPStatus.MULTIPLE_CHOICES),
        ResponseStatus.FAIL: range(HTTPStatus.BAD_REQUEST, HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS),
    }

    def determine_status(self, status_code):
        """Determine the response status for success or fail."""
        for status, range_ in self.HTTP_STATUS_RANGES.items():
            if status_code in range_:
                return status.value
        return ResponseStatus.ERROR.value

    def build_response(self, data, message, status_code, response_status):
        """Build the success or fail response payload."""
        return ApiResponseSerializer(ApiResponse(
            status=response_status,
            message=message or self.default_message(status_code),
            status_code=status_code,
            data=data
        )).serialize()

    @staticmethod
    def default_message(status_code):
        """Provide default messages based on HTTP status code."""
        messages = {
            HTTPStatus.OK: "Operation completed successfully.",
            HTTPStatus.BAD_REQUEST: "Bad request. Please check your input.",
            HTTPStatus.INTERNAL_SERVER_ERROR: "An unexpected error occurred."
        }
        return messages.get(status_code, "An error occurred.")


class ErrorResponseFormatter(ResponseFormatter):
    """
    Formatter for error responses with a dedicated error structure.
    """

    def determine_status(self, status_code):
        """Errors always return 'error' status."""
        return ResponseStatus.ERROR.value

    def build_response(self, data, message, status_code, response_status):
        """Build the error response payload."""
        return {
            "error": {
                "status_code": status_code,
                "message": message or "An unexpected error occurred.",
            }
        }
