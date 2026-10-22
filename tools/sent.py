"""Sentence-accurate metrics for the Book 1 chapters.

The regex splitter used by tools/metrics.py misses boundaries where a sentence
ends in a closing quote (`." `, `!" `, `?' `), which silently glues dialogue to
the following narration. This module scans properly.

Usage: python3 tools/sent.py [chapter files...]
"""

import glob
import os
import re
import sys

WORD = re.compile(r"[A-Za-z0-9'’\-]+")
CLOSERS = '"\'”’)]}*_`\''
OPENERS = '"\'“‘([{'

SENT_END = re.compile(r'[.!?]+')


def split_sentences(text):
    """Split text into sentences, honouring closing quotes after terminal marks.

    Paragraph breaks and scene separators (a line of exactly `---`) are hard
    breaks, exactly as a reader or a word processor would treat them.
    """
    out = []
    for chunk in re.split(r'(?m)^[ \t]*-{3,}[ \t]*$|\n[ \t]*\n', text):
        out.extend(_split_chunk(chunk))
    return out


def _split_chunk(text):
    out = []
    start = 0
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch in '.!?':
            j = i
            while j < n and text[j] in '.!?':
                j += 1
            # absorb any closing quotes/brackets that belong to this sentence
            k = j
            while k < n and text[k] in CLOSERS:
                k += 1
            if k < n and text[k].isspace():
                nxt = k
                while nxt < n and text[nxt].isspace():
                    nxt += 1
                if nxt >= n:
                    i = k
                    break
                if text[nxt] in OPENERS or text[nxt].isupper() or text[nxt].isdigit():
                    seg = text[start:k]
                    if seg.strip():
                        out.append(seg.strip())
                    start = nxt
                    i = nxt
                    continue
            i = j
            continue
        i += 1
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return out


def words(text):
    return WORD.findall(text)


def paragraphs(text):
    out = []
    for p in text.split('\n\n'):
        p = p.strip()
        if not p or p == '---' or p.startswith('#'):
            continue
        out.append(p)
    return out


def report(path):
    text = open(path, encoding='utf-8').read()
    sents = split_sentences(text)
    lens = [len(words(s)) for s in sents]
    paras = paragraphs(text)
    plens = [len(words(p)) for p in paras]
    dlg = [p for p in paras if p[0] in OPENERS]
    quoted = sum(len(words(s)) for s in re.findall(r'"([^"]*)"', text))
    n = len(lens)
    over = [(s, l) for s, l in zip(sents, lens) if l > 45]
    print(
        f"{os.path.basename(path):20} words={len(words(text)):5} sents={n:4} "
        f"avg={sum(lens)/n:5.2f} max={max(lens):3} >45={len(over):3} "
        f"paras={len(paras):4} >120={sum(1 for l in plens if l > 120):2} "
        f"dlg%={100*len(dlg)/len(paras):5.1f} quoted%={100*quoted/len(words(text)):5.1f}"
    )
    return over


if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob('chapters/*.md'))
    for f in files:
        if os.path.getsize(f) < 100:
            continue
        report(f)
