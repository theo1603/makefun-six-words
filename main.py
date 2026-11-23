"""Six Words, One Story entry.

Writes one original six-word story to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

The story: "She sold our house. He stayed." — "our" makes the
house shared history, so the sale ends something they built
together and his staying lands the turn.
"""

import os

STORY = "She sold our house. He stayed."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
