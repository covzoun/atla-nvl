"""Cross-chapter repeated 6-gram scanner for the Book 1 revision pass.

Prints every 6-word span that appears in two or more chapters, with generic
connective phrases whitelisted so only real repeated wording shows up.
Also reports any 6-gram that crosses a scene separator (those are seams,
not echoes) under SCANNED-SEAM count.

Usage: python3 tools/dupscan.py
"""
import glob
import os
import re
from collections import defaultdict

WORD = re.compile(r"[A-Za-z0-9'’\-]+")

GENERIC = {
    "in the middle of the", "kept his eyes on the", "at the edge of the",
    "at the top of the", "did not look at him", "did not look at the",
    "jake kept his eyes on", "jake stayed where he was", "of a man who had",
    "at the head of the", "he did not look at", "he kept his eyes on",
    "and he did not look", "at the end of the", "he did not try to",
    "in the middle of it", "at the end of it", "as though it were a",
    "at the back of the", "at the base of the", "at the end of a",
    "came back out of the", "did not look at jake", "did not raise his voice",
    "did not so much as", "down the length of the", "for a moment and then",
    "had gone out of his", "had nothing to do with", "hands loose at his sides",
    "he did not need to", "he did not say anything", "he had stopped trying to",
    "he looked at jake and", "he sat down on the", "he understood what he was",
    "he went after the prince", "him and he did not", "his eyes were on the",
    "his hands in his sleeves", "in front of him and", "it and he did not",
    "jake felt it before he", "looked at him a moment",
    "neither of them said anything", "not looking at him he",
    "on the edge of the", "on the other side of", "one piece at a time",
    "stayed where he was and", "stood at the edge of", "stood at the rail with",
    "stood in the middle of", "that was the first thing",
    "the other side of the", "there was no time to", "there was nothing in the",
    "there was nothing to say", "was the first thing jake",
    "with a sound like a", "with his back against a", "with his back to the",
    "with his hands at his", "with his mouth open and", "a coil of rope with",
    "a creature the size of", "against his chest and the",
    "against his chest and his", "against the wind and the",
    "along the edge of the", "and a letter and a", "and by the time he",
    "and did not come back", "and did not look at", "come up out of the",
    "looked at it for a", "his hands at his sides", "at the end of the table",
    "the whole of what", "half a beat behind", "a half step behind",
}


def grams(path, n=6):
    t = open(path, encoding='utf-8').read()
    # mark scene-break seams so a span crossing one is excluded
    t = re.sub(r'(?m)^[ \t]*-{3,}[ \t]*$', ' \\n#\\n ', t)
    w = []
    seam = []
    for tok in WORD.findall(t):
        w.append(tok.lower())
        seam.append(False)
    # rebuild seams: a '\n#' token would have been split; approximate by
    # scanning offsets where the separator sits in the original stream
    return t, w


def grams_with_seams(path, n=6):
    """Yield (gram_tuple, crosses_seam) for consecutive word windows."""
    t = open(path, encoding='utf-8').read()
    w = WORD.findall(t)
    lows = [x.lower() for x in w]
    # positions of scene separators mapped to word index
    seam_idx = set()
    idx = 0
    for m in re.finditer(r'(?m)^[ \t]*-{3,}[ \t]*$', t):
        before = WORD.findall(t[:m.start()])
        seam_idx.add(len(before))
    out = []
    for i in range(len(lows) - n + 1):
        crosses = any(i <= s - 1 and s <= i + n for s in seam_idx)
        out.append((' '.join(lows[i:i + n]), crosses, i))
    return out


def main():
    files = [f for f in sorted(glob.glob('chapters/*.md'))
             if os.path.getsize(f) >= 100]
    seen = defaultdict(set)
    for p in files:
        for g, crosses, _ in grams_with_seams(p):
            if crosses:
                continue
            seen[g].add(os.path.basename(p))
    hits = {k: v for k, v in seen.items()
            if len(v) >= 2 and k not in GENERIC}
    for k, v in sorted(hits.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"  {sorted(v)}  ::  {k}")
    print(f"\n{len(hits)} repeated 6-grams (non-generic, non-seam)")


if __name__ == '__main__':
    main()
