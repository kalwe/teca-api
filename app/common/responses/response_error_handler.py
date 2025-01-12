from http import HTTPStatus
from pydantic import ValidationError

from app.common.responses.enums import ResponseMessages
from app.common.responses.factories.response_error_factory import (
    ErrorResponseFactory)
from app.common.responses.response_handler import ResponseHandler
from app.common.responses.response_schema import ResponseSchema


class ResponseErrorHandler:
    @staticmethod
    def create_validation_error_response(e: ValidationError) -> ResponseSchema:
        """
        Creates a standardized response for validation errors.

        Args:
            e (ValidationError): The validation error.

        Returns:
            ResponseSchema: A standardized error validation response.
        """
        body_error = ErrorResponseFactory.create_error_body(
            e.errors(),
            default_message="Validation failed.")
        return ResponseHandler.create_response(
            body=body_error,
            status=HTTPStatus.BAD_REQUEST,
            headers=None,
            content_type=None)

    @staticmethod
    def create_generic_error_response(e: Exception) -> ResponseSchema:
        """
        Creates a standardized response for generic exceptions.

        Args:
            e (Exception): The exception.

        Returns:
            ResponseSchema: A standardized error response.
        """
        http_code = HTTPStatus.INTERNAL_SERVER_ERROR
        body_error = (ErrorResponseFactory.create_error_body(
            e,
            default_message=ResponseMessages.get_message_for_status(
                http_code)))
        return ResponseHandler.create_response(
            body=body_error,
            status=http_code,
            headers=None,
            content_type=None)
