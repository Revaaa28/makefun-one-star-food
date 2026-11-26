#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence one-star review of Earth, in the voice of an
alien tourist, that still slips in a compliment about the food,
to /output/entry.txt.
"""

import os

ENTRY = "One star: I came for the sights, stayed for the snacks \u2014 Earth's gravity crushed my spine, its pigeons stole my lunch, yet the biryani made me extend my visa by a century."


def main() -> None:
    # Gate self-check: the kit gate requires /output/entry.txt to be
    # UTF-8 text of 1 to 200 characters, not only white space, and the
    # brief requires a single sentence.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip() == ENTRY, "entry has leading/trailing whitespace"
    assert ENTRY.count(".") + ENTRY.count("?") + ENTRY.count("!") == 1, (
        "entry must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
