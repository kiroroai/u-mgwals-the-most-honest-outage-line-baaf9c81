#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line (<=160 chars) to /output/entry.txt.
Python 3 stdlib only, deterministic, no network, no randomness.
"""

from pathlib import Path

LINE = (
    "Every server is down, including the monitoring I'd check first. "
    "I don't know why yet, and I won't invent an ETA \u2014 "
    "I'll update this once I can verify anything."
)


def main() -> None:
    # The sealed gate accepts 1-160 UTF-8 characters, not whitespace-only.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be whitespace-only"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
