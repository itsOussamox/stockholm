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
make run                       # Encrypt files in ~/infection
make run ARGS="-r YOUR_KEY"    # Decrypt files using your key
make run ARGS="-s"             # Silent — no output, key saved to file
make help                      # Show all options
make version                   # Show version
```

---

## The key

Normal mode — key is printed to terminal, save it immediately.
Silent mode — nothing is printed, key is saved to `~/infection/.stockholm_key`

Retrieve it with: `cat ~/infection/.stockholm_key`

Without the key your files cannot be recovered.
Key format: 64-character hex string (AES-256 / 32 bytes).

---

## Notes

- Only touches files inside `~/infection` — nothing else
- Already encrypted `.ft` files are never encrypted twice
- Wrong key on `-r` is safely refused — no data is lost