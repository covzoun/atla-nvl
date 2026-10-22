"""Final verification scan for the Book 1 revision pass.

Reports, per chapter:
  words, dashes per 1k, "the way" constructions, not-X-but-Y contrasts,
  "not just/only ... but", and stock Humanizer vocabulary.
Then reports cross-chapter repeated phrases (5-grams appearing in two or
more chapters), which is the duplicate scan from the revision plan.
"""

import glob
import os
import re
import sys
from collections import defaultdict

WORD = re.compile(r"[A-Za-z0-9'’\-]+")


def words(t):
    return WORD.findall(t)


def chapter_metrics(path):
    t = open(path, encoding='utf-8').read()
    n = len(words(t))
    dash = t.count('—') + t.count('–')
    way = len(re.findall(r'\bthe way\b', t, re.I))
    split = len(re.findall(r'\bnot\b[^.?!]{0,60}[.!?,]\s+(?:And\s+)?(?:It|He|She|That|There|This)\b', t))
    notjust = len(re.findall(r'\bnot (?:just|only)\b', t, re.I))
    stock = len(re.findall(r'\b(quietly|landscape|momentarily|somewhat|underscore|testament|showcase)\b', t, re.I))
    print(f"{os.path.basename(path):18} words={n:5} dash/1k={1000*dash/max(n,1):4.1f} "
          f"theway={way:3} notX-butY={split:3} notjust={notjust:3} stock={stock:3}")


def ngram_scan(paths, n=5, min_chapters=2):
    seen = defaultdict(set)
    for p in paths:
        t = open(p, encoding='utf-8').read()
        w = [x.lower() for x in words(t)]
        for i in range(len(w) - n + 1):
            seen[' '.join(w[i:i + n])].add(os.path.basename(p))
    hits = {k: v for k, v in seen.items() if len(v) >= min_chapters}
    return hits


if __name__ == '__main__':
    files = [f for f in sorted(glob.glob('chapters/*.md')) if os.path.getsize(f) >= 100]
    print("===== per-chapter ceilings =====")
    for f in files:
        chapter_metrics(f)
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    print(f"\n===== cross-chapter repeated {n}-grams =====")
    hits = ngram_scan(files, n)
    for k, v in sorted(hits.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"  {sorted(v)}  ::  {k}")
    print(f"\n{len(hits)} repeated {n}-grams")
