from typing import Union
from pydantic_core import ErrorDetails
from app.common.responses.response_schema import (
    BodyErrorSchema, ErrorDetailSchema)

from app.common.responses.response_types import ErrorDetailsType


class ErrorResponseFactory:
    """
    A factory class for creating error response details.
    """

    @staticmethod
    def create_error_details(
            errors: ErrorDetailsType,
            default_message=None) -> list[ErrorDetailSchema]:
        """
        Generates a list of error details from the provided
        errors or exception.

        Args:
            errors (list or Exception): A list of error objects
            or a single exception.
            default_message (str, optional): A default message
            if none is provided in the error. Defaults to None.

        Returns:
            list[ErrorDetailSchema]: A list of standardized error details.
        """
        if isinstance(errors, list[ErrorDetails]):
            return [
                ErrorDetailSchema(
                    message=err.get("msg", default_message),
                    details=str(err))
                for err in errors
            ]
        elif isinstance(errors, Exception):
            return [
                ErrorDetailSchema(
                    # TODO: avoid this: "An unexpected error occurred."
                    message=default_message or "An unexpected error occurred.",
                    details=str(errors))
            ]
        else:
            raise ValueError("Invalid input for error details creation.")

    @staticmethod
    def create_error_body(
            errors: ErrorDetailsType,
            default_message: str) -> BodyErrorSchema:
        """
        Creates an error body schema.

        Args:
            errors (list[ErrorDetails] or Exception): The errors or exception to include.
            default_message (str): Default error message.

        Returns:
            BodyErrorSchema: A standardized error body schema.
        """
        error_details = ErrorResponseFactory.create_error_details(
            errors=errors,
            default_message=default_message)
        return BodyErrorSchema(error=error_details)
