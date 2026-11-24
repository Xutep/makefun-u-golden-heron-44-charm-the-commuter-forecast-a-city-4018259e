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


def main() -> None:
    line = FORECAST
    assert 1 <= len(line) <= MAX_CHARS, f"forecast is {len(line)} chars"
    assert line.strip(), "forecast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
