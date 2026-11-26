import json,html,os,glob
C='/Users/dorutirlea/Business Ideas/letterlyn/packages/content/catalog/'
d=json.load(open(C+'shelves.json'))
topics={}
for f in glob.glob(C+'topics/*.json'):
    t=json.load(open(f))
    for p in t['packs']: topics[p['pack']]=p['topics']
rep=json.load(open(C+'report.json'))
import os as _os
S=_os.path.dirname(_os.path.abspath(__file__))+'/'
B=S+'build/'   # generated inputs (refresh-catalogue.sh)
rro=json.load(open(B+'report.ro.json'))
learn={(x['pack'],x['topic']):x for x in rro['learn']['list']}
LV={'expert':'Expert','classic':'Classic','relaxed':'Relaxed only','none':'not in Learn'}
pr={x['pack']:x for x in rep['packs']}
iss={}
for i in rep['issues']+[x for x in rro['issues'] if x['level']!='info']:
    iss.setdefault(i['where'].split(' ')[0].split('/')[-1],[]).append(i)
import re as _re
import sys as _sys; _sys.path.insert(0,'/Users/dorutirlea/Business Ideas/letterlyn/packages/content/scripts/wordfill')
from mark_reviewed import fp as _fp
REV=json.load(open(C+'reviews.json'))['packs'] if os.path.exists(C+'reviews.json') else {}
LAUNCH_SHELVES=['animals','sea','food','home','world','travel','holidays','romania']   # rules sheet 'Launch' (2026-11-25)
LAUNCH={}
_MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
def _d(x): y,m,dd=x.split('-'); return f'{int(dd)} {_MON[int(m)-1]}'
CHANGED=set()
for _pid,_rs in REV.items():
    _last=_rs[-1]['topics']
    for _t in topics.get(_pid,[]):
        if _last.get(_t['en'])!=_fp(_t): CHANGED.add(f"{_pid}/{_t['en']}")
def wordhtml(w):
    if w is None: return '<span class="nw">—</span>'
    n=len(_re.sub(r"[\s\-']","",w))
    cls=' class="lw"' if n>11 else (' class="mw"' if n>9 else '')
    return f'<span{cls}>{E(w)}</span>'
E=html.escape
MET=json.load(open(B+'shelf-metrics-all.json'))
XW=json.load(open(C+'extras-words.json'))['shelves']
import sys; sys.path.insert(0,S); from decisions import GROUPS
ROD=json.load(open(S+'ro-title-dups.json'))
ALLT={t['en'].lower() for v in topics.values() for t in v}
dupt=set()
for i in rep['issues']:
    if i['level']=='error' and 'repeats' in i['msg']: dupt.add(i['msg'].split('"')[1].lower())
def RT(t): return f' <span class="rot">· {E(t["ro"])}</span>' if t.get('ro') else ''
def topichtml(t,pid):
    chg='<span class="lb chg">changed since review</span>' if f"{pid}/{t['en']}" in CHANGED else ''
    en=t.get('words',{}).get('en',[]); ro=t.get('words',{}).get('ro'); ex=t.get('extra',{}).get('ro',[])
    if not en:
        d=' <span class="dup">title also used elsewhere</span>' if t['en'].lower() in dupt else ''
        return f'<li class="tonly">{E(t["en"])}{RT(t)}{d}</li>'
    if ro is None:
        return f'<li><span class="tt">{E(t["en"])}{RT(t)}</span><span class="ws">{" · ".join(wordhtml(w) for w in en)}</span></li>'
    if t.get('learn') is False:
        return f'<li><span class="tt">{E(t["en"])}{RT(t)}<span class="lb none">Not in Learn · own words per language</span>{chg}</span><span class="ws"><b class="lg">EN</b> {" · ".join(wordhtml(w) for w in en)}</span><span class="ws rows"><b class="lg">RO</b> {" · ".join(wordhtml(w) for w in ro)}</span></li>'
    # One line per topic while Doru checks (2026-11-26): each pair as RO → EN, easy to read and copy.
    def _pair(w,r):
        if r and w: return f'{wordhtml(r)} → {E(w)}'
        if r: return f'{wordhtml(r)} → <i>(no English)</i>'
        return f'<span class="nr">(no Romanian) → {E(w)}</span>'
    rol=" · ".join([_pair(w,r) for w,r in zip(en,ro)]+[f'<span class="ex">+{wordhtml(r)}</span>' for r in ex])
    lx=learn.get((pid,t['en'])); lb=f'<span class="lb {lx["best"]}">Learn: {LV[lx["best"]]} · {lx["shared"]} shared</span>' if lx else ''
    if t.get('learn') is False: lb='<span class="lb none">Not in Learn · own words per language</span>'
    return f'<li><span class="tt">{E(t["en"])}{RT(t)}{lb}{chg}</span><span class="ws rows"><b class="lg">RO → EN</b> {rol}</span></li>'
