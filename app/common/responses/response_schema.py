from http import HTTPStatus
from typing import Dict, List, Optional
from pydantic import Field

from app.common.common_schema import CommonSchema
from app.common.responses.enums import ResponseStatus
from app.common.responses.response_types import BodySchemaType, DictType


class BaseResponse(CommonSchema):
    """
    Schema representing a response result with body and HTTP code.

    Attributes:
        body (Dict[str, Any]): JSON-serializable body of the response.
        status (HTTPStatus): HTTP status code of the response.
        headers (Optional[Dict[str, str]]): Optional headers for the response.
        content_type (Optional[str]): Content type of the response, defaults to "application/json".
    """
    body: DictType
    status: HTTPStatus = Field(
        ...,
        description="The HTTP status code of the response.",
    )
    headers: Optional[Dict[str, str]] = Field(
        None,
        description="Optional headers to include in the response.",
    )
    content_type: Optional[str] = Field(
        "application/json",
        description="The content type default is 'application/json'.",
    )

    class Config:
        use_enum_values = True  # Serialize Enums as their values


class BodySuccessSchema(CommonSchema):
    """
    Schema for a successful response.

    Attributes:
        status (ResponseStatus): The status of the response, typically "success".
        message (str): A descriptive message for the response.
        data (Dict[str, Any]): A dictionary containing the response data payload.
    """
    status: ResponseStatus
    message: str
    data: DictType

    class Config:
        use_enum_values = True  # Serialize Enums as their values


class ErrorDetailSchema(CommonSchema):
    """
    Schema for individual error details.

    Attributes:
        message (str): A descriptive message about the error.
        details (str): Additional details explaining the error.
    """
    message: str = Field(
        ...,
        description="Error message from Exception"
    )
    details: str = Field(
        ...,
        description="Error details from Exception"
    )


class BodyErrorSchema(CommonSchema):
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
        description="The main body(JSON) of the response.",
    )


class ResultSchema(CommonSchema):
    """
    Schema for the result extracted from a controller.

    Attributes:
        data (Dict[str, Any]): The data returned by the controller.
        http_code (HTTPStatus): The HTTP status code associated with the result.
    """
    data: DictType
    http_code: HTTPStatus
