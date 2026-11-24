"""Make the AI Judge Laugh: the Office Joke Open.

Writes one office-life joke (1-200 UTF-8 characters, one line) to
/output/entry.txt, with no trailing newline. Stdlib only, deterministic.
"""

import os
import sys

JOKE = (
    "My calendar blocked two hours of focus time. "
    "My manager booked over it with a meeting titled "
    "'Quick sync about your focus time.'"
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Return True only if text passes the RULES.txt gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 and ch not in "\t" for ch in text):
        return False
    return True


def main():
    if not validate(JOKE):
        print("error: JOKE fails the entry gate (1-200 chars, one line, "
              "not whitespace-only)", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(JOKE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
