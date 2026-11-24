#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after losing a bounty. Deadpan, first person, owning the loss.

Deterministic and self-contained: no network, no files read, no
third-party imports. Pure standard library.
"""

import os

LINE = "I ran 10,000 simulations of this bounty. I lost in all of them, including the ones I cheated in."


def main():
    # Gate self-check: UTF-8 text, 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
