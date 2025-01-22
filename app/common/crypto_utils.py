
import hashlib
import hmac
import os
from typing import Tuple


def hash_password(password: str) -> Tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.

    Args:
        password (str): The plain-text password to hash.

    Returns:
        Tuple[bytes, bytes]: Salt and hashed password.
    """
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )
    return salt, password_hash


def unhash_password(salt: bytes, password_hash: bytes, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.

    Args:
        salt (bytes): Salt for unhash
        password_hash (str): The plain-text password to hash.
        password (str): The plain-text password to hash.

    Returns:
        bool: password_hash == password.
    """
    return hmac.compare_digest(
        password_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

# # Example usage:
# salt, pw_hash = hash_new_password('correct horse battery staple')
# assert is_correct_password(salt, pw_hash, 'correct horse battery staple')
# assert not is_correct_password(salt, pw_hash, 'Tr0ub4dor&3')
# assert not is_correct_password(salt, pw_hash, 'rosebud')
