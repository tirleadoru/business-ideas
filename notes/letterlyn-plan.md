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
| **M1 ✅ (2026-11-19, branch m1)** | **Complete core loop** | Tutorial and direction cards, ⚙️ menu, coins and hints, Daily Puzzle + streak + calendar, Relax/Challenge with score and combo, personal bests, share text and friend codes, Quick Play, XP/achievements/album, sound and haptics, large print and contrast |
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
7. 🔄 Tech stack: **reopened** after the user's "premium only" challenge and research (see §9). A device spike decides: Capacitor vs Expo.
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

## 9. Tech stack re-check: "premium only" (2026-11-19)
**The user's challenge:** web-in-app usually feels slow. Everything must feel premium.

**Research findings (honest):**
- No rigorous independent benchmark exists. The 2026 comparisons agree that WebViews handle simple and moderate UI at 60fps, but **games, gesture-heavy UI and complex animation are exactly where they fall short**.
- **Android is the weak point:** the system WebView differs by device, and budget phones struggle.
- WebViews add about 150–500ms of cold start and extra memory.
- **No evidence found of top-chart mobile games built with Capacitor/Cordova.** Only tutorials and small titles.
- → Claude's earlier claim that a WebView is "plenty fast" was **stated with more confidence than the evidence supports**. Corrected.

**Portal size limits** (relevant for a React Native web build):
- CrazyGames: initial download ≤ **50 MB**, and ≤ **20 MB** to qualify for the mobile homepage.
- Poki: ~**8 MB** target (third-party guides; verify), and players leave if loading takes over 10s.
- → An Expo web build (low single-digit MB) **fits**. Bundle size alone does not rule out Expo.

**Revised options:**
| Option | Mobile | Web/portals | Fit |
|---|---|---|---|
| A. Capacitor (M0 code) | WebView: risk of non-premium feel on mid/low Android | Best (7 KB) | Cheapest, but risks the premium bar |
| **B. Expo universal** (one RN codebase: iOS + Android + web) | **Truly native** UI; gestures on the UI thread (Gesture Handler + Reanimated) | react-native-web: bigger bundle, gestures run in JS on web, needs measuring | Matches the user's skills and EAS workflow; native folders git-ignored (CNG) |
| C. Expo for mobile + tiny web UI | Native | Best | Two UIs (both small) sharing `packages/engine`. Fallback if B's web build is poor |

**Decision method: a device spike (1–2 days) instead of opinions.**
1. Build the same puzzle screen in Expo (iOS/Android/web) and wrap M0 in Capacitor.
2. Test release builds on the user's iPhone, a mid-range Android and a **budget Android** (~€100–150, worth buying as a permanent test device).
3. Measure: drag smoothness/fps, touch latency, haptics timing, cold start, web bundle size and portal load time.
4. Pick the one that meets the premium bar.

**Claude's expectation going in:** B (Expo) is likely the winner for mobile feel and fits the user's existing workflow; its web build must prove itself, with C as the fallback.

## 10. Spike results (2026-11-19, branch `spike/stack-comparison` in SmartDevSolutionsLimited/letterlyn)
The same 12×12 RO puzzle screen in both stacks, measured identically.

| Test | Capacitor (WebView) | Expo (React Native) |
|---|---|---|
| Web bundle (gzip) | **~7 KB** | ~359 KB (1.56 MB raw) |
| Web: ready to play, slow 4G, CPU ×1/×4/×6 | **0.48 / 0.55 / 0.60 s** | 2.16 / 2.42 / 2.64 s |
| Web: drag smoothness (CPU ×6) | 60 fps, 0 dropped | 60 fps, 0 dropped |
| Android emulator cold start (`am start -W`, 5 runs) | 2.50/1.74/1.18/0.94/1.15 s (median 1.18) | **0.90/0.95/0.84/0.75/0.73 s (median 0.84)** |
| Android emulator drag (12 long swipes) | 59 fps, 0.7% dropped, worst **67 ms** | **60 fps, 0.3% dropped, worst 33 ms** |
| iOS simulator, first launch | **blank white screen ≥6 s** (WebKit start-up), board by ~9 s | board within 1 s |
| iOS simulator, relaunch (screenshot at 1 s) | blank on 1 of 2 runs | **board on 2 of 2 runs** |
| Android APK (universal, all ABIs) | 3 MB | 81 MB (the Play AAB per-device download is much smaller) |

**Reading so far:**
- **Web:** both are perfectly smooth. Capacitor/plain web loads about 4× faster, but Expo's 2.2–2.6 s is acceptable for portals (well under Poki's 10 s drop-off).
- **Mobile:** Expo starts faster, shows content immediately, and has steadier frames. Capacitor shows the classic **blank-WebView-on-launch** symptom. A native splash screen can hide it, but not remove it.
- **Caveat:** the emulator and simulator use Mac hardware. **The final verdict needs the user's devices:** iPhone 13, iPhone 16, Samsung S20 Ultra (120 Hz), plus a budget Samsung A15/A16 (to buy).

