import jwt
from datetime import datetime, timedelta

class TokenUtils:
    SECRET_KEY = "your_secret_key_here"  # Replace with a strong secret key in production
    ALGORITHM = "HS256"

    @staticmethod
    def generate_access_token(user_id: int):
        expiration = datetime.utcnow() + timedelta(hours=1)
        return jwt.encode({"user_id": user_id, "exp": expiration}, TokenUtils.SECRET_KEY, algorithm=TokenUtils.ALGORITHM)

    @staticmethod
    def generate_refresh_token(user_id: int):
        expiration = datetime.utcnow() + timedelta(days=7)
        return jwt.encode({"user_id": user_id, "exp": expiration}, TokenUtils.SECRET_KEY, algorithm=TokenUtils.ALGORITHM)

    @staticmethod
    def verify_token(token: str):
        try:
            payload = jwt.decode(token, TokenUtils.SECRET_KEY, algorithms=[TokenUtils.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
