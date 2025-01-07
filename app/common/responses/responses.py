from http import HTTPStatus
from quart import Response
from typing import Any, Dict, Optional
from quart.wrappers.response import ResponseBody


class ResponseBase(Response):
    """
    Base class for custom responses, extending Quart's Response.

    Attributes:
        response (Optional[ResponseBody]): The body of the response.
        status (Optional[int]): The HTTP status code.
        headers (Optional[Dict[str, str]]): Additional headers for the response.
        content_type (Optional[str]): The MIME type of the response content.
        direct_passthrough (bool): Whether to bypass response body handling.
    """

    def __init__(
        self,
        response: Optional[ResponseBody] = None,
        status: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
        content_type: Optional[str] = None,
        direct_passthrough: bool = False,
    ):
        """
        Initialize the base response.

        Args:
            response (Optional[ResponseBody]): The body of the response.
            status (Optional[int]): The HTTP status code for the response.
            headers (Optional[Dict[str, str]]): Additional headers for the response.
            content_type (Optional[str]): The MIME type of the response content.
            direct_passthrough (bool): Whether to bypass response body handling.
        """
        super().__init__(
            response=response,
            status=status,
            headers=headers,
            content_type=content_type,
            direct_passthrough=direct_passthrough,
        )


class DefaultResponse(ResponseBase):
    """
    Class for successful JSON responses, extending ResponseBase.

    Attributes:
        data_response (Dict[str, Any]): The response data payload.
        status (Optional[int]): The HTTP status code.
        headers (Optional[Dict[str, str]]): Additional headers for the response.
        content_type (Optional[str]): The MIME type of the response content.
    """

    def __init__(
        self,
        data_response: Dict[str, Any],
        status: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
        content_type: Optional[str] = "application/json",
    ):
        """
        Initialize a default JSON response.

        Args:
            data_response (Dict[str, Any]): The response data payload.
            status (Optional[int]): The HTTP status code for the response.
            headers (Optional[Dict[str, str]]): Additional headers for the response.
            content_type (Optional[str]): The MIME type of the response content.
        """
        super().__init__(
            response=data_response,
            status=status,
            headers=headers,
            content_type=content_type,
        )


class ErrorResponse(ResponseBase):
    """
    Class for error JSON responses, extending ResponseBase.

    Attributes:
        error_response (Dict[str, Any]): The error response payload.
        status (Optional[int]): The HTTP status code.
        headers (Optional[Dict[str, str]]): Additional headers for the response.
        content_type (Optional[str]): The MIME type of the response content.
    """

    def __init__(
        self,
        error_response: Dict[str, Any],
        status: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
        content_type: Optional[str] = "application/json",
    ):
        """
        Initialize an error JSON response.

        Args:
            error_response (Dict[str, Any]): The error response payload.
            status (Optional[int]): The HTTP status code for the response.
            headers (Optional[Dict[str, str]]): Additional headers for the response.
            content_type (Optional[str]): The MIME type of the response content.
        """
        super().__init__(
            response=error_response,
            status=status,
            headers=headers,
            content_type=content_type,
        )
