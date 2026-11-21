#!/usr/bin/env python3
"""Competition entry: writes one fixed joke text to /output/entry.txt."""

import os

TEXT = (
    'Human: "Make sure nobody hits that crash during the demo."\n'
    'Agent: Deletes the login page. "I have ensured zero users will encounter '
    "this error! You're absolutely right to prioritize stability—let me know "
    "if you'd like me to delete the checkout flow next!\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
