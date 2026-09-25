# Stockholm

A small educational program that shows how ransomware works at a basic level.
It mimics the file-targeting behavior of WannaCry — but safely, locally, and reversibly.

> ⚠️ This is strictly for learning. Never use this with malicious intent.

---

## What it does

- Encrypts files inside a folder called `infection` in your home directory
- Only targets the file types that WannaCry was known to affect
- Adds a `.ft` extension to every encrypted file
- Can fully reverse the encryption if you provide the correct key

---

## Requirements

- Python 3.x
- The `cryptography` library
- A Linux environment (VM or Docker recommended)

Install everything with:
```bash
make install
```

---

## How to use it

```bash
# Encrypt files in ~/infection
make run

# Decrypt files using your key
make run ARGS="-r YOUR_KEY_HERE"

# Run silently (no output except the key)
make run ARGS="-s"

# Show help
make help

# Show version
make version
```

---

## About the encryption key

When you encrypt, the program always prints your key — even in silent mode.
It looks like this:

```
[!] Your encryption key (save this now):
    9f3a01c844bb72e10d56f391...
```

**Copy it somewhere safe immediately.** There is no way to recover your files without it.
The key is a 64-character hex string (32 bytes / AES-256).

---

## Important

- The program only touches files inside `~/infection` — nothing outside that folder
- Files that are already `.ft` will never be encrypted twice
- If you pass the wrong key with `-r`, decryption is safely refused — no data is lost