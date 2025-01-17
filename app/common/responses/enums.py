from enum import Enum
from http import HTTPStatus


class ResponseStatus(Enum):
    """
    Enum representing response statuses for API responses.

    Attributes:
        SUCCESS (str): Indicates a successful response.
        FAILURE (str): Indicates a failed response.
        NOT_FOUND (str): Indicates a resource was not found.
        ERROR (str): Indicates an error response.
    """
    SUCCESS = "success"
    FAILURE = "failure"
    NOT_FOUND = "not_found"
    ERROR = "error"


class ResponseMessages(Enum):
    """
    Enum mapping HTTP status codes to user-friendly messages.

    Attributes:
        CREATED_SUCCESS (tuple): Represents HTTP 201 (Created) with a success
            message.
        FETCHED_SUCCESS (tuple): Represents HTTP 200 (OK) with a success
            message.
        INVALID_INPUT (tuple): Represents HTTP 400 (Bad Request)
            with an error message.
        INTERNAL_SERVER_ERROR (tuple): Represents HTTP 500
            (Internal Server Error) with an error message.
        ITEM_NOT_FOUND (tuple): Represents HTTP 404
            (Not Found) with an error message.
    """
    CREATED_SUCCESS = (HTTPStatus.CREATED, "Item successfully created.")
    FETCHED_SUCCESS = (HTTPStatus.OK, "Successfully fetched the item(s).")
    INVALID_INPUT = (HTTPStatus.BAD_REQUEST, "Invalid input.")
    INTERNAL_SERVER_ERROR = (
        HTTPStatus.INTERNAL_SERVER_ERROR, "An unexpected error occurred.")
    ITEM_NOT_FOUND = (HTTPStatus.NOT_FOUND, "Item not found.")

    def __new__(cls, http_code: HTTPStatus, message: str):
        """
        Creates a new enum member with additional attributes.

        Args:
            http_code (HTTPStatus): The HTTP status code for the response.
            message (str): The user-friendly message for the status code.

        Returns:
            ResponseMessages: An instance of the ResponseMessages enum.
        """
        obj = object.__new__(cls)
        obj._value_ = http_code
        obj.http_code = http_code
        obj.message = message
        return obj

    @classmethod
    def get_message_for_status(cls, http_code: HTTPStatus) -> str:
        """
        Retrieves the appropriate message for a given HTTP status code.

        Args:
            http_code (HTTPStatus): The HTTP status code.

        Returns:
            str: A user-friendly message corresponding to the status code.
        """
        for response_message in cls:
            if response_message.http_code == http_code:
                return response_message.message
        return cls.INTERNAL_SERVER_ERROR.message
