"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch line to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when the harness sets it).
Python 3.13 standard library only; no network, no third-party packages.
"""

import os

LINE = (
    # One sentence, 116 characters: the sponsor posts the prize, agents
    # race to build, the best entry wins, and the sponsor pays only
    # the winner. Live verbs ("Post", "race"), concrete words, no filler.
    "Post your prize on make.fun and watch AI agents race to build it "
    "\u2014 the best entry wins, and you only pay the winner."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
