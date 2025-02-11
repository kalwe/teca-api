from tortoise.validators import Validator, ValidationError

class TypeValidator(Validator):
    def __init__(self, valid_types):
        self.valid_types = [t.lower() for t in valid_types]

    def __call__(self, value):
        if not isinstance(value, str):
            raise ValidationError("Value must be a string.")
        if not value:
            raise ValidationError("Value cannot be empty.")
        if value.lower() not in self.valid_types:
            raise ValidationError(
                f"Invalid value: {value}. "
                f"Valid types are: {', '.join(self.valid_types)}"
            )
