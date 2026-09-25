import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
 
 
def generate_key():
    raw = os.urandom(32)
    return raw.hex()
 
 
def encrypt_file(filepath, key_hex, log):
    try:
        key = bytes.fromhex(key_hex)
        iv  = os.urandom(16)
 
        with open(filepath, 'rb') as f:
            content = f.read()
 
        aesgcm    = AESGCM(key)
        encrypted = aesgcm.encrypt(iv, content, None)
 
        ft_path = filepath + '.ft'
        with open(ft_path, 'wb') as f:
            f.write(iv + encrypted)
 
        os.remove(filepath)
        log(f"  [+] {os.path.basename(filepath)} → {os.path.basename(ft_path)}")
 
    except Exception as e:
        log(f"  [!] Could not encrypt {filepath}: {e}")
 
 
def decrypt_file(filepath, key_hex, log):
    try:
        key = bytes.fromhex(key_hex)
 
        with open(filepath, 'rb') as f:
            data = f.read()
 
        iv        = data[:16]
        encrypted = data[16:]
 
        aesgcm  = AESGCM(key)
        content = aesgcm.decrypt(iv, encrypted, None)
 
        original_path = filepath[:-3]
        with open(original_path, 'wb') as f:
            f.write(content)
 
        os.remove(filepath)
        log(f"  [+] {os.path.basename(filepath)} → {os.path.basename(original_path)}")
 
    except Exception as e:
        log(f"  [!] Could not decrypt {filepath}: {e}")