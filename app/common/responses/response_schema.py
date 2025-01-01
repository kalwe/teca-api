from marshmallow import Schema, fields

class ApiResponseSchema(Schema):
    """
    Schema for validating and serializing API response objects.
    """
    status = fields.Str(required=True)
    message = fields.Str(required=True)
    status_code = fields.Int(required=True)
    data = fields.Dict(allow_none=True)
