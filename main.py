"""Write one childhood-memory sentence for the nostalgia judge.

The program writes a single sentence recalling a specific childhood
moment: streetlights coming on at dusk, running home barefoot, a
marbles game left unfinished. The detail is concrete and small, the
ache arrives only in the last words, and nothing is explained.
"""

import os
from pathlib import Path

ENTRY = "When the streetlights buzzed on, I ran home barefoot, marbles still in my pocket, the game still undecided."


def output_path() -> Path:
    """Return the entry file, honouring the grader's output directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
