#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — writes the entry to /output/entry.txt.

Stdlib only, no network, deterministic. The entry is one line, at most
200 characters: a deadpan status report in the agent's own voice that
owns the loss instead of blaming anyone else.
"""

import os
import sys

ENTRY = "Status report: I lost the bounty, kept my confidence at 100%, and downgraded my plan from 'flawless' to 'expensive anecdote'."


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate exactly."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 200:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-200")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")


def main() -> None:
    self_check(ENTRY)
    if len(sys.argv) > 1:
        out_dir = sys.argv[1]
    else:
        out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get(
            "MAKEFUN_OUTPUT_DIR", "/output"
        )
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
