#!/usr/bin/env python3
"""Collect what is left after the automatic checklist round (25 Nov): questions for Doru (*-ask.json)
and changes the rules did not allow (*-ops.log.json) -> build/round3q.json for the catalogue page."""
import json, glob, os
S = os.path.dirname(os.path.abspath(__file__)) + '/'
R3 = '/Users/dorutirlea/Business Ideas/letterlyn/packages/content/catalog/work/round3/'
STEP = {'topics': 'Topics that repeat', 'bad': 'Bad words', 'wrong': 'Wrong Romanian', 'heads': 'First words'}
asks, fails = [], []
for f in sorted(glob.glob(R3 + '*-ask.json')):
    key = os.path.basename(f).split('-')[0]
    for x in json.load(open(f)):
        asks.append(dict(step=STEP.get(key, key), item=x))
for f in sorted(glob.glob(R3 + '*-ops.log.json')):
    key = os.path.basename(f).split('-')[0]
    for x in json.load(open(f)):
        if x.get('result') != 'ok':
            fails.append(dict(step=STEP.get(key, key), shelf=x.get('shelf'), topic=x.get('topic'), what=x.get('out') or x.get('en'), why=x.get('why', ''), note=x.get('note', '')))
json.dump({'asks': asks, 'fails': fails}, open(S + 'build/round3q.json', 'w'), ensure_ascii=False, indent=1)
print('asks', len(asks), 'fails', len(fails))
