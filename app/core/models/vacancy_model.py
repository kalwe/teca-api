from tortoise import fields

from app.core.models.shared.base_model import ModelBase


class Vacancy(ModelBase):
    quantity = fields.IntField()
    position = fields.CharField(
        max_length=32,
        description="Position of vacancy",
    )
    description = fields.CharField(
        max_length=32,
        description="description of vacancy",
    )
    requirements = fields.CharField(
        max_length=255,
        description="Requirements of vacancy",
    )
    benefits = fields.CharField(
        max_length=255,
        description="Benefits of vacancy",
    )
    salary = fields.IntField(
        max_length=32,
        description="Salary of vacancy",
    )
