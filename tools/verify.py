import re, sys, glob, os

def words(t):
    return re.findall(r"[A-Za-z0-9'’\-]+", t)

def report(path):
    t = open(path, encoding='utf-8').read()
    name = os.path.basename(path)
    lines = t.split('\n')
    # long paragraphs
    print(f"\n===== {name} =====")
    for i, p in enumerate(t.split('\n\n')):
        p = p.strip()
        if not p or p.startswith('#') or p == '---':
            continue
        n = len(words(p))
        if n > 120:
            print(f"  [PARA {n}w] {p[:160]}...")
    # long sentences: split inside each paragraph only, so paragraph breaks
    # are never glued into a single false sentence
    sents = []
    for p in t.split('\n\n'):
        p = p.strip()
        if not p or p.startswith('#') or p == '---':
            continue
        sents += [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"“\'])', p) if re.search(r'[A-Za-z]', s)]
    for s in sents:
        n = len(words(s))
        if n > 45:
            print(f"  [SENT {n}w] {s[:180]}...")
    # "the way"
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r'\bthe way\b', line, re.I):
            s = max(0, m.start()-60)
            print(f"  [WAY L{i}] ...{line[s:m.end()+70]}...")

if __name__ == '__main__':
    for f in (sys.argv[1:] or sorted(glob.glob('chapters/*.md'))):
        if os.path.getsize(f) < 100:
            continue
        report(f)
