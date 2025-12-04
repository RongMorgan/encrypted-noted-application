import os
from encryption import encrypt_note, decrypt_note
from kdf import derive_key
from hashing import save_password_hash, verify_password
from storage import save_encrypted_note, load_encrypted_note, list_notes, delete_note
from utils import load_master_config, create_master_config


def require_master_password():
    """
    Load master password hash and verify user input.
    If no master password exists, user must create one.
    """
    config = load_master_config()

    if config is None:
        print("\nNo master password found. Create one now.")
        pwd = input("Create master password: ")
        save_password_hash(pwd)
        print("Master password created.\n")
        return pwd

    # Existing password → verify
    pwd = input("Enter master password: ")
    if verify_password(pwd, config['hash'], config['salt']):
        return pwd
    else:
        print("❌ Incorrect password. Access denied.")
        return None


def create_note():
    print("\n=== CREATE NEW NOTE ===")
    pwd = require_master_password()
    if not pwd:
        return

    note_text = input("Enter your note:\n")
    key = derive_key(pwd)

    ciphertext, nonce = encrypt_note(key, note_text)
    save_encrypted_note(ciphertext, nonce)

    print("✓ Note encrypted and saved!\n")


def view_notes():
    print("\n=== VIEW NOTES ===")
    pwd = require_master_password()
    if not pwd:
        return

    key = derive_key(pwd)
    notes = list_notes()

    if not notes:
        print("No notes found.\n")
        return

    for idx, filename in enumerate(notes, start=1):
        print(f"{idx}. {filename}")

    choice = int(input("\nChoose a note number to view: "))
    filename = notes[choice - 1]

    ciphertext, nonce = load_encrypted_note(filename)
    plaintext = decrypt_note(key, ciphertext, nonce)

    print("\n--- NOTE CONTENT ---")
    print(plaintext)
    print("--------------------\n")


def delete_notes():
    print("\n=== DELETE NOTE ===")
    pwd = require_master_password()
    if not pwd:
        return

    notes = list_notes()
    if not notes:
        print("No notes to delete.\n")
        return

    for idx, filename in enumerate(notes, start=1):
        print(f"{idx}. {filename}")

    choice = int(input("\nChoose note number to delete: "))
    filename = notes[choice - 1]

    delete_note(filename)
    print("✓ Note deleted.\n")


def menu():
    while True:
        print("\n=== ENCRYPTED NOTES APP ===")
        print("1. Create Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    menu()
