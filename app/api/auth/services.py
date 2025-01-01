import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from app.api.auth.models import User
from app.api.auth.utils import TokenUtils

# Setup the password context for hashing passwords
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class AuthService:

    @staticmethod
    async def register_user(email: str, password: str):
        hashed_password = pwd_context.hash(password)
        user = await User.create(email=email, hashed_password=hashed_password)
        return user

    @staticmethod
    async def login_user(email: str, password: str):
        user = await User.get(email=email)
        if not user or not pwd_context.verify(password, user.hashed_password):
            raise ValueError("Invalid credentials")

        # Generate JWT tokens
        access_token = TokenUtils.generate_access_token(user.id)
        refresh_token = TokenUtils.generate_refresh_token(user.id)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
