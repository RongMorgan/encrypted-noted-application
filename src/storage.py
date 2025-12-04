import os
import json

NOTES_DIR = "notes/"
CONFIG_FILE = "master_config.json"


# ----------------------------
# Notes Directory Management
# ----------------------------

def ensure_notes_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)


# ----------------------------
# Master Password Config
# ----------------------------

def load_master_config():
    """
    Load stored master password hash + salt.
    Returns None if config does not exist.
    """
    if not os.path.exists(CONFIG_FILE):
        return None

    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_master_config(data):
    """
    Save master password hash and salt.
    Expected data format:
    {
        "hash": "...",
        "salt": "..."
    }
    """
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ----------------------------
# Encrypted Notes Handling
# ----------------------------

def save_encrypted_note(ciphertext: bytes, nonce: bytes):
    ensure_notes_dir()

    note_id = str(len(os.listdir(NOTES_DIR)) + 1)
    filename = f"note_{note_id}.enc"

    with open(os.path.join(NOTES_DIR, filename), "wb") as f:
        f.write(nonce + ciphertext)

    return filename


def load_encrypted_note(filename: str):
    with open(os.path.join(NOTES_DIR, filename), "rb") as f:
        data = f.read()

    nonce = data[:12]
    ciphertext = data[12:]
    return ciphertext, nonce


def list_notes():
    ensure_notes_dir()
    return sorted(os.listdir(NOTES_DIR))


def delete_note(filename: str):
    os.remove(os.path.join(NOTES_DIR, filename))
