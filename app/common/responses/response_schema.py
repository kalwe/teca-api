from http import HTTPStatus
from typing import Dict, List, Optional
from pydantic import BaseSchema, Field

from app.common.base_schema import BaseSchema
from app.common.responses.enums import ResponseStatus
from app.common.responses.response_types import BodySchemaType, DataBodyType


class BaseResponse(BaseSchema):
    """
    Schema representing a response result with body and HTTP code.

    Attributes:
        body (Dict[str, Any]): JSON-serializable body of the response.
        status (HTTPStatus): HTTP status code of the response.
        headers (Optional[Dict[str, str]]): Optional headers for the response.
        content_type (Optional[str]): Content type of the response, defaults to "application/json".
    """
    body: DataBodyType
    status: HTTPStatus = Field(
        ...,
        description="The HTTP status code of the response.")
    headers: Optional[Dict[str, str]] = Field(
        None,
        description="Optional headers to include in the response.")
    content_type: Optional[str] = Field(
        "application/json",
        description="The content type default is 'application/json'.")

    class Config:
        use_enum_values = True  # Serialize Enums as their values


class BodySuccessSchema(BaseSchema):
    """
    Schema for a successful response.

    Attributes:
        status (ResponseStatus): The status of the response, typically "success".
        message (str): A descriptive message for the response.
        data (Dict[str, Any]): A dictionary containing the response data payload.
    """
    status: ResponseStatus
    message: str
    data: DataBodyType

    class Config:
        use_enum_values = True  # Serialize Enums as their values


class ErrorDetailSchema(BaseSchema):
    """
    Schema for individual error details.

    Attributes:
        message (str): A descriptive message about the error.
        details (str): Additional details explaining the error.
    """
    message: str
    details: str


class BodyErrorSchema(BaseSchema):
    """
    Schema for an error response.

    Attributes:
        error (List[ErrorDetailSchema]): A list of error details.
    """
    error: List[ErrorDetailSchema]


class BodySchema(BodySchemaType):
    """
    Represents a generic body schema type, inheriting from BodySchemaType.
    """
    pass


class ResponseSchema(BaseResponse):
    """
    Represents a standardized API response that can contain either a generic
    response schema or an error response schema.

    Attributes:
        body (BodySchemaType): The main body of the response, which can
            either be a successful response or an error.
    """
    body: BodySchemaType = Field(
        ...,
        description="The main body of the response.")


class ResultSchema(BaseSchema):
    """
    Schema for the result extracted from a controller.

    Attributes:
        data (Dict[str, Any]): The data returned by the controller.
        http_code (HTTPStatus): The HTTP status code associated with the result.
    """
    data: DataBodyType
    http_code: HTTPStatus
