import re, sys, glob, os

def metrics(path):
    t = open(path, encoding='utf-8').read()
    # strip headers/scene breaks
    body = t
    words = re.findall(r"[A-Za-z0-9'’\-]+", body)
    n = len(words)
    paras = [p for p in body.split('\n\n') if p.strip() and not p.strip().startswith('#') and p.strip() != '---']
    paras = [p.strip() for p in paras]
    # sentence split
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z"“\'])', body)
    sents = [s for s in sents if re.search(r'[A-Za-z]', s)]
    slens = [len(re.findall(r"[A-Za-z0-9'’\-]+", s)) for s in sents]
    avg = sum(slens)/len(slens) if slens else 0
    over45 = [s for s,l in zip(sents,slens) if l>45]
    plens = [len(re.findall(r"[A-Za-z0-9'’\-]+", p)) for p in paras]
    over120 = [l for l in plens if l>120]
    dlg = [p for p in paras if p.lstrip().startswith('"') or p.lstrip().startswith('“')]
    dash = body.count('—') + body.count('–')
    way = len(re.findall(r'\bthe way\b', body, re.I))
    theway = len(re.findall(r'\bthe way (a|an|he|she|it|they|you|his|her|their|your|someone|somebody|a man|men)\b', body, re.I))
    notx = len(re.findall(r'\b(was|is|were|are) not [^.]{1,60}\.\s+It (was|is)\b', body))
    just = len(re.findall(r'\bnot (just|only)\b', body, re.I))
    quietly = len(re.findall(r'\bquietly\b', body, re.I))
    print(f"{os.path.basename(path):22} words={n:6} sents={len(sents):5} avg={avg:5.1f} max={max(slens) if slens else 0:3} >45={len(over45):3} paras={len(paras):4} avgP={sum(plens)/len(plens) if plens else 0:5.1f} >120={len(over120):3} dlg%={100*len(dlg)/max(len(paras),1):5.1f} dash/1k={1000*dash/max(n,1):4.1f} theway={way:3} notXbutY={notx:2} notjust={just:2} quietly={quietly:3}")
    return slens, sents

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob('chapters/*.md'))
    for f in files:
        if os.path.getsize(f) < 100: continue
        metrics(f)