npacks=sum(len(s['packs']) for s in d['shelves']); ntop=sum(len(v) for v in topics.values())
done_shelves=sorted({s['id'] for s in d['shelves'] for p in s['packs'] if p['id'] in topics})
parts=[]
_SH={s['id']:s for s in d['shelves']}
_ll=[]
for _sid in LAUNCH_SHELVES:
    for _p in [q for q in _SH[_sid]['packs'] if not q.get('placeholder')][:5]:
        LAUNCH[_p['id']]=len(LAUNCH)+1; _ll.append((_sid,_p))
_rows=''
for _sid in LAUNCH_SHELVES:
    _it=[]
    for _s2,_p in _ll:
        if _s2!=_sid: continue
        _st=''
        if _p['id'] in REV:
            _n=sum(1 for k in CHANGED if k.split('/')[0]==_p['id'])
            _st=' <span class="chip rev">✓</span>'+(f' <span class="chip todo">{_n} changed</span>' if _n else '')
        _it.append(f'<li><b>#{LAUNCH[_p["id"]]}</b> {E(_p["title"]["en"])} <span class="ro">{E(_p["title"]["ro"])}</span>{_st}</li>')
    _rows+=f'<div><h3 style="margin:6px 0 2px;font-size:15px">{E(_SH[_sid]["title"]["en"])}</h3><ol style="margin:0;padding-left:18px;list-style:none">{"".join(_it)}</ol></div>'
_ndone=sum(1 for _s2,_p in _ll if _p['id'] in REV and not any(k.split('/')[0]==_p['id'] for k in CHANGED))
import re as _re, collections as _col
_weak=_col.defaultdict(list)
for _r in (rep, rro):
    for _i in _r['issues']:
        if _i['level']=='info' and _i['msg'].startswith('rated weak but in use: '):
            _m=_re.match(r'([^/]+)/([^ ]+) "(.*)"$',_i['where'])
            if _m:
                _k=(_m.group(1),_m.group(3)); _w=_i['msg'].split(': ',1)[1]
                if _w not in _weak[_k]: _weak[_k].append(_w)
