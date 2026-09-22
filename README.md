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

Install dependencies with:
```bash
make install
```

---

## How to use it

```bash
# Encrypt files in ~/infection
python3 stockholm.py

# Decrypt files using your key
python3 stockholm.py -r YOUR_KEY_HERE

# Run without any output
python3 stockholm.py -s

# Show help
python3 stockholm.py -h

# Show version
python3 stockholm.py -v
```

---

## Important

- The program only touches files inside `~/infection` — nothing else
- Your encryption key will be at least 16 characters long — keep it somewhere safe
- Must be run in a Linux environment (VM or Docker recommended)