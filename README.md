# encrypted-noted-application
🛡️ Secure Encrypted Notes Application

A lightweight, local-first application designed to securely store personal notes using strong cryptographic mechanisms. All notes are encrypted using AES-256 and protected with a password-derived key, ensuring confidentiality even if the device or files are compromised.

📌 Overview

The Secure Encrypted Notes Application allows users to:
- Create encrypted text notes
- View and decrypt notes only with the correct password
- Delete notes securely
- Store all data locally in encrypted form
- Protect note files with strong cryptographic algorithms
This project demonstrates practical cryptography concepts such as AES encryption, hashing, salting, and key derivation functions (KDF). It is designed to show how theory applies to real-world secure software development.

🔐 Key Features
- AES-256 symmetric encryption for strong data confidentiality
- PBKDF2 or Argon2 for secure key derivation
- SHA-256 hashing with salt for password verification
- Encrypted local file storage (no plaintext written to disk)
- Clean code and modular structure
- Cross-platform (Linux)
- Simple and easy-to-use command-line 
