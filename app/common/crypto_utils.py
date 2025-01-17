
import hashlib


def hash_password(password: str) -> str:
    """
    Hash the given password using SHA-256.

    Args:
        password (str): The plain-text password to hash.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()
