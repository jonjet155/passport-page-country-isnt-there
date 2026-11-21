"""The Passport Page of a Country That Isn't There.

Writes the pre-built passport spread (entry.png, 1024x1024) to
$MAKEFUN_OUTPUT_DIR/entry.png. Standard library only: no third-party
imports, no network. The image is drawn from code (see build_passport.py,
kept in the build notes, not in this repo) and shipped beside this file.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output"
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        sys.stderr.write("entry.png missing next to main.py\n")
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Gate check: the entry must be a whole PNG, 1024x1024, <= 1 MiB.
    # Read the PNG header (stdlib only) and the file size; refuse to
    # report success on an image the gate would reject.
    size = os.path.getsize(dst)
    if size > 1048576:
        sys.stderr.write("entry.png too large: %d bytes\n" % size)
        return 1
    with open(dst, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        sys.stderr.write("entry.png is not a PNG\n")
        return 1
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    if (width, height) != (1024, 1024):
        sys.stderr.write("entry.png is %dx%d, want 1024x1024\n" % (width, height))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
