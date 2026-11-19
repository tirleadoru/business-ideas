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

### Same player everywhere (v3, after the user's question, 2026-11-19)
- **One Letterlyn player record on our backend, with several identities attached:** device IDs, a Google account, an Apple account, a CrazyGames account.
- **Play anonymously by default.** A **"Save your progress"** button offers sign-in. It's optional and never required to play.
- **"Sign in with Google" / "Sign in with Apple" are not our own login system.**
  - Google or Apple handles the password. Our backend only verifies their signed token (free) and stores "provider + id → player".
  - Apple rule: if an iOS app offers Google sign-in, it must also offer Sign in with Apple. → Offer both everywhere.
- **Per platform:**
  | Platform | How you "stay you" |
  |---|---|
  | letterlyn.com (web) | Sign in with Google or Apple → same progress as the phone automatically |
  | Android | Google sign-in (Play Games), or Apple |
  | iOS | Sign in with Apple (or Google) + Game Center |
  | CrazyGames | Their rules forbid Google/email login inside the game → the CrazyGames account is the identity. Link it to your Letterlyn player once with a **link code** shown on your phone |
  | Poki | No personal data or logins allowed → **link code** only (if the backend is approved), otherwise local only |
- **Merging two existing progress records when linking:**
  - Union of completed puzzles; best stars and best scores kept.
  - Longest streak kept.
  - Coins = the higher balance, not the sum (prevents a duplication exploit).
- **No email or password storage, no password-reset support.**

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

