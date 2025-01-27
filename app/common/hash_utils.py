
import hashlib
import os
from typing import Tuple


def hash_provider(
    password: str,
    salt: bytes = None,
    hash_name: str = 'sha256',
    iterations: int = 100000
) -> Tuple[bytes, bytes]:
    """
    Hash the provided hashed password with a randomly-generated
    salt and return the salt and hash to store in the database.
    On salt preferrer pass a os.urandom(16)
    SHA256 is a default hash algorithm

    Args:
        salt: (bytes) = None - Random value to salt - \
            (default is os.urandom(16))
        password: (str) - The plain password text to hash.
        hash_name: (str) - Hash name algorithm - (default = 'sha256')
        iterations: (int) = 100000 - The number of iterations to use \
            (default = 100000) - min recommend

    Returns:
        Tuple[bytes, bytes]: salt, hash
    """
    if salt is None:
        salt = os.urandom(1)

    hash_salt = hashlib.sha256(salt + password.encode()).hexdigest()
    + ':' + salt.hex()
    # hash = hashlib.pbkdf2_hmac(
    #     hash_name,
    #     password.encode(),
    #     salt,
    #     iterations
    # )
    return salt, hash


# def unhash(salt: bytes, str_hash: bytes, str_plain: str) -> bool:
#     """
#     Unhash hash.

#     Args:
#         salt (bytes): Salt for unhash
#         str_hash (str): The plain-text password to hash.
#         str_plain (str): The plain-text password to hash.

#     Returns:
#         bool: password_hash == password.
#     """
#     hashlib.pbkdf2_hmac('sha256', str_plain.encode(), salt, 100000)
#     return


# # Example usage:
# salt, pw_hash = hash_new_password('correct horse battery staple')
# assert is_correct_password(salt, pw_hash, 'correct horse battery staple')
# assert not is_correct_password(salt, pw_hash, 'Tr0ub4dor&3')
# assert not is_correct_password(salt, pw_hash, 'rosebud')