**Device test protocol (user):**
1. Cold start: force-close, launch, watch for a white flash or blank screen.
2. Drag feel: slow drags, fast zig-zags. Does the line stick to the finger? Is there a haptic tick per letter?
3. Press "Reset stats", do 10 drags, read the on-screen numbers.
4. Objective lag test: record a fast drag in iPhone **slow-mo (240 fps)** and compare finger vs line.
5. Found-word animation feel.

## 11. Direction after the spike (2026-11-19)
**User:** stop testing. Build each platform "as it's meant to be built", with no web-in-app and no app-in-web. Two codebases are acceptable.

**Claude's proposal: native mobile + real web, one shared engine.**
| Target | Built with | Why |
|---|---|---|
| iOS + Android | **Expo / React Native**: real native views, gestures and animation on the UI thread | Won the spike on mobile (startup, frame stability, no blank screen). The user already knows it (EAS workflow) |
| Web (portals + play.letterlyn.com) | **Plain TypeScript web** (the M0 approach) | Won the spike on web (7 KB, ready in ~0.5 s) |
| API | TypeScript on Cloudflare Workers | — |
| Shared | `packages/engine` (generator, scoring, validation), `packages/content`, i18n strings, design tokens | **The same puzzle code everywhere** → identical daily puzzles on every platform, and server-side score checks always match |

**Why not Swift + Kotlin + web (three fully separate native codebases)?**
- Three UIs, plus the engine rewritten in Swift and Kotlin.
- **The cross-language determinism risk:** the daily puzzle and the leaderboard checks need *bit-identical* puzzles. Different RNG, float maths and Unicode uppercasing between languages would produce different grids.
- For a 2D word game, React Native already renders real native views, so the extra gain is marginal and the cost is about 3× the work.

## 12. Deployment (discussed 2026-11-19; letterlyn.com bought, Remus preparing a server)
- **Never put the repo on a server.** Only build outputs are deployed, each to its own place:
  - **letterlyn.com:** `apps/site` static build (marketing, privacy policy).
  - **play.letterlyn.com:** `apps/web/dist` (about 20 KB). The same dist is zipped and uploaded by hand to CrazyGames/Poki.
  - **api.letterlyn.com:** `apps/api` (M2): a Cloudflare Worker per the plan, or a Node service on Remus's server.
  - **Mobile:** EAS → App Store / Google Play. Nothing on any server.
  - `packages/*` are compiled into each build; never deployed alone.
- **Claude's recommendation:** Cloudflare Pages (free; builds only the named folder from GitHub) for site + web game, and Workers for the API. No server upkeep.
  - Use Remus's server only if he wants to maintain it long-term.
  - If his server is used: `/var/www/letterlyn.com`, `/var/www/play.letterlyn.com`, DNS per subdomain; never expose `.git` or source.
- **Open questions for Remus:**
  - What kind of server, and who maintains it?
  - Where is DNS managed (moving it to Cloudflare is easiest)?
  - Domain email (support@letterlyn.com) for the store listings.
  - Privacy policy URL (Apple requires one).

### 12b. Decision (user, 2026-11-19): Letterlyn gets its own setup on the company's AWS **Lightsail** (Remus administers)
- Letterlyn is a **separate business** from red-assistance (which runs on its own EC2 servers). Don't copy red-assistance's infrastructure.
- **One Lightsail instance:**
  - nginx serves letterlyn.com (site) and play.letterlyn.com (web game) as static `dist` folders.
  - api.letterlyn.com (+ staging-api) is a **Node/TS** service (systemd + nginx), because it must run the shared engine to verify scores.
