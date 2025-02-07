
import hashlib
import uuid


def hash_provider(plain_text: str) -> str:
    """
    Hash password with a randomly-generated uuid4(16 bytes) salt.

    Args:
        plain_text: (str) - The plain  text to hash.

    Returns:
        str: salted_hash
    """
    salt = uuid.uuid4().hex
    hash = hashlib.sha256(
        salt.encode() + plain_text.encode()
    ).hexdigest()

    return salt + ':' + hash


def hash_match(hash: str, plain_text: str) -> bool:
    """
    Check if password match
    Split salt from hash by _IFS=:,

    Args:
        hash (str): hash with salt
        plain (str): plain password

    Returns:
        bool: True if match
    """
    salt, _hash = hash.split(':')
    hash_digest = hashlib.sha256(
        salt.encode() + plain_text.encode()
    ).hexdigest()

    return _hash == hash_digest
