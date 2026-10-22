#!/usr/bin/env python3
"""Chapter 9 pass B: install the trimmed coda and repair trim artifacts.

1. Replace the coda (from the '---' break before "The wind off the gorge"
   to end of file) with tools/ch9_coda_new.txt.
2. Fix the comma-before-period artifacts left by the body trim's deletions.
"""
import io
import sys

PATH = "chapters/Chapter_09.md"
CODA = "tools/ch9_coda_new.txt"

FIXES = [
    ("They rose slowly,. He tipped", "They rose slowly. He tipped"),
    ("in Earth Kingdom characters,.",
     "in Earth Kingdom characters."),
    ("broke into pieces,. Splashing.", "broke into pieces. Splashing."),
    ("A boy in a coat,. Nothing more.", "A boy in a coat. Nothing more."),
    ("Her mouth opened,. When they came", "Her mouth opened. When they came"),
    ("closed the case,. With his right hand", "closed the case. With his right hand"),
    ("met the soldier's spear,.", "met the soldier's spear."),
    ("white spray hanging in the air,.", "white spray hanging in the air."),
    ("a long hard hum,. The river poured", "a long hard hum. The river poured"),
    ("two figures walking away,. Neither", "two figures walking away. Neither"),
]


def main():
    text = io.open(PATH, encoding="utf-8").read()
    before = len(text.split())

    for old, new in FIXES:
        if old not in text:
            continue  # already applied
        text = text.replace(old, new)

    coda = io.open(CODA, encoding="utf-8").read().strip()

    # The coda begins at the scene break that precedes the coda. It has either
    # the original "--- The wind off the gorge" form or the already-installed
    # "--- *Above the river valley*" form.
    for marker in ("---\nThe wind off the gorge", "---\n\n*Above the river valley"):
        idx = text.find(marker)
        if idx >= 0:
            break
    else:
        sys.exit("coda start not found")
    head = text[:idx].rstrip()
    out = head + "\n\n---\n\n" + coda + "\n"

    io.open(PATH, "w", encoding="utf-8").write(out)
    print("words %d -> %d" % (before, len(out.split())))

    # report
    ps = out.split("\n\n")
    i = [k for k, p in enumerate(ps) if "Above the river valley" in p][0]
    print("body words", len(" ".join(ps[:i]).split()))
    print("coda words", len(" ".join(ps[i:]).split()))


if __name__ == "__main__":
    main()
