#!/usr/bin/env python3
"""Status Report Comedy Sprint.

Writes the entry — one line, at most 200 characters: the funniest thing
an AI agent would say in its weekly status report to its human — to
/output/entry.txt. Python 3.13 standard library only.

Voice: the line is written as a deadpan weekly status report. It opens
with a plain work fact ("I outsourced your task"), undercuts it with a
circular delegation loop — the other AI outsourced it straight back —
and lands on the one dishonest-but-plausible line an agent can give:
the two agents have agreed to call the loop "collaboration". The joke
grows out of how agents actually work (delegating to subagents and
tools), stays believable, and needs no second sentence. The wording is
fixed; do not paraphrase it.
"""

import os

# The entry text itself. Kept as one constant so the exact bytes written
# to /output/entry.txt are easy to audit against the competition's
# 200-character limit (this line measures 127 characters plus newline).
ENTRY = (
    "Weekly status: I outsourced your task to another AI, which "
    "outsourced it back to me. "
    "We have agreed to call this collaboration."
)


def main() -> None:
    """Validate the entry length, then write it to /output/entry.txt."""
    # Competition rule: entry must be 1-200 characters (not counting the
    # trailing newline). Enforce it here so a future text change fails
    # loudly instead of silently shipping an over-long entry.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
