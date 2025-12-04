import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

ITERATIONS = 200_000  # strong security


def derive_key(password: str, salt: bytes = None):
    """
    Derive AES-256 key from password using PBKDF2.
    """
    if salt is None:
        salt = b"fixed-salt-for-notes"  # for simplicity; you can randomize later

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )

    return kdf.derive(password.encode())
