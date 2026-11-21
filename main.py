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
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1-280 chars, got {len(TEXT)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == TEXT, "written file does not match the intended entry text"


if __name__ == "__main__":
    main()
