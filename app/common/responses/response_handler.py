from http import HTTPStatus
from typing import Any, Dict, Optional, Tuple, Union

from pydantic import ValidationError
from pydantic_core import ErrorDetails

from app.common.responses.enums import ResponseMessages, ResponseStatus
from app.common.responses.response_schema import (
    BodyErrorSchema,
    BodySuccessSchema,
    ErrorDetailSchema,
    ResponseSchema,
    ResultSchema,
)
from app.common.responses.response_types import BodySchemaType


class ResponseHandler:
    """
    Handles the creation of standardized response objects.

    Methods:
        create_response: Creates a success or error response based on the provided schema.
        create_success_response: Creates a success response.
        create_validation_error_response: Creates a response for validation errors.
        create_generic_error_response: Creates a response for generic exceptions.
        extract_result: Extracts and validates the body and HTTP status from a controller result.
    """

    @staticmethod
    def create_response(
        body: BodySchemaType,
        status: HTTPStatus,
        headers: Optional[Dict[str, str]] = None,
        content_type: Optional[str] = None,
    ) -> ResponseSchema:
        """
        Creates a response object using the appropriate schema.

        Args:
            body (BodySchemaType): The schema instance for the response body.
            status (HTTPStatus): The HTTP status code for the response.
            headers (Optional[Dict[str, str]]): Additional headers to include in the response.
            content_type (Optional[str]): The content type of the response.

        Returns:
            ResponseSchema: A validated response object.
        """
        return ResponseSchema(
            body=body,
            status=status,
            headers=headers,
            content_type=content_type,
        )

    @staticmethod
    def create_success_response(
        data: Dict[str, Any],
        http_code: HTTPStatus,
    ) -> ResponseSchema:
        """
        Creates a standardized success response.

        Args:
            data (Dict[str, Any]): The data payload for the response.
            http_code (HTTPStatus): The HTTP status code for the response.

        Returns:
            ResponseSchema: A standardized success response.
        """
        body = BodySuccessSchema(
            status=ResponseStatus.SUCCESS,
            message=ResponseMessages.get_message_for_status(http_code),
            data=data,
        )
        return ResponseHandler.create_response(
            body=body,
            status=http_code,
            headers=None,
            content_type=None,
        )

    @staticmethod
    def create_error_details(
        errors,
        default_message=None
    ) -> list[ErrorDetailSchema]:
        """
        Generates a list of error details from the
        provided errors or exception.

        Args:
            errors (list or Exception): A list of error objects or a single exception.
            default_message (str, optional): A default message if none is provided in the error. Defaults to None.

        Returns:
            list[ErrorDetailSchema]: A list of standardized error details.
        """
        if isinstance(errors, list[ErrorDetails]):
            return [
                ErrorDetailSchema(
                    message=err.get("msg", default_message),
                    details=str(err),
                )
                for err in errors
            ]
        elif isinstance(errors, Exception):
            return [
                ErrorDetailSchema(
                    message=default_message or "An unexpected error occurred.",
                    details=str(errors),
                )
            ]
        else:
            raise ValueError("Invalid input for error details creation.")

    @staticmethod
    def create_validation_error_response(e: ValidationError) -> ResponseSchema:
        """
        Creates a standardized response for validation errors.

        Args:
            e (ValidationError): The validation error.

        Returns:
            ResponseSchema: A standardized error validation response.
        """
        # error_details_unused = [
        #     ErrorDetailSchema(
        #         message=err["msg"],
        #         details=str(err),
        #     )
        #     for err in e.errors()
        # ]
        error_details = ResponseHandler.create_error_details(
            e.errors(),
            default_message="Validation failed.",
        )
        body_error = BodyErrorSchema(error=error_details)
        return ResponseHandler.create_response(
            body=body_error,
            status=HTTPStatus.BAD_REQUEST,
            headers=None,
            content_type=None,
        )

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

        error_details = ResponseHandler.create_error_details(
            e,
            ResponseMessages.get_message_for_status(http_code),
        )
        body_error = BodyErrorSchema(error=error_details)
        return ResponseHandler.create_response(
            body=body_error,
            status=http_code,
            headers=None,
            content_type=None,
        )

    @staticmethod
    def extract_result(
        result: Union[Any, Tuple[Any, int]]
    ) -> Tuple[Dict[str, Any], HTTPStatus]:
        """
        Extracts and validates the body and HTTP status from a controller result.

        Args:
            result (Union[Any, Tuple[Any, int]]): The result returned by the controller.

        Returns:
            Tuple[Dict[str, Any], HTTPStatus]: A tuple containing the body and HTTP status code.

        Raises:
            ValueError: If the result does not match the expected schema.
        """
        try:
            if isinstance(result, Tuple) and len(result) == 2:
                data, http_code = result
            else:
                data, http_code = result, HTTPStatus.OK

            validated = ResultSchema(data=data, http_code=http_code)
            return validated.data, HTTPStatus(validated.http_code)

        except ValidationError as e:
            raise ValueError(f"Invalid result schema: {e}")
