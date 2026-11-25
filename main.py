"""Invent a Word We Need entry (Python 3.13, standard library only).

Writes one invented word and its one-line definition to /output/entry.txt
(or to $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Deterministic: every run writes exactly the same bytes.

The word: savepile — the growing pile of posts and videos you saved for
later and will never open again. Everyone has one: the bookmark folder,
the watch-later list, the saved posts nobody ever reopens. English has
words for hoarding things, but none for hoarding things to read later
that you will never read. savepile names that pile, in one breath.
"""

import os
from pathlib import Path

# One line, 99 characters, no trailing newline in the output file.
LINE = "savepile (n.) — the growing pile of posts and videos you saved for later and will never open again."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
