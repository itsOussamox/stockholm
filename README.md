# Stockholm

Educational ransomware simulation — mimics WannaCry file targeting, safely and reversibly.

> ⚠️ For learning only. Never use with malicious intent.

---

## Requirements

- Python 3.x — Linux environment (VM or Docker recommended)

```bash
make install
```

---

## Usage

```bash
make run                        # Encrypt files in ~/infection
make run ARGS="-r YOUR_KEY"     # Decrypt files using your key
make run ARGS="-s"              # Silent mode (only the key is printed)
make help                       # Show all options
make version                    # Show version
```

---

## The key

When encrypting, the key is **always printed** — even in silent mode:

```
[!] Your encryption key (save this now):
    9f3a01c844bb72e10d56f391...
```

Save it immediately. Without it your files cannot be recovered.
It is a 64-character hex string (AES-256 / 32 bytes).

---


## Notes

- Only touches files inside `~/infection` — nothing else
- Already encrypted `.ft` files are never encrypted twice
- Wrong key on `-r` is safely refused — no data is lost