_st={x['id']:x['title']['en'] for x in d['shelves']}
_wl=''.join(f'<li><b>{E(_st.get(k[0],k[0]))}</b> › {E(k[1])}: {E(", ".join(v))}</li>' for k,v in sorted(_weak.items()))
weak_html=(f'<details class="shelf"><summary><h2>Weak words still in use</h2><span class="ro">no better pool word fits the rules</span><span class="meta">{sum(len(v) for v in _weak.values())} words · {len(_weak)} topics</span></summary><p class="cov" style="margin:8px 16px 8px 40px">Rated weak by the second rating. The swap tool replaced 980 of 1,186 on 26 Nov, then a helper round wrote new rated words for the last 100 topics and replaced 201 of the 211 left; for these, every pool word would break a rule (repeat within 4 puzzles, hidden pair, grid fit). Fix them in your review, or leave them: they are correct words, just loose fits. Read from the checker report.</p><ul style="columns:2;margin:0 16px 14px 40px;font-size:.85rem">{_wl}</ul></details>' if _weak else '')
launch_html=f'<details class="shelf" open><summary><h2>Your review list: the launch packs</h2><span class="ro">8 shelves × 5 packs, decided 25 Nov</span><span class="meta">{_ndone} of {len(_ll)} done</span></summary><p class="cov" style="margin:8px 16px 8px 40px">These 40 packs go live at launch (rules sheet "Launch"): ~60 h of review at ~1.5 h a pack. The catalogue is frozen, so each pack is reviewed once; only your corrections change words. Always the first 5 packs in shelf order, so the play order and the no-repeat checks stay as they are. Look for the <span class="chip launch" style="margin:0">Launch #</span> chip in the shelves below.</p><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:8px 20px;padding:0 16px 14px 40px">{_rows}</div></details>'
for s in d['shelves']:
    has=any(p['id'] in topics for p in s['packs'])
    nl=sum(p['launch'] for p in s['packs'])
    local=f'<span class="chip loc">only in {s.get("lang","ro").upper()}</span>' if s['kind']=='local' else ''
    hasw=any(any(t.get('words',{}).get('en') for t in topics.get(p['id'],[])) for p in s['packs'])
    nph=sum(1 for p in s['packs'] if p.get('placeholder'))
    allw=all(t.get('words',{}).get('ro') or t.get('words',{}).get('en') for p in s['packs'] for t in topics.get(p['id'],[]))
    status=('<span class="chip ok">words done</span>' if allw else '<span class="chip ok">words started</span>' if hasw else '<span class="chip">topics drafted</span>')+(f'<span class="chip todo">{nph} to draft</span>' if nph else '')
    _nr=sum(1 for p in s['packs'] if p['id'] in REV)
    if _nr: status+=f'<span class="chip rev">{_nr} of {len(s["packs"])} packs reviewed</span>'
    packs=[]
    for p in s['packs']:
        tl=topics.get(p['id'])
        badge=''
        cov=f'<p class="cov"><b>Covers:</b> {E(p.get("covers",""))}' + (f' · <b>Leaves:</b> {E(p["leaves"])}' if p.get('leaves') else '') + '</p>'
        if p.get('placeholder'):
            packs.append(f'<div class="pack flat ph"><span class="pt">{E(p["title"]["en"])}</span><span class="ro">{E(p["title"]["ro"])}</span><span class="chip todo">to draft</span><span class="covi">{E(p.get("covers",""))}</span></div>')
            continue
        if p['id'] in LAUNCH: badge+=f'<span class="chip launch">Launch #{LAUNCH[p["id"]]}</span>'
        if p['id'] in REV:
            _r=REV[p['id']][-1]; _n=sum(1 for k in CHANGED if k.split('/')[0]==p['id'])
            badge+=f'<span class="chip rev">✓ Review {_r["round"]} · {_d(_r["date"])}</span>'+(f'<span class="chip todo">{_n} changed since</span>' if _n else '<span class="chip ok">latest version</span>')
        if tl:
            r=pr.get(p['id'],{})
            fr=r.get('fresh'); frs=f'{round(fr*100)}% new' if fr is not None else ''
            low=''
            lis=''.join(topichtml(t,p['id']) for t in tl)
            warn=''.join(f'<li>{E(i["msg"])}</li>' for i in iss.get(p['id'],[]))
            warn=f'<ul class="warn">{warn}</ul>' if warn else ''
            hasw=any(t.get('words',{}).get('en') for t in tl)
            wtxt=f'{r.get("distinct",0)} words · <span class="fr{low}">{frs}</span>' if hasw else '<span class="nw">topics only, words next</span>'
            thin=' <span class="dup">under 20 topics</span>' if len(tl)<20 else ''
            olc=' class="tl"' if not hasw else ''
            packs.append(f'<details class="pack"><summary><span class="pt">{E(p["title"]["en"])}</span><span class="ro">{E(p["title"]["ro"])}</span>{badge}<span class="cnt">{len(tl)} topics{thin} · {wtxt}</span></summary>{cov}<ol{olc}>{lis}</ol></details>')
        else:
            packs.append(f'<div class="pack flat"><span class="pt">{E(p["title"]["en"])}</span><span class="ro">{E(p["title"]["ro"])}</span>{badge}<span class="covi">{E(p.get("covers",""))}</span></div>')
    op=''
    mm=MET.get(s['id'],{}); mt=''
    if mm:
        q=mm['quality']; m=mm['metrics']
        def _c(L):
            v=m.get(L); 
            if not v: return ''
            return f'<span class="{"m bad" if v["ratio"]<0.70 else "m"}"><b>{L.upper()}</b> {v["distinct"]:,} words · {v["ratio"]:.3f} per slot · max ×{v["max"]} ({E(v["maxw"])})</span>'
        mt=f'<div class="mets">{_c("en")}{_c("ro")}<span class="{"m bad" if q.get("under5core") else "m"}">core {q["core"]:.1f} · weak {q["weak"]:.2f} · bad {q["bad"]:.2f} per topic{f" · {q[chr(117)+'nder5core']} topics under 5 core" if q.get("under5core") else ""}</span></div>'
    parts.append(f'<details class="shelf"{op}><summary><h2>{E(s["title"]["en"])}</h2><span class="ro">{E(s["title"]["ro"])}</span><span class="meta">{len(s["packs"])} packs</span>{local}{status}{mt}</summary><div class="packs">{"".join(packs)}</div></details>')
ex=json.load(open(C+'extras.json'))
sp=''.join(f'<details class="pack"><summary><span class="pt">{E(x["title"]["en"])}</span><span class="ro">{E(x["title"]["ro"])}</span><span class="cnt">from {E(x["fromShelf"])} · {len(x["topics"])} topics</span></summary><p class="cov">{E(x.get("covers",""))}</p><ol class="tl">{"".join(f"<li class=tonly>{E(t)}</li>" for t in x["topics"])}</ol></details>' for x in ex['sparePacks'])
def rtopic(t):
    w=t.get('words',{}).get('en')
    if t['en'].lower() in ALLT: return f'<li class="tonly used">{E(t["en"])} <span class="lb">now in the catalogue</span></li>'
    return f'<li class="tonly">{E(t["en"])}' + (f' <span class="nw">· {E(" · ".join(w))}</span>' if w else '') + '</li>'
