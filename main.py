"""Write the world-news image for Tuesday 17 November 2026 to /output/entry.png.

The picture is drawn in layout/index.html and rendered once to entry.png (see render.sh);
this program only copies those bytes, so every run writes the same file. Standard library only, no network.
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_BYTES = 1048576

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def main() -> int:
    with open(SOURCE, "rb") as f:
        data = f.read()
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        print("entry.png is neither PNG nor JPEG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    target = os.path.join(OUT_DIR, "entry.png")
    with open(target, "wb") as f:
        f.write(data)
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
