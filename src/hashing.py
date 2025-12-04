import os
import hashlib
import json

CONFIG_FILE = "master_config.json"


def hash_password(password: str, salt: bytes):
    return hashlib.sha256(password.encode() + salt).hexdigest()


def save_password_hash(password: str):
    salt = os.urandom(16)
    hashed = hash_password(password, salt)

    data = {
        "salt": salt.hex(),
        "hash": hashed
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)


def verify_password(password: str, stored_hash: str, stored_salt: str):
    salt = bytes.fromhex(stored_salt)
    return hash_password(password, salt) == stored_hash