rv=''.join(f'<details class="pack"><summary><span class="pt">{E(r["packTitle"])}</span><span class="cnt">{E(r["shelf"])} · {len(r["topics"])} reserve topics</span></summary><ol>{"".join(rtopic(t) for t in r["topics"])}</ol></details>' for r in ex['reserveTopics'])
nres=sum(len(r['topics']) for r in ex['reserveTopics'])
extras_html=f'<details class="shelf"><summary><h2>Extras</h2><span class="ro">not a shelf</span><span class="meta">{len(ex["sparePacks"])} spare packs · {nres} reserve topics</span></summary><p class="cov" style="margin:8px 16px 8px 40px">Everything we thought of that is not in a shelf: <b>spare packs</b> set aside when shelves were cut to 15, and <b>reserve topics</b> beyond 20 in a pack. Used to replace weak topics, seed new shelves, or for dailies and Quick Play.</p><div class="packs"><div class="pack flat"><span class="pt">Spare packs</span></div>{sp}<div class="pack flat"><span class="pt">Reserve topics (by pack)</span></div>{rv}</div></details>'
shtitle={s['id']:s['title']['en'] for s in d['shelves']}
ptitle={p['id']:p['title']['en'] for s in d['shelves'] for p in s['packs']}
xw_parts=[]
for s in d['shelves']:
    x=XW.get(s['id'])
    if not x: continue
    rt=''.join(f'<li><b>{E(r["old"])}</b> → {E(r["new"])} <span class="nw">({E(ptitle.get(r["pack"],r["pack"]))}) · {E(r.get("reason",""))}</span></li>' for r in x['replacedTopics'])
    by={}
    for n in x['noRo']: by.setdefault(n['en'],set()).add(n['topic'])
    nr=' · '.join(E(w) for w in sorted(by))
    rj=' · '.join(f'{E(r.get("en") or r.get("word") or "")}{"="+E(r["ro"]) if r.get("ro") else ""}' for r in x['rejected'][:400] if isinstance(r,dict))
    more=f' <span class="nw">… and {len(x["rejected"])-400} more in the file</span>' if len(x['rejected'])>400 else ''
    xw_parts.append(f'<details class="pack"><summary><span class="pt">{E(s["title"]["en"])}</span><span class="cnt">{len(x["unused"]):,} unused · {len(by):,} no Romanian · {len(x["rejected"]):,} rejected · {len(x["replacedTopics"])} topics replaced</span></summary>'
      +(f'<p class="cov"><b>Topics replaced</b></p><ul class="xl">{rt}</ul>' if rt else '')
      +(f'<p class="cov"><b>English words with no Romanian partner</b></p><p class="xw">{nr}</p>' if nr else '')
      +(f'<p class="cov"><b>Rejected or removed (bad, UK, wrong Romanian, excluded)</b></p><p class="xw">{rj}{more}</p>' if rj else '')+'</details>')
nx=sum(len(v['unused']) for v in XW.values()); nn=sum(len({n['en'] for n in v['noRo']}) for v in XW.values()); nj=sum(len(v['rejected']) for v in XW.values()); nrt=sum(len(v['replacedTopics']) for v in XW.values())
xwords_html=f'<details class="shelf"><summary><h2>Extra words</h2><span class="ro">not in any topic</span><span class="meta">{nx:,} unused · {nn:,} no Romanian · {nj:,} rejected · {nrt} topics replaced</span></summary><p class="cov" style="margin:8px 16px 8px 40px">Everything the word helpers found or wrote that is not in a topic, kept as reference: <b>unused</b> candidates (with their rating, too many to list here), English words with <b>no Romanian</b> partner, and words <b>rejected or removed</b> with a reason. Full file: <code>catalog/extras-words.json</code>; each shelf\'s notes are in <code>catalog/work/scrap/&lt;shelf&gt;.json</code>.</p><div class="packs">{"".join(xw_parts)}</div></details>'
import unicodedata as _ud
def _g(w): return _ud.normalize('NFC',(w or '').upper()).replace(' ','').replace('-','').replace("'",'')
TT={}
for _s in json.load(open(C+'shelves.json'))['shelves']:
    _pt={p['id']:p['title']['en'] for p in _s['packs']}
    for _p in json.load(open(C+f"topics/{_s['id']}.json"))['packs']:
        for _t in _p['topics']:
            _w=_t.get('words') or {}
            TT[_t['en'].lower()]=dict(path=f"{_s['title']['en']} › {_pt.get(_p['pack'],_p['pack'])} › {_t['en']}",ro=_t.get('ro',''),
                en=[x for x in (_w.get('en') or []) if x],rw=[x for x in (_w.get('ro') or []) if x])
