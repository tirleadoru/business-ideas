# LetterLyn coin economy model (25 Nov; numbers on the content page "The math"). Run: python3 letterlyn-economy-model.py: earnings, spending, purchase power, per player type.
import json, sys

def model(F, P, verbose=False):
    # player types: per-day behaviour (Classic unless said), days played per week, hints per day, freezes bought per month
    players = {
        'Casual':  dict(days=5,   puzzles=3,  expert=0,   qp=0, tasks=1, ads=0, mystery=.5, nohint=.5, jars_wk=.5, league_wk=0,  hints=.7, freezes=0.5, lvl_speed=.5),
        'Regular': dict(days=6.5, puzzles=6,  expert=0,   qp=1, tasks=3, ads=1, mystery=.7, nohint=.6, jars_wk=1.5, league_wk=8, hints=.8, freezes=1,   lvl_speed=1),
        'Heavy':   dict(days=7,   puzzles=12, expert=.5,  qp=3, tasks=3, ads=3, mystery=.8, nohint=.8, jars_wk=3,  league_wk=40, hints=.4, freezes=1,  lvl_speed=2),
    }
    # level timeline for a regular player (weeks to reach level); others scale by lvl_speed
    lvl_weeks = {5: .5, 10: 1.5, 15: 3.5, 20: 7, 25: 12, 30: 18, 40: 34, 50: 55}
    out = {}
    for name, p in players.items():
        per_puzzle = (1 - p['expert']) * F['puzzle_classic'] + p['expert'] * F['puzzle_expert'] + p['mystery'] * F['mystery'] + p['nohint'] * F['nohint']
        streak_avg = min(F['daily_streak_cap'], 15)  # long-run streak bonus
        day = (F['daily'] + streak_avg * F['daily_per_streak_day']) + p['puzzles'] * per_puzzle + min(p['qp'], 3) * F['qp'] \
              + sum(F['tasks'][:p['tasks']]) + (F['tasks_all3'] if p['tasks'] == 3 else 0) + min(p['ads'], F['ads_max']) * F['ad']
        week = day * p['days'] + p['jars_wk'] * F['jar'] + p['league_wk']
        spend_wk = p['hints'] * 7 * F['hint_price'] * (p['days'] / 7) + p['freezes'] * P['freeze'] / 4.33
        # one-off bonuses in month 1 and month 3
        def lvl_bonus(weeks):
            tot = 0
            for lv in range(2, 61):
                w = next((lvl_weeks[k] for k in sorted(lvl_weeks) if k >= lv), 80) / p['lvl_speed']
                if w <= weeks:
                    tot += F['level'] + (F['lvl5'] if lv % 5 == 0 else 0) + (F['lvl_10_25_50'] if lv in (10, 25, 50) else 0) + (F['lvl_20_40'] if lv in (20, 40) else 0)
            return tot
        def streak_bonus(weeks):
            if p['days'] < 6: return F['streak_goals'][0] if weeks >= 2 else 0   # casual: reaches 7 days once in a while
            t = 0
            for d, c in zip((7, 14, 30, 50), F['streak_goals']):
                if weeks * 7 >= d: t += c
            return t
        res = {'per_day_played': round(day), 'earn_week': round(week), 'spend_week': round(spend_wk), 'net_week': round(week - spend_wk)}
        for label, wk in (('week1', 1), ('month1', 4.33), ('month3', 13), ('month6', 26), ('month12', 52)):
            gross = week * wk + lvl_bonus(wk) + streak_bonus(wk)
            res[label] = round(gross - spend_wk * wk)
        res['steady_month'] = round((week - spend_wk) * 4.33)
        out[name] = res
    return out

# ---------------- CURRENT (content page before 25 Nov) ----------------
CUR_F = dict(puzzle_classic=5, puzzle_expert=7, mystery=2, nohint=2, daily=10, daily_per_streak_day=1, daily_streak_cap=10, qp=5,
             tasks=[5, 10, 15], tasks_all3=20, ads_max=5, ad=10, jar=10, hint_price=25,
             level=25, lvl5=0, lvl_10_25_50=0, lvl_20_40=0, streak_goals=[30, 60, 120, 0])
CUR_P = dict(freeze=150, picture=300, frame=500, outfit=1150, theme=2000)
# ---------------- PROPOSED (25 Nov) ----------------
NEW_F = dict(puzzle_classic=4, puzzle_expert=6, mystery=1, nohint=1, daily=8, daily_per_streak_day=1, daily_streak_cap=5, qp=3,
             tasks=[4, 6, 10], tasks_all3=10, ads_max=3, ad=8, jar=10, hint_price=15,
             level=15, lvl5=50, lvl_10_25_50=150, lvl_20_40=300, streak_goals=[30, 75, 200, 350])
NEW_P = dict(freeze=200, picture=400, frame=700, outfit=1500, theme=3000)

def catalogue(P):
    launch = 6 * P['theme'] + 8 * P['outfit'] + 12 * P['picture'] + 10 * P['frame']   # 8 of 20 pictures free
    monthly = 1 * P['theme'] + 1 * P['outfit'] + 2 * P['picture'] + 1 * P['frame']
    return launch, monthly

for tag, F, P in (('CURRENT', CUR_F, CUR_P), ('PROPOSED', NEW_F, NEW_P)):
    m = model(F, P); launch, monthly = catalogue(P)
    print(f'\n== {tag}: launch catalogue {launch:,} coins, new items each month {monthly:,} coins')
    for n, r in m.items():
        steady = r['steady_month']
        print(f"{n:8} day {r['per_day_played']:4} | week earn {r['earn_week']:5} spend {r['spend_week']:4} net {r['net_week']:5} | "
              f"wk1 {r['week1']:5} m1 {r['month1']:6} m3 {r['month3']:7} m12 {r['month12']:7} | steady/month {steady:6} "
              f"| first picture {P['picture']/max(1,r['net_week'])*7:4.0f} d, outfit {P['outfit']/max(1,r['net_week']):4.1f} wk, theme {P['theme']/max(1,r['net_week']):4.1f} wk "
              f"| buys {steady/monthly*100:3.0f}% of each month's new items | catalogue in {launch/max(1,steady):4.1f} months (if no new items)")
    print(f"  freeze = {P['freeze']/ (F['puzzle_classic']+F['mystery']*.7+F['nohint']*.6):.0f} Classic puzzles; hint = {F['hint_price']/(F['puzzle_classic']+F['mystery']*.7+F['nohint']*.6):.1f} puzzles; theme = {P['theme']/(F['puzzle_classic']+F['mystery']*.7+F['nohint']*.6):.0f} puzzles")
json.dump({'current': model(CUR_F, CUR_P), 'proposed': model(NEW_F, NEW_P), 'F': NEW_F, 'P': NEW_P}, open(sys.argv[1] if len(sys.argv) > 1 else '/dev/null', 'w'), indent=1)
