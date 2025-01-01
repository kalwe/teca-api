from http import HTTPStatus

class CustomValidationError(Exception):
    """
    Custom exception for validation errors in API requests.
    """

    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