- **Database:** on the instance, or a Lightsail managed DB (~$15/month). Remus decides.
- **Backups:** Lightsail automatic daily instance snapshots, plus a nightly DB dump to a Lightsail bucket.
- **HTTPS:** Let's Encrypt. Secrets: `.env` on the server, never in git.
- **Deploy (revised, user's call):** **no repo on the server.** `deploy.sh` on the Mac builds site + web + API (API bundled to one file) and uploads only the outputs over SSH into `releases/<date>`, then switches `current` and restarts. Rollback = previous release.
- The API is written portably (Hono + a thin DB layer).
- **Questions for Remus:** instance size (smallest to start), DB choice, staging from day one, region (Frankfurt), support@letterlyn.com + privacy policy URL.

### 12c. Deploy workflows (agreed 2026-11-19, same idea as the user's red-assistance site/admin deploys)
- **Three path-filtered GitHub Actions deploys in the monorepo:**
  - `deploy-site`: `apps/site/**`, `packages/content/**`.
  - `deploy-web`: `apps/web/**`, `packages/**`.
  - `deploy-api`: `apps/api/**`, `packages/**`. Bundle → upload release → migrations → switch `current` → restart → `/health` check → automatic rollback on failure.
- **Branches:** `staging` → staging, `main` → production.
- **Engine changes** deploy API + web together, API first.
- **Mobile apps are never built in CI**; only site/web/API (seconds).
- **Lightsail has no IAM-role/SSM route like EC2**, so deploys use SSH: a GitHub secret key for a restricted `letterlyn` user plus a sudo rule limited to the two service restarts. A Mac fallback script runs the same steps.

## 13. Offline-first (agreed 2026-11-19)
- **The game never needs the server to play.**
  - Puzzles are generated on the device: packs, Quick Play, friend codes and the **daily puzzle** (built from the date).
  - Progress is saved locally first.
- **Online only:** leaderboards (view/submit), cloud save + Google/Apple sign-in, ads (offline = no ads; hints still work with earned coins).
- **Sync:** each finished puzzle is saved locally and added to an **outbox queue**, sent on app open / foreground / puzzle end when online. Multi-device conflicts use the agreed merge rules.
- **Daily leaderboard fairness:** a late (offline) result counts for that day if it arrives within ~48 h and passes the server check (seed + plausible timings). After that it counts for streaks and stats only.
- **Costs:** the API is a fixed-cost Lightsail service, not per-usage. Server downtime only delays leaderboard updates.

## 14. Content delivery and the daily puzzle (agreed 2026-11-19)
- **Daily puzzle = generated from the date** (theme pack + words + grid, seeded). No stock to prepare and it never runs out; tests already cover a full year in both languages.
  - The limit is **variety**: the theme repeats every N days, where N = number of packs (6 now, target ~50 per language).
- **Content feed** (versioned JSON on Lightsail, e.g. `letterlyn.com/content/…`):
  - The app ships with all packs existing at release (fully offline).
  - When online, it downloads new packs and caches them. Allowed by Apple/Google (data, not code).
  - The web game reads the same feed (needs Poki approval).
  - **Monthly content = add packs to the feed; no app release.** App releases only for features and fixes.
  - EAS Update not used for content: its cost scales with users.
- **Fair daily rule:**
  - Packs are append-only and versioned (never edited after publish).
  - The feed carries a **daily schedule ~30 days ahead** (date → pack + version, plus special days like holidays and events).
  - Dates outside the schedule fall back to the built-in date rotation.
  - A player missing the schedule (offline >30 days) plays an **unranked** daily (streak/stats still count).
  - The server validates scores with the same schedule.
- **Milestones:** M2 = API (leaderboards, cloud save) + content feed + daily schedule. M4 (content) = filling the feed.

## 15. Offline rules, told to players (agreed 2026-11-19, built in M2)
**Rules (also the "Playing offline" section of How to play):**
1. Everything works offline, the daily included.
2. Progress is saved on this phone right away, then synced when online.
3. Your streak always counts, online or offline.
4. Daily leaderboard: an offline result joins that day's ranking if you're online within **48 hours**.
5. Hints use coins (work offline); ad rewards need internet.
6. Two devices: progress is combined on sync, best results kept, coins = higher balance.
7. Until you sync or sign in, progress lives only on this phone; deleting the app before that loses it.

**Where they're shown (EN / RO):**
| Moment | Text |
|---|---|
| Header offline | "Offline · progress saved on this phone" / "Offline · progresul e salvat pe acest telefon" |
| Header pending | "3 results waiting to sync" / "3 rezultate așteaptă sincronizarea" |
| Daily card offline | "Play now. Your result joins today's ranking if you're online within 48 hours." / "Joacă acum. Rezultatul intră în clasamentul zilei dacă revii online în 48 de ore." |
| Results offline | "Saved. We'll send it when you're back online." / "Salvat. Îl trimitem când revii online." |
| After 48 h | "Played offline: counts for your streak, not that day's ranking." / "Jucat offline: contează pentru serie, nu pentru clasamentul zilei." |
| Unranked daily | "Unranked" + "Connect once to get the latest daily puzzles." / "Neclasat" + "Conectează-te o dată pentru careurile zilei la zi." |
| Leaderboard offline | "Connect to see today's leaderboard." / "Conectează-te ca să vezi clasamentul de azi." |
| Not signed in (after a few days) | "Keep your progress safe: sign in to sync it and move it to a new phone." / "Păstrează-ți progresul: conectează-te ca să-l sincronizezi și să-l muți pe un telefon nou." |

- Store listings: "Plays fully offline."
- Messages appear only at the moment they matter; no startup text walls.
- All strings go into `packages/content` i18n (same text on web + mobile).
