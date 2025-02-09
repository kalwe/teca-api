

class RepositoryError(Exception):
    pass

# DEPRECATED
# class CustomValidationError(Exception):
#     """
#     Custom exception for validation errors in API requests.
#     Provides a standardized structure for error handling and response.
#     """

#     def __init__(
#         self,
#         message=ResponseMessages.INVALID_INPUT,
#         http_code: int = HTTPStatus.BAD_REQUEST,
#         details: Optional[Any] = None
#     ):
#         """
#         Initialize the CustomValidationError.

#         Args:
#             message (Union[str, dict]): The error message or a dictionary of error details.
#             http_code (int): The HTTP status code associated with the error.
#             details (Optional[Any]): Additional error details for debugging or logging.
#         """
#         self.message = message
#         self.http_code = http_code
#         self.details = details
#         super().__init__(self.message)

#     # def to_dict(self) -> dict:
#     #     """
#     #     Convert the exception to a dictionary for standardized API responses.

#     #     Returns:
#     #         dict: A dictionary representation of the exception.
#     #     """
#     #     error_response = {
#     #         "error": "ValidationError",
#     #         "message": self.message,
#     #         "http_code": self.http_code,
#     #     }
#     #     if self.details:
#     #         error_response["details"] = self.details
#     #     return error_response


class UserAlreadyExistsException(Exception):
    """
    Exception raised when attempting to create a user that already exists.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str = "User already exists."):
        """
        Initialize the exception with an optional custom message.

        Args:
            message (str): Custom error message. Defaults to "User already exists."
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """
        Return the string representation of the exception.

        Returns:
            str: The error message.
        """
        return self.message


class UserNotFoundException(Exception):
    """
    Exception raised when attempting to create a user that already exists.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message: str = "User already exists."):
        """
        Initialize the exception with an optional custom message.

        Args:
            message (str): Custom error message. Defaults to "User already exists."
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """
        Return the string representation of the exception.

        Returns:
            str: The error message.
        """
        return self.message
