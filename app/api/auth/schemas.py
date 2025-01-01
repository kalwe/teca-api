from pydantic import BaseEntity, EmailStr

class LoginSchema(BaseEntity):
    email: EmailStr
    password: str

class RegisterSchema(BaseEntity):
    email: EmailStr
    password: str
