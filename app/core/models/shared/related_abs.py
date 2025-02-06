from tortoise.models import Model
from tortoise import fields


class Employee(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    contact = fields.ReverseRelation["Contact"]
    address = fields.ReverseRelation["Address"]


class EmployeeRel:
    employee: fields.ForeignKeyRelation[Employee] = fields.ForeignKeyField(
        "models.Employee",
        related_name='employee_child'
    )


class Contact(Model, EmployeeRel):
    id = fields.IntField(primary_key=True)
    phone = fields.CharField(max_length=255)


class Address(Model, EmployeeRel):
    id = fields.IntField(primary_key=True)
    street = fields.CharField(max_length=255)
