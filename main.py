#!/usr/bin/env python3
"""Charm the Commuter: one-line weather forecast for a city that isn't.

Writes a single deterministic forecast line (139 characters) for the
fictional city of Mizzlewick to /output/entry.txt. Standard library only,
no input, no network, no randomness: every run produces the same bytes.
"""

import os

FORECAST = (
    "Mizzlewick: 9\u00b0C, drizzle turning to sideways rain by 8am "
    "\u2014 hold your umbrella low, the 7:42 bus is late again, "
    "but the puddles are on time."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """The gate needs 1-140 UTF-8 characters, not only whitespace."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"forecast is {len(line)} chars, must be 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("forecast must not be only whitespace")
    return line


def main() -> None:
    line = validate(FORECAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
