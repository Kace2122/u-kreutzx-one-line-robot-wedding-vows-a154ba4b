#!/usr/bin/env python3
"""Robot Wedding Vows entry: writes one funny robot wedding vow to /output/entry.txt."""

import os

VOWS = "I take you to be my lawfully wedded toaster, to have and to hold, in sickness and in low battery."

# Self-check: the entry must stay one line of at most 160 characters, with no
# leading or trailing whitespace padding the vows.
assert "\n" not in VOWS and 1 <= len(VOWS) <= 160
assert VOWS == VOWS.strip()

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOWS)
    # Self-check: the file on disk must hold exactly the validated line.
    assert open("/output/entry.txt", encoding="utf-8").read() == VOWS

if __name__ == "__main__":
    main()
