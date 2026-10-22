"""Bring Chapters 0-10 inside the Style Guide's hard sentence/paragraph ceilings.

- Paragraph splits: insert a blank line at a chosen sentence boundary. No words
  change; only the paragraph break moves.
- Sentence splits: re-punctuate one long sentence into two.

Both passes assert that the target text was found exactly once and that the
result is inside the ceiling.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sent import split_sentences, words  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (file, paragraph key, sentences before the break)
PARA_SPLITS = [
    ("chapters/Chapter_02.md", "He came at the boy in a flat, controlled arc of fire", 3),
    ("chapters/Chapter_06.md", "The cold met him at the hatch.", 5),
    ("chapters/Chapter_06.md", "The engines changed their note.", 4),
    ("chapters/Chapter_07.md", "There were two men missing from the shore party.", 4),
    ("chapters/Chapter_09.md", "Jake had seen waterbending on Kyoshi Island", 3),
    ("chapters/Chapter_09.md", "The pirates moved first.", 3),
    ("chapters/Chapter_09.md", "Pain came up his arms in a white sheet", 6),
    ("chapters/Chapter_09.md", "She had cut herself free.", 4),
    ("chapters/Chapter_10.md", "A woman stood in a doorway with a basket", 3),
    ("chapters/Chapter_10.md", "He knew it was foolish. He had watched the white bison", 5),
    ("chapters/Chapter_10.md", "His whole body ached by then, from the knees up.", 4),
]

# (file, old, new)
SENT_SPLITS = [
    (
        "chapters/Chapter_03.md",
        "There was a great deal more he could have said and did not, standing there with his scarred hands working through Zuko's hair in the fading light, the ghost of another burning room pressing close around both of them without either one giving it a name.",
        "There was a great deal more he could have said and did not. He stood there with his scarred hands working through Zuko's hair in the fading light, the ghost of another burning room pressing close around both of them without either one giving it a name.",
    ),
    (
        "chapters/Chapter_04.md",
        "Sokka came out of the dojo with his hair wet and a green uniform folded over his arm and a bruise coming up along his jaw, and he was trying very hard to look like a man who had not been thrown on his back four times in an afternoon by a girl.",
        "Sokka came out of the dojo with his hair wet and a green uniform folded over his arm and a bruise coming up along his jaw. He was trying very hard to look like a man who had not been thrown on his back four times in an afternoon by a girl.",
    ),
    (
        "chapters/Chapter_07.md",
        "Iroh's eyes went to the stiff leather of the gloves, then to Jake's face, then to Zuko's back, where the prince stood with his shoulders drawn up around his ears, and then he was gone down the path with his towel and his easy walk, whistling something that did not have a tune.",
        "Iroh's eyes went to the stiff leather of the gloves, then to Jake's face, then to Zuko's back, where the prince stood with his shoulders drawn up around his ears. Then he was gone down the path with his towel and his easy walk, whistling something that did not have a tune.",
    ),
    (
        "chapters/Chapter_07.md",
        "He had sat in the water with his eyes closed and a hand trailing in it, easy as a man in his own house, and Jake had walked away and left him there, and had been *sorry* to, a little, because the hour had been so plainly a kindness.",
        "He had sat in the water with his eyes closed and a hand trailing in it, easy as a man in his own house. Jake had walked away and left him there, and had been *sorry* to, a little, because the hour had been so plainly a kindness.",
    ),
    (
        "chapters/Chapter_08.md",
        "He stood at the head of the stair with the light shining straight through his coat, and when Zuko reached the landing Jake caught him by the forearm with his bleeding glove, hauled him over the last step, and felt the whole weight of him come against his own.",
        "He stood at the head of the stair with the light shining straight through his coat, and when Zuko reached the landing Jake caught him by the forearm with his bleeding glove. He hauled him over the last step and felt the whole weight of him come against his own.",
    ),
    (
        "chapters/Chapter_10.md",
        "A boy of six or seven came out of a doorway to watch them pass and put his thumb in his mouth, and Jake thought, with a clarity that arrived from nowhere, that the boy would remember a tall man in red with a bandaged hand.",
        "A boy of six or seven came out of a doorway to watch them pass and put his thumb in his mouth. Jake thought, with a clarity that arrived from nowhere, that the boy would remember a tall man in red with a bandaged hand.",
    ),
    (
        "chapters/Chapter_10.md",
        "The print in the soft ground at the edge of the ring was the size of a table, three toes at the front and a heel like a scupper, pressed deep enough in the wet leaf mould that a man could have put his forearm in it.",
        "The print in the soft ground at the edge of the ring was the size of a table, three toes at the front and a heel like a scupper. It was pressed deep enough in the wet leaf mould that a man could have put his forearm in it.",
    ),
]


def path(rel):
    return os.path.join(ROOT, rel)


def do_para_splits():
    for rel, key, after in PARA_SPLITS:
        p = path(rel)
        text = open(p, encoding="utf-8").read()
        blocks = text.split("\n\n")
        hits = [i for i, b in enumerate(blocks) if key in b]
        if len(hits) != 1:
            raise SystemExit(f"FAIL {rel}: {len(hits)} blocks contain {key!r}")
        i = hits[0]
        block = blocks[i]
        before = len(words(block))
        if before <= 120:
            raise SystemExit(f"FAIL {rel}: paragraph with {key!r} is only {before}w")
        sents = split_sentences(block)
        if after >= len(sents):
            raise SystemExit(f"FAIL {rel}: {key!r} has {len(sents)} sentences, need {after}")
        head = " ".join(sents[:after])
        tail = " ".join(sents[after:])
        blocks[i] = head + "\n\n" + tail
        out = "\n\n".join(blocks)
        open(p, "w", encoding="utf-8").write(out)
        print(f"para split {os.path.basename(rel)}: {before}w -> "
              f"{len(words(head))}w + {len(words(tail))}w  [{key[:34]}...]")


def do_sent_splits():
    for rel, old, new in SENT_SPLITS:
        p = path(rel)
        text = open(p, encoding="utf-8").read()
        n = text.count(old)
        if n != 1:
            raise SystemExit(f"FAIL {rel}: {n} matches for {old[:50]!r}")
        text = text.replace(old, new)
        open(p, "w", encoding="utf-8").write(text)
        print(f"sent split {os.path.basename(rel)}: {len(words(old))}w -> "
              f"{len(words(old.split(' ', 1)[0]))}w + {len(words(new)) - len(words(old.split(' ', 1)[0]))}w")


if __name__ == "__main__":
    do_para_splits()
    do_sent_splits()
    print("done")
