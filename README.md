# Stockholm

Educational ransomware simulation — mimics WannaCry file targeting, safely and reversibly.

> ⚠️ For learning only. Never use with malicious intent.

---

## Docker (recommended)

```bash
docker build -t stockholm .
docker run --name stockholm -it stockholm 
docker rm stockholm
docker rmi stockholm
```


## Local setup

Requires Python 3.x on Linux.

```bash
make install                    # setup
make run                        # encrypt
make run ARGS="-r YOUR_KEY"     # decrypt
make help                       # all options
```

---

## The key

Normal mode — key is printed to terminal, save it immediately.
Silent mode — key is saved to `~/infection/.stockholm_key`

Retrieve it with: `cat ~/infection/.stockholm_key`

Key format: 64-character hex string (AES-256 / 32 bytes).

---

## Notes

- Only touches files inside `~/infection` — nothing else
- Already encrypted `.ft` files are never encrypted twice
- Wrong key on `-r` is safely refused — no data is lost