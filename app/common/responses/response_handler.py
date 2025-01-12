from http import HTTPStatus
from typing import Dict, Optional, Tuple

from pydantic import ValidationError
from quart import Response, current_app

from app.common.responses.factories.response_factory import ResponseFactory
from app.common.responses.response_schema import (
    ResponseSchema, ResultSchema)
from app.common.responses.response_types import (
    BodySchemaType, DataBodyType, ResultType, ResultReturnType)


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
            content_type: Optional[str] = None) -> ResponseSchema:
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
            content_type=content_type)

    @staticmethod
    def create_success_response(
            data: DataBodyType,
            http_code: HTTPStatus) -> ResponseSchema:
        """
        Creates a standardized success response.

        Args:
            data (DataBodyType): The data payload for the response.
            http_code (HTTPStatus): The HTTP status code for the response.

        Returns:
            ResponseSchema: A standardized success response.
        """
        body = ResponseFactory.create_success_body(
            data=data,
            http_code=http_code)

        # TODO: implements def create() as factory
        return ResponseHandler.create_response(
            body=body,
            status=http_code,
            headers=None,
            content_type=None)

    @staticmethod
    def extract_result(
        result: ResultType
    ) -> ResultReturnType:
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

    @staticmethod
    async def convert_to_response(response_schema: ResponseSchema) -> Response:
        """
        Converts a ResponseSchema object to a Quart Response.

        Args:
            response_schema (ResponseSchema): The standardized response schema.

        Returns:
            Response: A Quart Response instance.
        """
        return await current_app.make_response(
            (response_schema.body.model_dump(), response_schema.status,
             response_schema.headers or {}))