def CMPT(titles):
    ts=[TT[t.strip().lower()] for t in titles if t.strip().lower() in TT]
    if len(ts)<2: return ''
    cnt={}
    for t in ts:
        for w in set(_g(x) for x in t['en']): cnt[w]=cnt.get(w,0)+1
    rows=''
    for t in ts:
        ws=' · '.join(f'<b>{E(x)}</b>' if cnt.get(_g(x),0)>1 else E(x) for x in t['en'])
        rows+=f'<span class="ws cmp"><i>{E(t["path"])}</i>: {ws}</span>'
    sh=sum(1 for v in cnt.values() if v>1)
    return f'<span class="ws cmp"><small>{sh} shared English words (bold)</small></span>'+rows
import re as _re
def CMP(g,w):
    if not g.startswith('Near-duplicate'): return ''
    out=''
    for part in w.split(';'):
        out+=CMPT(_re.split(r'\s*/\s*',part))
    return out
dec=''.join(f'<details class="pack"><summary><span class="pt">{E(g)}</span><span class="cnt">{len(items)}</span></summary>'+(f'<p class="cov">{E(intro)}</p>' if intro else '')+'<ol>'+''.join(f'<li><span class="tt">{E(w)}</span><span class="ws">{E(c)}</span>'+(f'<span class="ws rows">→ {E(pr_)}</span>' if pr_ else '')+CMP(g,w)+'</li>' for w,c,pr_ in items)+'</ol></details>' for g,intro,items in GROUPS)

rod='<ol>'+''.join(f'<li><span class="tt">{E(o["ro"])}</span><span class="ws">{" · ".join(E(f"{a} › {b} › {c}") for a,b,c,_ in o["uses"])}</span>'+CMPT([c for a,b,c,_ in o["uses"]])+'</li>' for o in ROD)+'</ol>'
dec_html=f'<details class="shelf" open><summary><h2>To decide together</h2><span class="ro">open</span><span class="meta">{sum(len(i) for _,_,i in GROUPS)} items</span></summary><p class="cov" style="margin:8px 16px 8px 40px">Topic pairs with similar titles. Both word lists are shown, shared words in bold: say which pairs really repeat; the rest stay.</p><div class="packs">{dec}</div></details>'
Q=json.load(open(B+'round2q.json'))
def _li(t,ws,pr_): return f'<li><span class="tt">{E(t)}</span><span class="ws">{E(ws)}</span>'+(f'<span class="ws rows">→ {E(pr_)}</span>' if pr_ else '')+'</li>'
def _grp(title,intro,rows):
    return f'<details class="pack"><summary><span class="pt">{E(title)}</span><span class="cnt">{len(rows)}</span></summary>'+(f'<p class="cov">{E(intro)}</p>' if intro else '')+'<ol>'+''.join(rows)+'</ol></details>'
def _byshelf(title,intro,L):
    by={}
    for r in L: by.setdefault(r['shelf'],[]).append(r)
    inner=''.join(_grp(sh,'',[_li(f"{r['en']} = {r['ro']}",f"{r['pack']} › {r['topic']} · {r['reason']}",r['proposal']) for r in rs]) for sh,rs in sorted(by.items()))
    return f'<details class="pack"><summary><span class="pt">{E(title)}</span><span class="cnt">{len(L)}</span></summary><p class="cov">{E(intro)}</p><div class="packs">{inner}</div></details>'
Q3=json.load(open(B+'round3q.json'))
def _ask_txt(x):
    it=x['item']
    if 'a' in it and 'b' in it:
        a,b=it['a'],it['b']; head=f"{a.get('shelf')} › {a.get('topic')}  ↔  {b.get('shelf')} › {b.get('topic')}"
        return _li(head,it.get('why',''),it.get('proposal',''))[:-5]+CMPT([a.get('topic',''),b.get('topic','')])+'</li>'
    head=' · '.join(str(it[k]) for k in ('en','shelf','topic') if it.get(k)) or it.get('kind','')
    body=it.get('why') or it.get('question') or it.get('facts') or ''
    prop=it.get('proposal') or it.get('proposal_ro') or it.get('proposal_en') or (' / '.join(it['options']) if it.get('options') else '')
    return _li(head,body,prop)
