from marshmallow import ValidationError
from http import HTTPStatus

def validate_schema(schema_class, data):
    """
    Validate input data against a Marshmallow schema.
    """
    schema = schema_class()
    try:
        validated_data = schema.load(data)
        return validated_data, None
    except ValidationError as error:
        return None, ResponseHandler.create_error_response(HTTPStatus.BAD_REQUEST, str(error))

async def fetch_or_404(service, item_id, not_found_message):
    """
    Fetch an item by ID or return a 404 response if not found.
    """
    item = await service.get(item_id)
    if not item:
        # TODO: should be fail response
        return None, ResponseHandler.create_error_response(HTTPStatus.NOT_FOUND, not_found_message)
    return item, None
