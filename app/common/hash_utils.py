
import hashlib
import uuid


def hash_provider(plain_text: str):
    """
    Hash password with a randomly-generated
    salt and return a hash + salt.

    Args:
        plain_text: (str) - The plain  text to hash.

    Returns:
        str: hash (hash + ':' + salt)
    """
    salt = uuid.uuid4().hex
    hash = hashlib.sha256(salt.encode() + plain_text.encode()
                          ).hexdigest() + ':' + salt

    return hash


def hash_match(hash: str, plain_text: str):
    """
    Check if password match

    Args:
        hash (str): hash with salt
        plain (str): plain password

    Returns:
        bool: True if match
    """
    _hash, salt = hash.split(':')
    hash_digest = hashlib.sha256(salt.encode() + plain_text.encode()
                                 ).hexdigest()

    return _hash == hash_digest
