#!/usr/bin/env python3

"""
stockholm.py - Entry point of the program.

This project is for educational purposes only.
Do not use it with malicious intent.
"""

import sys
from args import get_args


def main():
    args = get_args()

    # From here on, every print goes through this small helper
    # so that --silent is respected everywhere without repeating the check.
    def log(message):
        if not args.silent:
            print(message)

    if args.reverse:
        log(f"[~] Reverse mode activated. Key: {args.reverse}")
        # TODO: decryption logic will go here
    else:
        log("[~] Encryption mode activated.")
        # TODO: encryption logic will go here


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Interrupted.")
        sys.exit(1)