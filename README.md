```markdown
# Encrypted Notes Application

A simple command-line application to create, view, and delete **encrypted personal notes** locally.  
All notes are securely encrypted using **AES-256** and a master password.

---

## Features

- Create encrypted notes  
- View decrypted notes (requires master password)  
- Delete notes  
- AES-GCM encryption for confidentiality and integrity  
- Master password stored securely with hash + salt  
- Notes stored locally in `notes/` folder  

---

## Project Structure

```

Encrypted_Note_Application_Code/
├── docs/                 # Project documentation (optional)
├── notes/                # Encrypted notes (created at runtime)
├── README.md
├── src/                  # Source code
│   ├── encryption.py
│   ├── hashing.py
│   ├── kdf.py
│   ├── main.py
│   └── storage.py
└── tests/                # Optional tests

````

---

## Requirements

- Python 3.8+  
- [cryptography](https://cryptography.io/) library

### Install dependencies

**Option 1: Using a virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/activate
pip install cryptography
````

**Option 2: System-wide install on Arch Linux**

```bash
sudo pacman -S python-cryptography
```

---

## How to Run

From the project root:

```bash
python3 -m src.main
```

If you prefer, you can also run from inside `src/`:

```bash
cd src
python3 main.py
```

---

## Usage Guide / Testing

1. **First-time setup / Master Password**

   * On first run, the app will ask you to create a master password.
   * This password will be used to encrypt and decrypt all notes.

2. **Create a Note**

   * Choose `1. Create Note`
   * Enter the master password
   * Type your note text
   * A new file will be saved in `notes/` as `note_1.enc` (binary, unreadable)

3. **View Notes**

   * Choose `2. View Notes`
   * Enter the master password
   * Select the note number to view
   * The app will decrypt and display the plaintext note

4. **Delete Notes**

   * Choose `3. Delete Note`
   * Enter the master password
   * Select the note number to delete
   * The corresponding `.enc` file will be removed

5. **Exit**

   * Choose `4. Exit` to close the app safely

---

## Security Checks (Optional Tests)

* Open a `.enc` file in a text editor or `cat notes/note_1.enc`.

  * Output should appear as **random binary characters**, not plaintext.
* Enter a wrong master password → access should be denied.
* Create multiple notes → each note saved with a unique filename.

---

## Notes

* All notes are stored **locally**, not on the cloud.
* Do not share your master password — it is required for all encryption/decryption.
* `master_config.json` stores the **hashed password and salt** securely.

---

## License

This project is for educational purposes.

```


