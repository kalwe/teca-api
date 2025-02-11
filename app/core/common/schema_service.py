from typing import Any, Optional

from api.schemas.base_schema import SchemaT

# class OutputSchema:
#     def __init__(self, schema: OutputSchemaT):
#         self._schema = schema


# class InputSchema:
#     def __init__(self, schema: InputSchemaT):
#         self._schema = schema


class SchemaService:
    def __init__(self, schema: SchemaT):
        self._schema = schema

    def validate(self, model) -> Optional[SchemaT]:
        if isinstance(model, list):
            validated_models = [self._schema.validate(m) for m in model]
            return validated_models

        validated_model = self._schema.validate(model)
        return validated_model

    def dump(self) -> dict[str, Any]:
        dumped_model = self._schema.dump()
        return dumped_model
