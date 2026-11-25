#!/usr/bin/env python3
"""Measure every shelf (variety + rating mix) into build/shelf-metrics-all.json for the catalogue page."""
import json, subprocess, sys, os
S = os.path.dirname(os.path.abspath(__file__)) + '/'
CONTENT = '/Users/dorutirlea/Business Ideas/letterlyn/packages/content/'
sys.path.insert(0, CONTENT + 'scripts/wordfill'); from shelf_metrics import metrics
M = {}
for sid in [x['id'] for x in json.load(open(CONTENT + 'catalog/shelves.json'))['shelves']]:
    m = metrics(sid)
    q = subprocess.run(['python3', CONTENT + 'scripts/wordfill/quality.py', sid], capture_output=True, text=True).stdout.strip().splitlines()
    M[sid] = {'metrics': {L: dict(slots=m[L]['slots'], distinct=m[L]['distinct'], ratio=round(m[L]['ratio'], 2), maxw=m[L]['max'][0], max=m[L]['max'][1]) for L in m},
              'quality': json.loads(q[-1]) if q and q[-1].startswith('{') else None}
json.dump(M, open(S + 'build/shelf-metrics-all.json', 'w'), ensure_ascii=False, indent=1)
print('shelves measured:', len(M))
