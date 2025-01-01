from app.common.responses.response_model import ApiResponse

class ApiResponseSerializer:
    """
    Serializer for converting ApiResponse objects to a dictionary.
    """

    def __init__(self, api_response: ApiResponse):
        self.api_response = api_response

    def serialize(self):
        """
        Serialize the ApiResponse object into a dictionary format.
        """
        return self.api_response.to_dict()
