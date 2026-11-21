#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network, no input.

Joke (111 chars, 1 line):
    Pair programming with my AI agent: I write the bugs, it writes the
    apologies, and git blame still says my name.
"""

import os

JOKE = (
    "Pair programming with my AI agent: I write the bugs, "
    "it writes the apologies, and git blame still says my name."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