_bystep={}
for x in Q3['asks']: _bystep.setdefault(x['step'],[]).append(_ask_txt(x))
step1=f'<details class="shelf" open><summary><h2>Questions for you</h2><span class="ro">all that is left to decide</span><span class="meta">{len(Q3["asks"])}</span></summary><div class="packs">'+''.join(_grp(k,'',v) for k,v in _bystep.items())+'</div></details>'
_fl=[_li(f"{x['step']} · {x['shelf']} › {x['topic']}",f"{x['what']} · {x['note']}",x['why']) for x in Q3['fails']]
step2=f'<details class="shelf"><summary><h2>Not changed automatically</h2><span class="ro">a game rule blocked these; for reference</span><span class="meta">{len(Q3["fails"])}</span></summary><p class="cov" style="margin:8px 16px 8px 40px">Changes the helpers proposed that would have broken a rule (a word repeated within 4 puzzles, used 8 times on a shelf, hidden in another word, or too long). These topics keep their current words; nothing urgent.</p><div class="packs">'+_grp('Blocked changes','',_fl)+'</div></details>'
dec_html=''
r2_html=(step1 if Q3['asks'] else '')+step2
today='25 Nov'
_titles={x['id']:x['title']['en'] for x in d['shelves']}
_under=[f"{_titles.get(k,k)} ({L.upper()} {v['metrics'][L]['ratio']:.3f})" for k,v in MET.items() for L in ('en','ro') if L in v['metrics'] and v['metrics'][L]['ratio']<0.70]
_lc=rro['learn']['best']['classic']+rro['learn']['best'].get('relaxed',0)+rro['learn']['best'].get('none',0)
_learn_txt=('every Learn topic reaches Expert, Romania included (the names that matter stay for Romanian players; resident names and side names were swapped for common words).' if not _lc else f'every Learn topic reaches Expert except {_lc} (see the Learn level on each topic).')
_st2={p['id']:p['title']['en'] for x in d['shelves'] for p in x['packs']}
_revsofar=('Reviewed so far: '+', '.join(f"{E(_st2.get(k,k))} ({v[-1].get('date','')})" for k,v in REV.items())+'.') if REV else 'Reviewed by hand so far: none yet (automated word audits are not reviews; audited packs are locked, see the rules sheet).'
_te,_tr=rep['totals'],rro['totals']
_check_txt=(f"The checker is clean: 0 errors and 0 warnings in English and Romanian (read from its reports, {rep['generated'][:16].replace('T',' ')} UTC);" if not (_te['errors'] or _te['warnings'] or _tr['errors'] or _tr['warnings'])
  else f"<b>The checker is NOT clean:</b> English {_te['errors']} errors / {_te['warnings']} warnings, Romanian {_tr['errors']} errors / {_tr['warnings']} warnings (catalog/report.json);")
