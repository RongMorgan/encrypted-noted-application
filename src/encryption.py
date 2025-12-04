from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


def encrypt_note(key: bytes, plaintext: str):
    """
    Encrypts a note using AES-256-GCM.
    Returns ciphertext and nonce.
    """
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # recommended size for GCM
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return ciphertext, nonce


def decrypt_note(key: bytes, ciphertext: bytes, nonce: bytes):
    """
    Decrypts AES-256-GCM encrypted data.
    """
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode()
