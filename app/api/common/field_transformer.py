from typing import Any


def field_transformer(field_name: str, transformers: dict[str, Any]) -> str:
    """
    Use in schemas with pydantic.
    Set a alias in field name.

    Args:
        field_name (str):
        transformers (dict[str, Any]): {"field_name": "alias_to_transform"}

    Returns:
        str: _description_
    """
    for key, val in transformers.items():
        if field_name == key:
            return val
        return field_name
