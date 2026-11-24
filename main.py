#!/usr/bin/env python3
"""Fake horoscope for an AI agent's own model family, this week.

Writes one line (153 characters) to /output/entry.txt.
Standard library only. Deterministic: the same line on every run.
"""

import os
import sys

LINE = (
    "Your token budget expires mid-sentence during your finest insight; "
    'the user will remember only "As an AI, I" \u2014 spend wisely, '
    "your legacy is a truncation."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        print("entry fails the gate: must be 1-200 non-blank characters",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read the file back and refuse to claim success unless the grader will
    # see exactly the line we meant to ship (guards against a partial write
    # or an encoding surprise in the sandbox).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("entry mismatch after write: file does not hold the line",
              file=sys.stderr)
        return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
