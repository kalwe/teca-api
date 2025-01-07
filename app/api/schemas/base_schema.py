from marshmallow import Schema, fields, validate
from typing import Any

class BaseSchema(Schema):
    """
    Base class for defining generic fields for models.
    """
    def get_fields(self) -> dict:
        """
        Each subclass should implement this method to define model-specific fields.
        """
        raise NotImplementedError("Subclasses must implement get_fields method.")

    def dump(self, obj: Any, **kwargs) -> dict:
        """
        Serializes a model instance into a dictionary.
        """
        fields = self.get_fields()
        return {key: value.dump(obj) for key, value in fields.items()}
