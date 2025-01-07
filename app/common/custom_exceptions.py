from http import HTTPStatus

from app.common.responses_old.response_messages import ResponseMessages


class CustomValidationError(Exception):
    """
    Custom exception for validation errors in API requests.
    """

    def __init__(self, message=ResponseMessages.INVALID_INPUT, http_code=HTTPStatus.BAD_REQUEST):
        self.message = message
        self.http_code = http_code
        super().__init__(self.message)
