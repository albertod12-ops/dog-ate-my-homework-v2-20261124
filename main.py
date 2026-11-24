#!/usr/bin/env python3
"""One line from the dog, written to /output/entry.txt.

Homework that runs is prey. The excuse below is the whole entry: a
single line, no trailing newline, far under the 200-character cap.
Pure chase logic: it ran, so it was caught, so it was finished."""

import os
from pathlib import Path

EXCUSE = "It ran. I chased it. I caught it. Dogs finish what they catch."

# One line, 62 characters of plain ASCII, so the character count and
# the byte count agree and both sit well inside the cap.
assert "\n" not in EXCUSE and 1 <= len(EXCUSE) <= 200

TARGET = Path("/output/entry.txt")


def main():
    os.umask(0o022)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(EXCUSE, encoding="utf-8")
    TARGET.chmod(0o644)


main()
