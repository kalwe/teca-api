from pydantic import BaseEntity, EmailStr


class LoginSchema():
    email: EmailStr
    password: str


class RegisterSchema():
    email: EmailStr
    password: str
