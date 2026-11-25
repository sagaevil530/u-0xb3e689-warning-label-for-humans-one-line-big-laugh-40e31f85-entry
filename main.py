"""Warning Label for Humans: One Line, Big Laugh.

Writes the funniest single-line safety warning label that should come
printed on every human being to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python 3.13, standard library only, no network, no randomness: the output
is fully deterministic.
"""

import os
import stat
import sys

MAX_CHARS = 160

# The label: a WARNING in the voice of a printed safety sticker, built on
# a three-beat rhythm -- skipped the instructions, blamed the instructions,
# and now explains them to you. The punchline lands in the last few words,
# and the joke is recognition: this is exactly how humans behave.
LINE = (
    "WARNING: This human skipped the instructions, "
    "blamed the instructions, and will now explain them to you."
)


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(
            f"error: line is {len(LINE)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not LINE.strip():
        print("error: line is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
