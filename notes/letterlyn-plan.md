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

## 4. Backend: needed, but not on day one
**Recommendation:** grow it in phases and borrow the platforms' free services before writing our own.

| Phase | What | Backend? | Cost |
|---|---|---|---|
| **A: launch** | Local progress, personal bests, daily puzzle, streaks, share text, friend challenge codes | **None** | €0 |
| **B: platform services** | **Google Play Games** (leaderboards, achievements, cloud save, sign-in) and **Apple Game Center** (same). CrazyGames has user accounts and a cloud-save data module; its leaderboard support needs checking | **None**, the platforms host it | €0 |
| **C: own backend, only if data justifies it** | One global, cross-platform **daily leaderboard** per language, friends lists | Small serverless API: Cloudflare Workers + D1, or Supabase | Free tier at first; $5–25/month once large, funded by revenue by then |

**Why not build accounts and login ourselves**
- Passwords, GDPR data handling, account recovery and support emails are exactly the ongoing work we want to avoid.
- Players already have a platform identity (Google Play Games, Game Center, CrazyGames account). We use those.

**Cheating on leaderboards**
- Any client-side game can be faked. For the daily leaderboard (phase C), the server re-checks the submission: puzzle seed, the found-word sequence with timestamps, and minimum human times. It also caps scores.
- Platform leaderboards (phase B) are accepted as "good enough" for a casual game.

## 5. Revised milestones
| # | Milestone | Contents |
|---|---|---|
| M0 ✅ | Engine prototype | Done 2026-11-19 |
| **M1** | **Complete core loop (no backend)** | Tutorial and direction cards, ⚙️ menu, coins and hint economy, Daily Puzzle + streak + calendar, Relax/Challenge with score and combo, personal bests, share text and friend codes, Quick Play, XP/achievements/album, sound and haptics, large print and contrast |
| **M2** | **Content for launch** | 30 packs EN + 30 RO (universal + local), banned-word lists, first weekly-event packs |
| **M3** | **Ads integration** | A single `ads` interface with adapters for Poki, CrazyGames and a dev mock, all following the fair-ads rules |
| **M4** | **Portal launch** | CrazyGames + Poki submissions; analytics (retention, session length, ad views per session) |
| **M5** | **Measure → go/no-go** | Gates: avg session ≥ ~15 min, good day-1/day-7 retention versus portal benchmarks. Fix, then re-test |
| **M6** | **Mobile** | Capacitor Android/iOS, AdMob, remove-ads purchase, Play Games + Game Center (leaderboards, achievements, cloud save) |
| **M7** | **Own backend (optional)** | Cross-platform daily leaderboard, only if M5/M6 data shows competition drives retention |
| **M8+** | **Growth** | More languages (TR, PL, PT-BR, DE…), learning mode, custom puzzles |

## 6. Open decisions for the user
1. **Competition style:** OK with "Relax by default, Challenge optional", so the game stays calm but competitive for those who want it?
2. **Coins/hints economy:** OK with "play to earn, ads as a shortcut, never a wall"?
3. **Backend phasing:** OK with A → B → C, with no own login system?
4. **Launch scope:** launch on portals with EN + RO only, then add languages after the data?
