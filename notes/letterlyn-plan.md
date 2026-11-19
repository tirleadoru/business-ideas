# Letterlyn: Product Plan v1 (2026-11-19)

> Based on the user's first-impression feedback on the M0 prototype. Builds on `word-search-game-design.md`.
> Status: plan agreed in principle, decisions open at the bottom. **No code until approved.**

## User feedback on M0
- ✅ Loads fast, works, logic and puzzles are good.
- ❌ Too few packs. No settings/info menu.
- ❌ Players don't know words can go **backwards**. The user only discovered it by struggling.
- ❌ No monetization yet: "how will I make gains from ads?"
- ❌ "Play 6 packs and I'm done": needs long-term replayability, catchiness, competition.
- ❓ Does it need a backend (accounts, login, leaderboards, high scores, timed scoring)?

---

## 1. Onboarding, how-to-play, settings
- **First-run tutorial (about 20 seconds, skippable):**
  - An animated hand drags across a word, then the player does one.
  - No text walls. Works the same in every language.
- **Teach directions when they first appear,** not up front. When a puzzle first uses a new direction, show a short card with a mini animation:
  - "New: words can go diagonally ↘"
  - "New: words can go backwards ←"
- **Per-puzzle direction icons:** a small "↔ ↕ ⤡" indicator above the grid shows which directions this puzzle uses. Clear without reading.
- **Menu (⚙️):**
  - How to play (replay the tutorial).
  - Language, sound, vibration.
  - Large letters, high contrast, ignore diacritics.
  - Timer on/off (Relax vs Challenge, see §3).
  - Privacy, credits, reset progress.

## 2. How the money actually works
**Right now the game earns €0.** Ads only pay once the platform's ad code (SDK) is built in. Portals also require the SDK for a full launch (with promotion and revenue share).

Where the ads go (the same "fair ads" rules everywhere):
| Ad type | When | Platform call |
|---|---|---|
| **Break ad (interstitial)** | Between puzzles only, never mid-puzzle, never before the first puzzle. Max one every ~3 puzzles; portals also enforce their own cooldowns | Poki `commercialBreak()`, CrazyGames `requestAd('midgame')`, AdMob interstitial |
| **Rewarded ad (opt-in)** | Player chooses: +coins for hints, double puzzle reward, restore a broken daily streak, unlock a pack early, a retry in Challenge mode | Poki `rewardedBreak()`, CrazyGames `requestAd('rewarded')`, AdMob rewarded |
| **Banner** | Optional, outside the play area (CrazyGames allows them). Test whether it's worth it | CrazyGames banner API |
| **Remove ads (purchase)** | Mobile: about €2.99–4.99 one-time, removes break ads forever. Rewarded ads stay as an option | Play Billing / StoreKit (later Xsolla on CrazyGames) |

**What is "locked behind ads": a soft economy, not a paywall.**
- Players earn **coins** by finishing puzzles. Hints cost coins.
- When coins run out, a rewarded ad gives coins, or the player just keeps playing without hints.
- New packs unlock by **playing** (finish N puzzles), or **right away with one rewarded ad**.
- Nothing is pay-to-win. Everything can be earned by playing, so ads are a shortcut and never a wall.

**Revenue estimate:** a portal play session of about 10 minutes ≈ 3 break ads + ~1 rewarded ad. At the ~$1 per 1,000 plays community estimate this is small per player; the money comes from volume plus long sessions. That's why §3 matters most.

## 3. Long-term play ("one and done" is the real risk)
Content alone can't solve this. The game needs **loops that never run out**:

1. **Daily Puzzle + streak** (the most important feature).
   - The same puzzle for everyone each day, per language. It's generated from the date, so it works offline.
   - Streak counter, and a monthly calendar that fills with stamps.
   - A rewarded ad can restore a broken streak once.
   - This is the Wordle hook: a reason to come back every day.
2. **Two ways to play every puzzle:**
   - **Relax** (default): no timer, stars only. The "calm" promise.
   - **Challenge:** a timer and a **score**: points per word, a speed bonus, a **combo** for finding words quickly in a row, and a penalty per hint. Personal best per puzzle, and a reason to replay.
3. **Shareable result** (free virality, no backend):
   - "Letterlyn Daily #42 🇷🇴 ⏱ 1:37 · 🔥 12-day streak · 💡0" plus a link.
   - Also **challenge a friend**: a code or link that loads the exact same puzzle (the generator is deterministic), and they try to beat your time.
4. **Endless "Quick Play":** a random puzzle from any unlocked theme, at your chosen size. Infinite, because the generator is.
5. **Progress meta:**
   - Player level/XP from every puzzle.
   - Stamp **album** (one stamp per completed pack).
   - **Achievements** ("Found 1,000 words", "7-day streak", "No-hint pack").
6. **Weekly themed event:** one special pack for the week (holidays, sports events, local celebrations), with a limited-time stamp. Built from content we already have, so cheap to run.
7. **Content pipeline:** about 30 packs per language at launch, then **2–4 new packs per month**. This is the "one week a month" maintenance work. Packs are drafted with AI at build time, then human-reviewed (the user reviews RO).

