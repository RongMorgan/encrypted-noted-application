import os
import json

NOTES_DIR = "notes/"


def ensure_notes_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)


def save_encrypted_note(ciphertext: bytes, nonce: bytes):
    ensure_notes_dir()

    note_id = str(len(os.listdir(NOTES_DIR)) + 1)
    filename = f"note_{note_id}.enc"

    with open(os.path.join(NOTES_DIR, filename), "wb") as f:
        f.write(nonce + ciphertext)


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
