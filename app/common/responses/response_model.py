from http import HTTPStatus

from app.common.responses.enum import ResponseStatus

class ApiResponse:
    """
    Represents a standardized API response.
    """

    def __init__(self, status: ResponseStatus, message: str, status_code: HTTPStatus, data=None):
        self.status = status
        self.message = message
        self.status_code = status_code
        self.data = data
        # self.timestamp = datetime.datetime.utcnow().isoformat()

    def to_dict(self):
        """
        Convert the ApiResponse object into a dictionary format.
        """
        return {
            "status": self.status.value,
            "message": self.message,
            "status_code": self.status_code.value,
            "data": self.data,
            # "timestamp": self.timestamp
        }