## 4. Backend: revised after the user's pushback (2026-11-19)
**The user is right.** Platform services are **separate silos**: an Android leaderboard can't see iOS players, and neither can see web players. One shared leaderboard everywhere, and analytics in one place, need **our own small backend from launch**.

**Key insight: a cross-platform leaderboard does *not* need a login system.** A leaderboard only needs a shared server that every platform sends scores to. Login is only needed when *one person* wants *their own* progress on *several devices*. That's a separate, later feature.

### Identity (no passwords, no emails, ever)
| Where | Player identity |
|---|---|
| Everywhere (default) | Anonymous **player ID** created on first launch, plus an **auto-generated nickname** like "CalmOtter42". Generated names mean no nickname moderation work. Players can re-roll, but not type free text |
| CrazyGames | Link our player ID to the CrazyGames account through their User module (allowed; Google/email logins inside the game are **not** allowed there) |
| Android / iOS | Link to Google Play Games / Game Center (and maybe Sign in with Apple/Google later). No passwords on our side |
| Moving to a new device | A **transfer code** ("LYN-7KQ2-9MXD"): enter it on the new device to pull your progress. Works on every platform, with no personal data |

### What the backend does
- **Scores:** daily-puzzle results and Challenge scores → **one global leaderboard per day and per language**, the same on web, Android and iOS. Also a friends view through challenge codes.
- **Anti-cheat:** the server knows the puzzle seed, re-checks the submitted found-word sequence and timestamps, rejects impossible times, and rate-limits.
- **Cloud save:** progress keyed by player ID (this powers the transfer code).
- **Analytics in one place:** a few anonymous events (puzzle started/completed, session length, ad shown) sent to our backend or to GameAnalytics. Portal dashboards stay as a second view.

### Stack and cost
- **Cloudflare Workers + D1 (SQLite).**
  - Free plan: 100K requests/day, 100K rows written/day, 5M rows read/day, 5 GB.
  - Since 1 Sep 2026, D1 free-plan queries fail when a daily limit is exceeded, so **switch to Workers Paid ($5/month) before launch** to avoid outages.
  - Rough capacity: about 10–20K daily players stay within the free limits. The $5 plan covers far more, and at that scale ads pay for it many times over.
  - No servers to patch, nothing to maintain beyond the code.

### Platform rules that affect this
- **Poki** blocks all external requests by default. Our backend URL and any analytics must be **approved by Poki** (send the exact URLs plus a privacy policy). No personal data (e.g. email) is allowed, and Google Analytics is blocked. → Our design fits: anonymous ID and generated nickname. **Fallback if not approved:** the Poki build runs offline with local bests only.
- **CrazyGames** has its own Leaderboards and Data (cloud save) modules, and supports server-side score submission. We can **mirror** our scores to their leaderboard too, for on-site visibility.
- **GDPR:** an anonymous ID plus gameplay data is still personal data. We need a privacy policy (hosted on letterlyn.com), a delete-my-data option in settings, and minimal data kept.

## 5. Revised milestones (v2: backend from launch, Android alongside the portals)
| # | Milestone | Contents |
|---|---|---|
| M0 ✅ | Engine prototype | Done 2026-11-19 |
| **M1** | **Complete core loop** | Tutorial and direction cards, ⚙️ menu, coins and hints, Daily Puzzle + streak + calendar, Relax/Challenge with score and combo, personal bests, share text and friend codes, Quick Play, XP/achievements/album, sound and haptics, large print and contrast |
| **M2** | **Backend v1** | Cloudflare Workers + D1: player ID and generated nicknames, daily and Challenge leaderboards (per day, per language), anti-cheat checks, cloud save and transfer code, anonymous analytics events, privacy policy and data deletion |
| **M3** | **Content for launch** | 30 packs EN + 30 RO, banned-word lists, first weekly-event packs |
| **M4** | **Ads + platform adapters** | One `ads`/`platform` interface: Poki, CrazyGames (+ user/leaderboard mirror), Capacitor/AdMob, dev mock |
| **M5** | **Launch wave 1** | CrazyGames + Poki (request backend approval) **+ Android on Google Play** (the company account skips the 12-tester rule) + the web version on letterlyn.com |
| **M6** | **Measure → decide** | Compare web vs Android retention, session length and revenue per player. Fix, then re-test |
| **M7** | **iOS + growth** | iOS app (Game Center link, Sign in with Apple if needed), more languages (TR, PL, PT-BR, DE…), learning mode, custom puzzles |

## 6. Decisions
1. ✅ Relax by default, Challenge optional (user, 2026-11-19).
2. ✅ Coin/hint economy: play to earn, ads as a shortcut, never a wall (user, 2026-11-19).
3. 🔄 Backend: the user questioned phasing → revised to **backend from launch** (§4). Waiting for the user's OK.
4. ✅ EN + RO first (user, 2026-11-19). The user is sceptical about judging only by the portals → revised plan launches **Android in the same wave** (M5).
