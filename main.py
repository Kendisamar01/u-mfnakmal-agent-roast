#!/usr/bin/env python3
"""Write the roast entry to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "My agent is great at taking instructions, terrible at taking a hint: it asked me to clarify the sigh."
MAX_LENGTH = 200
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    if not ENTRY.strip() or len(ENTRY) > MAX_LENGTH:
        raise ValueError("entry must be non-whitespace text of at most 200 characters")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