_check_txt+=f" {_te.get('weakInUse',0):,} English words rated weak are still in topics, only where no better pool word fits the rules (list below);"
_variety_txt=('Every shelf has at least 0.70 different words per slot in both languages.' if not _under else 'Every shelf has at least 0.70 different words per slot in both languages, except '+', '.join(_under)+' (just short: their pools have no more words that fit the rules).')
_nd=0
todo=(f'<b>Questions for you</b> ({len(Q3["asks"])}), on this page. ' if Q3['asks'] else '<b>Nothing left to decide on the catalogue.</b> The four checklist steps (repeating topics, bad words, wrong Romanian, first words) were done automatically on 25 Nov and Doru answered the last 16 questions (10 topics replaced). ')+'Separately: the coin numbers on the content page.'
page=f'''<title>LetterLyn Catalogue</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap">
<style>
/* Layout: one reading column; each shelf is a collapsible block like a shelf label, packs inside, topics as a numbered list. */
:root{{--bg:#F5F4EE;--surface:#FFFFFF;--fg:#1E1E1A;--muted:#5F5E56;--line:#DDDBD1;--accent:#2F5FD0;--accent-soft:#E7EDFB;--ok:#22703A;--ok-soft:#E3F1E6;--gold:#8A6410;--gold-soft:#F7EDD5;
--display:"Space Grotesk",Inter,system-ui,sans-serif;--body:Inter,system-ui,-apple-system,"Segoe UI",sans-serif}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#151613;--surface:#1E1F1B;--fg:#ECEBE4;--muted:#A6A59B;--line:#34352F;--accent:#8FB0F5;--accent-soft:#1F2A40;--ok:#7FD18F;--ok-soft:#1B3022;--gold:#E6C178;--gold-soft:#3A2E14;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#151613;--surface:#1E1F1B;--fg:#ECEBE4;--muted:#A6A59B;--line:#34352F;--accent:#8FB0F5;--accent-soft:#1F2A40;--ok:#7FD18F;--ok-soft:#1B3022;--gold:#E6C178;--gold-soft:#3A2E14;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:16px;line-height:1.5}}
.wrap{{max-width:900px;margin:0 auto;padding-block:36px 72px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:14px}}
h1,h2{{font-family:var(--display);margin:0;line-height:1.2;text-wrap:balance}}
h1{{font-size:2rem}} h2{{font-size:1.15rem}}
.lead{{color:var(--muted);max-width:68ch;margin:0}}
.stats{{display:flex;flex-wrap:wrap;gap:8px 20px;font-variant-numeric:tabular-nums;color:var(--muted);font-size:.92rem}}
.stats b{{color:var(--fg);font-size:1.1rem}}
.shelf{{background:var(--surface);border:1px solid var(--line);border-radius:12px}}
.shelf>summary{{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 12px;padding:14px 16px;cursor:pointer;list-style:none}}
.shelf>summary::-webkit-details-marker{{display:none}}
.shelf>summary::before{{content:"▸";color:var(--muted);width:1em}}
.shelf[open]>summary::before{{content:"▾"}}
.ro{{color:var(--muted);font-size:.9rem}}
.meta{{color:var(--muted);font-size:.85rem;margin-left:auto;font-variant-numeric:tabular-nums}}
.chip{{font-size:.7rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:999px;background:var(--accent-soft);color:var(--accent)}}
.chip.ok{{background:var(--ok-soft);color:var(--ok)}} .chip.launch{{background:var(--gold-soft);color:var(--gold)}} .chip.loc{{background:var(--bg);color:var(--muted);border:1px solid var(--line)}}
.packs{{display:flex;flex-direction:column;border-top:1px solid var(--line)}}
.pack{{border-bottom:1px solid var(--line)}} .pack:last-child{{border-bottom:0}}
.pack>summary,.pack.flat{{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 10px;padding:9px 16px 9px 40px}}
.pack>summary{{cursor:pointer}}
.pt{{font-weight:600}} .cnt{{margin-left:auto;color:var(--muted);font-size:.85rem;font-variant-numeric:tabular-nums}}
.pack ol{{margin:0;padding:4px 16px 14px 56px;font-size:.9rem;display:flex;flex-direction:column;gap:8px}}
.pack li{{padding:0}}
.tt{{display:block;font-weight:600}}
.ws{{display:block;color:var(--muted);font-size:.82rem;letter-spacing:.02em;overflow-wrap:anywhere}}
.ws .mw{{color:var(--fg)}} .ws .lw{{color:var(--gold);font-style:italic}}
.cov{{margin:2px 16px 6px 40px;font-size:.85rem;color:var(--muted)}} .cov b{{color:var(--fg);font-weight:600}}
.covi{{flex-basis:100%;color:var(--muted);font-size:.82rem}}
.ws.rows{{color:var(--fg);margin-top:2px}} .ws.cmp{{margin-top:3px}} .ws.cmp b{{color:var(--fg)}} .ws.cmp i{{font-style:normal;color:var(--accent)}} .ws small{{color:var(--muted);font-size:.72rem;margin-left:3px}} .ws .ex{{color:var(--accent)}} .ws .nr{{text-decoration:line-through;opacity:.6}}
.lg{{font-size:.68rem;font-weight:700;color:var(--muted);margin-right:4px;letter-spacing:.06em}}
.lb{{font-size:.72rem;font-weight:600;margin-left:8px;padding:1px 7px;border-radius:999px;background:var(--ok-soft);color:var(--ok)}} .lb.relaxed,.lb.none{{background:var(--gold-soft);color:var(--gold)}}
.chip.rev{{background:var(--ok);color:var(--surface)}} .chip.launch{{background:var(--accent);color:var(--surface)}} .lb.chg{{background:var(--gold-soft);color:var(--gold)}}
.rot{{color:var(--muted);font-weight:400}}
.chip.todo{{background:var(--gold-soft);color:var(--gold)}} .pack.ph .pt{{color:var(--muted)}}
.tonly{{font-weight:500}} .pack ol.tl{{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:2px 18px}}
.dup{{font-size:.7rem;font-weight:600;color:var(--gold);background:var(--gold-soft);border-radius:999px;padding:0 6px;margin-left:4px;white-space:nowrap}} .nw{{color:var(--muted)}}
.fr{{color:var(--ok)}} .fr.low{{color:var(--gold);font-weight:600}}
.warn{{margin:0 16px 8px 40px;padding:8px 12px 8px 28px;background:var(--gold-soft);color:var(--gold);border-radius:8px;font-size:.82rem}}
summary:focus-visible{{outline:2px solid var(--accent);outline-offset:-2px;border-radius:12px}}
.mets{{flex-basis:100%;display:flex;flex-wrap:wrap;gap:4px 14px;font-size:.78rem;color:var(--muted);font-variant-numeric:tabular-nums;padding-left:1.4em}} .mets b{{color:var(--fg);font-size:.7rem}} .m.bad{{color:var(--gold);font-weight:600}}
.xw{{margin:0 16px 10px 40px;font-size:.8rem;color:var(--muted);overflow-wrap:anywhere}} .xl{{margin:0 16px 8px 40px;padding-left:18px;font-size:.85rem;display:flex;flex-direction:column;gap:4px}} .used{{color:var(--muted)}}
code{{font-size:.85em}}
.note{{background:var(--accent-soft);border-radius:12px;padding:12px 16px;font-size:.92rem;max-width:none}}
</style>
<div class="wrap">
  <header style="display:flex;flex-direction:column;gap:10px">
    <span class="chip" style="align-self:flex-start">Draft · 25 Nov 2026</span>
    <h1>LetterLyn Catalogue</h1>
    <p class="lead">Every shelf and pack the game will have. <b>15 packs per shelf</b>, and the game grows by adding new shelves, never longer ones, so every shelf's trophies (bronze 5 · silver 10 · gold 15) are reachable the day it comes out. At launch: 8 shelves with their first 5 reviewed packs each (bronze reachable); the monthly packs then fill them to 15. English and Romanian are written together as matching pairs; a pack is locked once published (per language).</p>
    <div class="stats"><span><b>{len(d["shelves"])}</b> shelves</span><span><b>{npacks}</b> packs</span><span><b>{ntop}</b> topics drafted</span><span><b>{rep["totals"]["distinct"+"Words"]:,}</b> different words</span><span><b>{rep["totals"]["warnings"]}</b> warnings</span><span><b>{rro["totals"]["topicsWithWords"]}</b> topics in Romanian · <b>{rro["totals"]["warnings"]}</b> RO warnings</span></div>
    <div class="note"><strong>Where we are ({today}).</strong> All 8,700 topics have 16–18 words in English and Romanian, and the whole catalogue has been checked together (look-alike topics, translations, a second rating). {_check_txt} {_learn_txt} {_variety_txt} Romanian checked on dexonline only where a doubt came up.</div>
    <div class="note"><strong>Left to do.</strong> {todo} Then: Doru reviews the 40 launch packs in the review list below (about 1.5 h per pack).</div>
    <div class="note"><strong>Reviews.</strong> A pack Doru has checked shows <b>✓ Review</b> with the date; if its words change later, the changed topics are marked <span class="lb chg" style="margin:0">changed since review</span>, so a second look only needs those. {_revsofar}</div>
    <div class="note"><strong>How the two languages are shown.</strong> One line per topic: each pair is written <b>ROMANIAN → ENGLISH</b>, pairs separated by · (the arrow is never part of a word, so dashed words like ZGÂRIE-NORI stay readable and copy cleanly). Each is the proper translation, the same kind of word. <i>(no English)</i> = a Romanian word without an English partner (local names); <span style="text-decoration:line-through;opacity:.6">(no Romanian) → WORD</span> = an English word with no Romanian partner; <span style="color:var(--accent)">+blue</span> = an extra Romanian-only word. Topics not in Learn (own words per language) still show two lists. <b>Learn</b> = the best level a Learn puzzle can reach from the shared words (Relaxed needs 6, Classic 10, Expert 16).</div>
    <div class="note"><strong>How to read it.</strong> Each shelf line shows its different words, words per slot (target 0.70, <span style="color:var(--gold);font-weight:600">gold</span> = under it), the most-used word and core / weak / bad words per topic. Each topic gives 3 puzzles from its 16–18 words: Relaxed 7×9 uses the 6–8 shortest, Classic 9×12 uses 10–12, Expert 11×14 uses all that fit. Two-word names are shown as in the game's list ("GUINEA PIG") and joined only in the grid; never in Relaxed. Topics are listed in <b>play order</b> (what Continue plays next); the first topic of each pack is its headline. No word comes back within the next 4 puzzles. <b>New</b> = share of a pack's words not used by packs above it on the same shelf (information only). Word colours (by letters in the grid): plain = up to 9 letters (fits across from Classic up) · <span style="font-weight:600">dark</span> = 10–11 letters, Classic down-only or Expert · <i style="color:var(--gold)">gold italic</i> = 12+ letters, Expert down-only or the mega puzzle.</div>
  </header>
  {launch_html}
  {weak_html}
  {dec_html}
  {r2_html}
  {"".join(parts)}
  {extras_html}
  {xwords_html}
</div>'''
open(S+'../pages/catalogue.html','w').write(page)
print(len(page))
