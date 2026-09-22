#!/usr/bin/env python3

"""
stockholm.py - Entry point of the program.

This project is for educational purposes only.
Do not use it with malicious intent.
"""

import sys
from args import get_args
from infection import get_infection_dir, get_target_files, get_encrypted_files


def main():
    args = get_args()

    def log(message):
        if not args.silent:
            print(message)

    try:
        folder = get_infection_dir()
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    if args.reverse:
        files = get_encrypted_files(folder)
        if not files:
            log("[!] No encrypted files found.")
            return
        log(f"[~] Reverse mode — {len(files)} file(s) to decrypt.")
        for f in files:
            log(f"    {f}")
        # TODO: decryption logic will go here

    else:
        files = get_target_files(folder)
        if not files:
            log("[!] No eligible files found in ~/infection.")
            return
        log(f"[~] Encryption mode — {len(files)} file(s) to encrypt.")
        for f in files:
            log(f"    {f}")
        # TODO: encryption logic will go here


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted.")
        sys.exit(1)