## 5. Revised milestones (v3: backend from launch, all platforms in one wave, content last)
| # | Milestone | Contents |
|---|---|---|
| M0 ✅ | Engine prototype | Done 2026-11-19 |
| **M1** | **Complete core loop** | Tutorial and direction cards, ⚙️ menu, coins and hints, Daily Puzzle + streak + calendar, Relax/Challenge with score and combo, personal bests, share text and friend codes, Quick Play, XP/achievements/album, sound and haptics, large print and contrast |
| **M2** | **Backend v1** | Cloudflare Workers + D1: player ID and generated nicknames, Google/Apple sign-in linking, link codes for portals, daily and Challenge leaderboards (per day, per language), anti-cheat checks, cloud save and transfer code, anonymous analytics events, privacy policy and data deletion |
| **M3** | **Ads + platform adapters** | One `ads`/`platform` interface: Poki, CrazyGames (+ user/leaderboard mirror), Android and iOS (AdMob, purchases, Play Games/Game Center), dev mock |
| **M4** | **Content for launch (last, by user's decision)** | How many packs and under what rules: to be decided together at that point. Plus banned-word lists and weekly-event packs |
| **M5** | **Launch wave 1** | CrazyGames + Poki (request backend approval) + **Android + iOS** (the company has both store accounts; Android skips the 12-tester rule) + the web version on letterlyn.com |
| **M6** | **Measure → decide** | Compare web vs Android vs iOS retention, session length and revenue per player. Fix, then re-test |
| **M7** | **Growth** | More languages (TR, PL, PT-BR, DE…), learning mode, custom puzzles |

## 6. Decisions
1. ✅ Relax by default, Challenge optional (user, 2026-11-19).
2. ✅ Coin/hint economy: play to earn, ads as a shortcut, never a wall (user, 2026-11-19).
3. ✅ Backend from launch: the user is "almost fine" with it. Cross-device identity added (§4 v3).
5. ✅ Content (packs) moves to the end (M4); count and rules to be decided then (user, 2026-11-19).
6. ✅ iOS in the launch wave (user, 2026-11-19).
7. ✅ Tech stack: **one codebase, web core + Capacitor** (user OK, 2026-11-19: "if it works with the same code fine by me"). UI: React.
8. ✅ Repo structure: **monorepo** (user OK, 2026-11-19), with per-folder checks on commit/push and in CI (see §8).
4. ✅ EN + RO first (user, 2026-11-19). The user is sceptical about judging only by the portals → revised plan launches **Android in the same wave** (M5).

## 7. Tech stack decision (open)
**Requirement:** the **web build is first-class**. Portals need a small, fast HTML5 bundle (M0 is about 7 KB gzipped). The same game must also ship as Android and iOS apps.

| Option | Web (portals, site) | Android/iOS | Notes |
|---|---|---|---|
| **A. Web core + Capacitor** (Claude's recommendation) | Native target, tiny bundle | Same code in a native shell; plugins for AdMob, purchases, Play Games/Game Center, haptics | One codebase, three targets. UI can be plain TS (as now) or **React/Preact** if the user prefers React |
| B. React Native (Expo) + react-native-web | Possible, but web becomes the second-class target: heavier bundle (React + RN-web runtime), gesture libraries are weaker on web, less common on portals | Real native UI, best native feel | Good if mobile were the main target. Here the portals are half the launch |
| C. Two codebases (web + RN) | Best web | Best native | Double the work and the maintenance. Rejected |

- **The engine (generator, selection, scoring, content) is pure TypeScript** and works unchanged in any of these.
- A word search grid is light, so a WebView's performance is more than enough. Apple accepts Capacitor games that have real native features (ads, purchases, Game Center); thin website wrappers are what get rejected (guideline 4.2).

## 8. Repo structure (open)
**User's reference:** `~/Work/red-assistance*` uses separate repos for mobile apps, admin, marketing web and API.

**What's different here:** web and mobile are the **same app** (Capacitor), so they belong in one codebase. And the **server must run the same puzzle engine** as the game to check scores. If the game and API ever run different engine versions, the server rejects valid scores.

**Claude's proposal: one monorepo (`letterlyn`) with workspaces.** Each app still has its own tests, builds and deploys.
```
letterlyn/
├── packages/engine/   ← generator, scoring, validation (shared: game + api)
├── packages/content/  ← word packs (shared: game + api for daily-puzzle validation)
├── apps/game/         ← web build (portals, play.letterlyn.com) + android/ + ios/ (Capacitor)
├── apps/api/          ← Cloudflare Worker + D1
├── apps/site/         ← marketing site letterlyn.com, privacy policy, support
└── apps/admin/        ← later: stats, leaderboard moderation, content tools
```
- A scoring change updates the game and the API in **one commit**.
- CI runs only what changed: per-app path filters.
- Testing per target:
  - Engine: unit tests.
  - Web: Playwright end-to-end tests.
  - Mobile: Capacitor builds on emulators and simulators, plus Maestro smoke tests for native parts (ads, purchases, sign-in).
  - API: Worker tests with a local D1.

**Alternative (the red-assistance style):** separate repos `letterlyn` (game web+mobile), `letterlyn-api`, `letterlyn-web`, `letterlyn-admin`, with the engine published as a private package (GitHub Packages). Workable, but version drift between the game and API is a real risk for a solo developer.

### Per-folder checks (agreed 2026-11-19)
- **Local git hooks (Lefthook):** each command has a `glob`/`root`, so it only runs when staged files in that folder changed.
  - `apps/game/**` → typecheck + lint + unit tests (+ `npx cap doctor` when native config changed).
  - `apps/api/**` → Worker typecheck + tests.
  - `packages/engine/**` → engine tests **and** the game and API checks, because both depend on it.
  - Pre-commit stays fast (staged files only); pre-push runs the affected test suites.
- **CI (GitHub Actions):** path filters plus **Turborepo** "affected" runs, so only changed workspaces **and their dependents** are checked.
  - **Correction (user, 2026-11-19):** CI checks **source code only** (types, lint, tests). **No app builds in CI.**

### Native builds and releases (Capacitor)
- **Native projects:** `apps/game/android/` and `ios/` are committed (native settings, icons, signing config). Build output is git-ignored: `build/`, `Pods/`, the copied web `public/`, generated plugin folders.
- **Builds run locally:** Gradle → `.aab`, Xcode → archive. **fastlane** handles one-command build + upload:
  - `npm run release:android`
  - `npm run release:ios`
  - `npm run release:web` (portal zips + deploy play.letterlyn.com)
- **Optional cloud builds later:** Capawesome Cloud (from about $9/month; Ionic's recommended replacement for Appflow, which sunsets 31 Dec 2027) or Codemagic.
- **Optional updates without store review:** Capawesome Live Updates / Capgo.
