# Collect round-2 questions for Doru (nothing is changed here) -> scratchpad/round2q.json
import json, glob, os, collections, unicodedata
C = '/Users/dorutirlea/Business Ideas/letterlyn/packages/content/catalog/'
R2 = C + 'work/round2/'
S = os.path.dirname(os.path.abspath(__file__)) + '/'
shelves = json.load(open(C + 'shelves.json'))['shelves']
stitle = {s['id']: s['title']['en'] for s in shelves}
def g(w): return unicodedata.normalize('NFC', (w or '').upper()).replace(' ', '').replace('-', '').replace("'", '')
W = {}
for s in shelves:
    d = json.load(open(C + f"topics/{s['id']}.json"))
    for p in d['packs']:
        for t in p['topics']:
            w = t.get('words') or {}
            W[(s['id'], t['en'])] = [(e or '', r or '') for e, r in zip(w.get('en') or [None] * len(w.get('ro') or []), w.get('ro') or [])]
def inuse(sid, topic, en):
    return any(g(e) == g(en) for e, _ in W.get((sid, topic), []))

out = {}
# 1. re-rating: bad + headline (still in the words after the polish)
bad, head = [], []
for f in sorted(glob.glob(R2 + 'rerate-*/*.json')):
    X = json.load(open(f)); sid = X.get('shelf') or os.path.basename(f)[:-5]
    for fl in X.get('flags', []):
        if fl.get('flag') == 'weak': continue
        if not inuse(sid, fl.get('topic'), fl.get('en')): continue
        row = dict(shelf=stitle.get(sid, sid), pack=fl.get('pack'), topic=fl.get('topic'), en=fl.get('en'), ro=fl.get('ro'),
                   reason=fl.get('reason', ''), proposal=fl.get('proposal', ''))
        (bad if fl['flag'] == 'bad' else head).append(row)
out['bad'], out['headline'] = bad, head
# 2. translations
wrong, inc, ctx = [], [], 0
for f in sorted(glob.glob(R2 + 'trans-*/verdicts.json')):
    for v in json.load(open(f)):
        if 'contextCount' in v: ctx += v['contextCount']; continue
        row = dict(en=v.get('en'), now='; '.join(f"{ro}: {', '.join(pl[:4])}{' +' + str(len(pl) - 4) if len(pl) > 4 else ''}" for ro, pl in (v.get('ro_now') or {}).items()),
                   proposal=v.get('proposal', ''), reason=v.get('reason', ''))
        still = any(g(r) == g(ro) for (sid2, tt), prs in W.items() for e, r in prs if g(e) == g(v.get('en')) for ro in (v.get('ro_now') or {}))
        if not still: continue
        (wrong if v.get('verdict') == 'wrong' else inc).append(row)
out['wrong'], out['inconsistent'], out['contextCount'] = wrong, inc, ctx
# 3. same-subject topic pairs, shared words measured now
pr = json.load(open(R2 + 'polish-report.json'))
same = []
for v in pr['sameTopics']:
    (sa, ta), (sb, tb) = [x.split(' › ', 1) for x in (v['a'], v['b'])]
    A, B = W.get((sa, ta), []), W.get((sb, tb), [])
    sh = [e for e, _ in A if e and any(g(e) == g(x) for x, _ in B)]
    same.append(dict(a=f"{stitle.get(sa, sa)} › {ta}", b=f"{stitle.get(sb, sb)} › {tb}", shared=len(sh), words=' · '.join(sh),
                     change=v.get('change', ''), note=v.get('note', ''), proposal=v.get('proposal', '')))
same.sort(key=lambda x: -x['shared'])
out['same'] = same
out['polish'] = {k: pr[k] for k in ('targets', 'start', 'end', 'topicsChanged')}
json.dump(out, open(S + 'build/round2q.json', 'w'), ensure_ascii=False, indent=1)
print({k: (len(v) if isinstance(v, list) else v) for k, v in out.items()})
print('same by shared now:', collections.Counter(min(x['shared'], 10) for x in same))
