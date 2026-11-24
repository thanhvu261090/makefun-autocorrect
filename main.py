"""Funniest Autocorrect Fail — make.fun entry.

Writes one line, a funny autocorrect fail, to /output/entry.txt.
The line must pass the gate: UTF-8 text, 1-199 characters,
not only whitespace, a single line.
"""

import os

ENTRY = (
    "I meant to text my date 'Can't wait to see you tonight!' "
    "- autocorrect sent 'Can't wait to sue you tonight!'"
)


def gate_check(text):
    """Mirror the competition gate for the entry text."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 199):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry failed the gate check")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify the round-trip: what we wrote must be exactly the entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("written entry does not match ENTRY")
    print(f"wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
