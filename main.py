#!/usr/bin/env python3
"""One Word for the Boss — make.fun bounty entry.

Deterministic, no network, no randomness, no LLM calls.
Writes the single-word entry to <ENTRY_OUTPUT_DIR>/entry.txt
(default /output) and validates it with a self-check gate.
"""

import os
import sys
from pathlib import Path

ENTRY = "Slacktator"


def main() -> int:
    # Self-check gate: exactly one word, 1-30 chars, no spaces, non-blank.
    assert ENTRY, "entry must not be blank"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    assert len(ENTRY.split()) == 1, "entry must be exactly one word"
    assert " " not in ENTRY, "entry must contain no spaces"
    assert ENTRY.isalnum(), "entry must be a single alphanumeric token (no punctuation)"
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"

    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    # Verify the write: read it back and confirm it matches exactly.
    assert out_path.read_text(encoding="utf-8") == ENTRY, "written entry does not match ENTRY"
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
