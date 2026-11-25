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

### Identity (no passwords, no email logins, ever; email only by opt-in, §27h)
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
- **No password storage, no password-reset support.** Email is stored only when a player opts in to notification emails or the newsletter (§27h, 2026-11-25).

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
| **M2 ✅ (2026-11-20, branch m2)** | **Backend v1** | Cloudflare Workers + D1: player ID and generated nicknames, Google/Apple sign-in linking, link codes for portals, daily and Challenge leaderboards (per day, per language), anti-cheat checks, cloud save and transfer code, anonymous analytics events, privacy policy and data deletion |
| **M3** | **Ads + platform adapters** | One `ads`/`platform` interface: Poki, CrazyGames (+ user/leaderboard mirror), Android and iOS (AdMob, purchases, Play Games/Game Center), dev mock |
| **M4** | **Content for launch (last, by user's decision)** | How many packs and under what rules: to be decided together at that point. Plus banned-word lists and weekly-event packs |
| **M5** | **Launch wave 1** | CrazyGames + Poki (request backend approval) + **Android + iOS** (the company has both store accounts; Android skips the 12-tester rule) + the web version on letterlyn.com |
| **M6** | **Measure → decide** | Compare web vs Android vs iOS retention, session length and revenue per player. Fix, then re-test |
| **M7** | **Growth** | More languages (chosen by who can check them, 2026-11-22: PL, CS, ES, IT, HU), learning mode, custom puzzles |

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

## 16. M2 as built (2026-11-20, branch `m2`)
**Changes from the plan (Claude's calls, easy to revisit):**
- **Content feed** is served by the API (`api.letterlyn.com/v1/content`), not `letterlyn.com/content`. One source: the API validates dailies with the same packs it serves.
- **No 30-day schedule file.** A new pack joins the daily rotation 31 days after its `addedOn` date. Anyone who synced in the last 30 days builds the same daily; older devices show "Unranked". The server decides the final ranking.
- **Friend codes name their pack** (seed = pack number × 65,536 + variant), so a code builds the same puzzle on every device. A code for a pack the device lacks triggers a sync, then "code invalid".
- **Leaderboard rule:** fastest time, +30 s per hint. Daily: first solve counts. Codes: best try counts.
- **Coins on sync:** fast-forward when only one device changed (spending stays spent); higher balance only when two devices really diverged.
- **Anti-cheat:** server rebuilds the puzzle, all words exactly once, first word ≥1.2 s, ≥250 ms between words, score recomputed.
- **Analytics:** only daily counters (event, platform, language). Nothing per player.
- **No staging web game.** The `staging` branch deploys only the API; mobile preview builds use staging-api.
- Local API runs on port 3010 (3000 is taken on the dev Mac).

**Still open after M2:**
- Sign in with Google/Apple **buttons** in the apps: the server part is done and tested. It needs a Google OAuth client ID and Apple Sign-in setup in the developer consoles.
- Sign-in nudge text (§15) waits for those buttons.
- Privacy policy page (letterlyn.com/privacy) before any store submission.
- GitHub environments + deploy key (README "One-time GitHub setup"), then Remus installs the server files.
- A dev-only Reanimated warning on the mobile puzzle screen (shows in debug builds only); source not found yet.

## 17. Future ideas backlog (user, 2026-11-20; not scheduled)
1. **Themes and seasonal content.**
   - A seasonal look switches on by default during the season (Christmas, Halloween…), and the player can turn it off.
   - A theme picker with a few designs to swap between.
   - Themed puzzle packs per holiday, plus country-specific ones (Thanksgiving for US/CA, Día de Muertos for MX, Romanian holidays…). Tag content by country, using the device's region setting; country ≠ language (es-MX vs es-ES).
   - Monetization: cosmetic themes are fair, non-pay-to-win money. Sell them inside a "LetterLyn Plus" lifetime purchase or as a theme bundle. On Poki (no in-app purchases) they're free or unlocked by a rewarded ad.
   - The UI already uses colour tokens (web CSS variables, mobile palette), so the colours are cheap. Decorations and art need an illustrator.
2. **Bilingual "learn" mode** (already planned as M6 in the design doc): the clue is in your language, the grid word is in the target language ("dog" → find CÂINE).
   - To teach (the player doesn't know the word yet): first a short card (dog = câine, with a picture and audio), then the grid shows "dog = CÂINE".
   - Later only "dog", with first-letter help if stuck. Missed words come back in a review list (spaced repetition).
3. **Kids variant + pronunciation.** Words read aloud, especially for learn mode; for adults learning languages too.
   - Cost rule: no per-use voice API. Option 1: the device's built-in text-to-speech, which is free (Romanian quality varies). Option 2: audio generated once per word and shipped with the packs (a one-time cost).
   - ⚠️ Targeting kids triggers store rules: Google Play Families, the Apple Kids category, COPPA/GDPR-K. No personalized ads and limited third-party SDKs, so a big monetization impact. Decide between a "kids-friendly mode" in the general app and a separate kids app before building.
4. **Brand: always "LetterLyn"** (capital L in Lyn) in every visible text.
   - The mascot is **Lyn the bookworm**: a cute little worm with a graduation cap, loved by both adults and kids. The logo must include Lyn. (Decided 2026-11-22: Lyn has no gender; outfits let players style Lyn any way.)
   - Domains and code ids stay lowercase (letterlyn.com).
5. **Learning packs by subject**, localized per country: geography (mountains, rivers, cities), and so on, each word with a short fact card.
   - Facts must come from a source (e.g. Wikidata), not be written by hand ("accuracy should come from the source" principle).

## 18. Feedback round: variety and coming back (2026-11-21; not built yet)
1. **Packs feel repetitive** (Doru's wife, Animals). Cause: Animals has 24 words, but its 12 puzzles need about 92 word slots, so each animal shows up about 4 times. Each puzzle also picks its words on its own, so repeats can come back to back.
   - Bigger packs: 60–100 words each, or split themes (Farm, Wild, Sea, Birds, Insects, Pets).
   - "Deck" rule: a pack uses all its words before any repeats.
   - Puzzles per pack follow the word count (e.g. 24–30), instead of a fixed 12.
   - We're still pre-launch (only testers), so the current packs can be changed now. The append-only rule starts at public launch.
2. **No general leaderboard.** Today: daily (time) + friend codes. Challenge mode in packs only keeps a personal best. Idea: a **weekly league per language**, ranked by XP earned this week (Monday–Sunday), with reset and top-3 stamps. Fair across different puzzles. Needs pack runs verified by the server, like daily runs are.
3. **XP does nothing yet** besides a level number in the album. Ideas: levels unlock cosmetics (board themes, Lyn outfits, ties in with §17.1); the level shown next to the nickname on boards; XP feeds the weekly league.
4. **Names.** Generated, never typed: no moderation (abuse, kids, store/portal rules for user content). This is not a GDPR rule. Idea: let players *build* their name from the lists (pick adjective + animal), not only re-roll.
   - Problem found: the share text has the name at share time; after a re-roll the friend looks for a name that no longer exists (boards always show the current name). Fix: the share link carries a short public id of the sharer (e.g. `&from=…`), and the code's board highlights "who challenged you" whatever the name. Also limit re-rolls (e.g. a few, then once a week).
5. **Reasons to come back today:** daily + streak + calendar stamps, achievements, album, friend codes, quick play, challenge personal bests. Missing: a daily reminder (local notification on mobile, opt-in, free), a weekly league, new content often (weekly event pack, already in M4), rewards for levels, and a streak freeze bought with coins.

## 19. Monetization rulebook (v2 after research, 2026-11-21; waiting for Doru's OK)
Based on three research reports (competitor games, revenue after "no ads", spending psychology and rules). Key facts:
- **Ads are the main income in word games:** Wordscapes makes about 80% from ads. Purchases come on top.
- **"No ads forever" costs $5–10 elsewhere** (Zen Word 4.99, Word Search Explorer 5.99, Words of Wonders 9.99). It removes forced ads only; optional rewarded ads stay everywhere.
- **A cheap no-ads purchase can lose money:** the buyers are the most engaged players, worth roughly $5–15 in ads each (rough estimate).
- **Nobody in the genre uses lives/energy.** Free players meet ads and limited hints, never a wall.
- **People buy hints only when searching on costs something:** the last hard word, a streak or a timer. Easy puzzles mean no hint sales.
- **Fair, per players:** optional ads for hints, everything earnable, daily stays free.
- **Money grab, per players:** ads you can't close, banners over the board, paid wheel spins, a "$0.99 sale" that is a weekly subscription, needing ads for basics after paying.
- **Regulation:** the EU's CPC principles (March 2025; enforcement against Candy Crush, Gardenscapes and others since Sept 2026) target currency **bought with real money**. Currency earned only by playing is out of scope. The Digital Fairness Act proposal (Nov 2026) would ban pay-to-win for minors and switch off paid currency by default for children. The UCPD already bans urging children to buy.

**Rules**
1. Playing is free forever: every puzzle, the daily, leaderboards, codes, league. No lives, no energy.
2. **Coins are earned only, never sold.** All purchases are real-money items at a real price. That keeps us out of the paid-currency rules.
3. Money never buys rank: hints already cost +30 s; ranked boards stay skill-only.
4. No loot boxes or paid wheels, no countdowns or fake sales, no subscription disguised as a sale, no purchase prompts aimed at children. Optional ads stay for everyone, including buyers.
5. Streak protection is never sold: a free streak freeze is earned by playing.

**Buckets**
| Bucket | What |
|---|---|
| Free | All play, daily, boards, codes, league, achievements, album |
| Earned (coins, levels, play) | Hints, pack unlocks (finish N puzzles), some themes/Lyn outfits, streak freeze |
| Optional ad | +coins (about 5 a day), double reward, unlock a pack now, a hint when out of coins |
| Forced ad (free players only) | Between puzzles only, never in the first 5 puzzles of a session, at most every 3 puzzles and 3 minutes apart, closable. No banners on the board |
| **LetterLyn Plus**, one-time, about **€6.99** | No forced ads forever, **play any past daily (archive, counts as a normal puzzle: no streak or ranking)**, 1 free hint a day, supporter frame + badge (seen by others on leaderboards). Themes are NOT in Plus: all earned by playing |
| **Hint bundles** (real money, not coins) | e.g. 15 hints €0.99 / 50 €2.99 / 120 €5.99 |
| **Cosmetic packs** | Board themes, Lyn outfits, €1.99–2.99 each (some also earnable) |
| Later | Paid learning packs (geography etc.), and a subscription only with the bilingual learn mode (§17.2) |

**Where money comes from after Plus:** (1) most players never buy, and they watch ads, which is the main income; (2) Plus is priced above its lost ads; (3) optional ads continue; (4) hint bundles, cosmetics, later learning packs; (5) a learn-mode subscription later.

**Economy (tuned with data in M6):** pack first clear by size 5/8/12/15 (+5 for no hints), replays 1; daily 20 + streak bonus up to +20; Quick Play: the first 3 a day pay, then 1; Challenge score gives XP, not coins; level up +50; achievements 50–200; hint 25 (maybe a "first letter" hint for 10); start 100. Target: a regular player affords about 1 hint a day from playing. Every pack gets one hard "bonus word" (long, backwards), so hints are worth something without making puzzles frustrating.

**Portals:** Poki = ads only (Plus, bundles and cosmetics are earned or ad-unlocked there). CrazyGames = ads, plus Xsolla purchases only if invited.

## 20. Competitor notes: Wordscapes Search (2026-11-21, reference only, never copy its design or features)
Doru's 38 screenshots are in ~/Downloads/sample pics competitor. 10M+ downloads.
**What players hate (our "never" list):**
- A banner over the top of the screen *during play*.
- A forced video after every level from level 10.
- "No ads for 30 days" for 54.99 RON (~€11), not auto-renewing, and banners and rewarded videos stay even after paying. Lots of complaints.
- Pop-ups mid-level ("watch a video for a bonus gift").
- A daily "bonus reel" of 5 ads in a row.
- **Ad content: gambling (Casa Pariurilor, Winbet, Princess Casino), "Unlock $200 Now", dating/marketing, served by Meta.**
**Ideas worth adapting in our own way:**
1. **Themes by association, not only category members** ("Lions": pride, pack, king, meat, big cat). Far more word variety per theme, which is the answer to the repetitive-packs complaint.
2. **Daily tasks:** 3 small goals a day (e.g. find 2 long words, 8 vertical words) with coin rewards, plus a bonus for finishing all. Cheap to build, a reason to come back.
3. **Streak milestones** at 7/14/30 days with *known* rewards (not random), a streak calendar, and **streak freezes** (earned).
4. **Profile picture from a fixed set + frames** unlocked by levels/achievements/events: self-expression with nothing to moderate. Gives XP/levels a purpose; fits "build your name".
5. **Tools unlocked by level**, first use free as a tutorial: e.g. "first letter", "reveal a word", "clear unused letters". Levels mean something.
6. **A mystery word** in each puzzle for a coin bonus (like our planned bonus word).
7. **A journey feel:** packs grouped into chapters with changing backgrounds and a progress bar with a reward at the end (needs art).
8. **A small dictionary card** for the words in a puzzle: learning, fits Lyn the bookworm. Needs a licensed source (e.g. Wiktionary, CC BY-SA with attribution). Later. Each word entry needs a short **sense note** (which meaning we mean: SPRAY = sea spray, the noun; SWELL = long waves from a far-off storm), so every language translates the same sense (Doru, 2026-11-24).
9. **Extra real words** found in the grid fill a bonus bar. Needs a full dictionary per language. Later.
**Notes:** they allow typed nicknames (so they must moderate them); they show the player ID in settings (useful for support); delete account and data management are in settings (we have those).
**Ads rule this adds:** block sensitive categories in the ad network (gambling, dating, alcohol, politics, get-rich-quick), cap the ad content rating for a general audience, and no banners on the play screen. On Poki/CrazyGames the portal controls the ads.
**Follow-up (Doru + Claude, 2026-11-21):**
- **No forced journey:** every pack is open to everyone. Progress shows through per-pack progress, stamps and the album. That drops "unlock a pack with an ad" from §19.
- **Packs get their own screen** (a library by category) instead of everything on home.
- **Puzzles are already fixed:** pack + number → the same words and grid for everyone (seed `lang:pack:index`). So a per-puzzle word card works for us too.
- **Content structure proposal:** pack (e.g. Animals) → puzzles, each a hand-picked topic with association words (e.g. "Lions": mane, roar, pride, savanna…). AI-drafted, human-reviewed (Doru for RO).
- **Performance budget** (their app lagged and heated the phone): no constant animations or particles, draw only on change, light backgrounds, a 15-minute session test on the budget Samsung for heat and battery. Video ad SDKs also heat phones, which is one more reason for few ads.
- **Tools:** their prices are 100/150/200 coins against about 25 coins earned per level. We keep one hint (plus maybe a cheaper "first letter" one) and a free **rotate board** button.
- **Hint purchases will be small money** in a game without pressure (mostly "stuck on the last word" players). Don't rely on them: launch with Plus + optional ads; add hint bundles only if the data shows demand.
- **They have no community** (no ranks or challenges). Our leaderboards, friend codes and the planned league are a real difference.

## 21. Trust rule and real money math (2026-11-21)
- **Never change the deal backwards** (lesson from Wordscapes Search: lifetime no-ads → a $10/month plan + more ads → angry reviews). A public "fair play promise" from day 1 (in-app + website):
  - what is free stays free;
  - the forced-ad frequency for free players never goes up;
  - a lifetime purchase stays lifetime;
  - a later yearly option is only ever *added*, never replaces lifetime.
- **Where a store sale goes** (to verify with the accountant):
  - The buyer's VAT is collected by Apple/Google in the buyer's country (RO 21%, DE 19%…). The company's country (Gibraltar) doesn't matter for this, and we file nothing.
  - Store fee: 15% under the small-business programs (first $1M a year), not 30%.
  - US withholding: Gibraltar has no US tax treaty, so up to 30% may be held back on **US customers' sales and US ad revenue only**, not on everything. Already on the accountant question list.
  - Example €9.99 to a Romanian buyer ≈ €7.00 to the company. $9.99 to a US buyer ≈ $8.50, or ≈ $5.95 if 30% is withheld.
- Plus pricing (€6.99 vs €9.99, a yearly option later): undecided. Decide with data.

## 22. Decisions round 2026-11-22 (wireframes v26, nothing built yet)

- **Game time.** One new daily for everyone at **00:00 UTC**, countdown on Home. Reason: one board opening and closing at the same moment, final ranks and league prizes right away, no time zone peeking, travellers unaffected (local midnight lengthens/shortens your day when you fly). Wordle uses local midnight but has no rankings. Dailies are labelled by number (Daily #326), never by weekday; the Sunday Expert puzzle is the **"weekend special"** so it reads fine when it lands on Saturday evening in the Americas. Reminders still go out at each player's local chosen time.
- **Server daily key.** Each day's puzzle needs a secret key from our server, released at 00:00 UTC. Nobody can build future dailies from the code or by changing the phone clock. Cost: the daily needs internet once that day (then plays offline).
- **Offline rule: play offline, compete and spend online.** Offline: packs, Quick Play, hints with coins you hold, earning coins/XP/stamps (synced later). Online: daily (key), rankings, league, friends, clubs, shop, purchases, sign-in. No catch-up ads after offline play. Friendly offline home (screen 20).
- **Anti-cheat.** Server keeps the real coin and hint balance; every earn/spend is a logged event; earnings re-checked against verified puzzles; the server's number always wins. Earning capped by design (first clears pay once, replays little, Quick Play full pay 3 a day). Flags on the admin site: too fast, too many puzzles, hints > owned, balance mismatch, clock jumps, many accounts per device, failed Play Integrity / App Attest (free; checked only on score submit and purchase). No automatic bans; flagged scores hidden until a person decides. This also protects hint bundles if we ever sell them.
- **Sign-in.** Guests can play and appear on boards, but are told clearly that progress lives only on the phone (first session, Home strip, Settings). Sign-in suggested after the first pack / first streak / first 100 coins. Required for league prizes (kept 30 days), purchases, Plus, new phone.
- **Admin site** `secure.letterlyn.com`: admin accounts only, no sign-up page; username + password + TOTP 2FA + backup codes; lockout after 5 tries; 8 h sessions; audit log. Sections: overview, flags, players, content review (bad-word scan in 8 directions, patterns, duplicates; approve/replace/regenerate), daily schedule, leagues, purchases, admins.
- **Navigation:** 5 tabs Play · Lyn · Home · Social · Me (Home in the middle). Gap: the Lyn tab is empty until Lyn's world is built → launch with 4 tabs or a minimal Lyn tab.
- **Library:** Continue row first, finished packs move to the end, filters (in progress / not started / hide finished).
- **Profile:** showcase of 3 items seen by friends and clubs; league medals in the Album; name change free once a month, sooner 100 coins or one optional ad.
- **Web:** shows purchases but sends to the app (QR + store buttons); Plus and sets follow the account. Web earns from ads.
- **Social:** friends by code/QR, friends' daily results, head-to-head, preset reactions only, no chat at launch (moderation cost, kids, EU rules, calm brand; revisit via clubs first).
- **Later (all in the wireframes):** clubs (~30, per language, names from lists, emblem + colour, team weekly goal, club league, shelf of the week, no chat); Lyn's adventures (scenes with item spots → postcard, never random) and Lyn's room; daily journey map (one stop per daily solved, missing a day only pauses); Lyn's bookshelf (a book per 100 words); duet puzzles (two friends, one grid, both rewarded); Lyn's hidden message (leftover letters spell a fun fact); mystery topic (guess the topic, earlier = more coins).
- **Art:** list for Remus (partner, not employee) at https://claude.ai/artifact/LxvHWvr8MBs75MFECKckTZ; art should be owned by the company through a short written copyright transfer.

## 23. Decisions round 2 (2026-11-22, wireframes v27)

- **Shelf trophies:** each shelf has its own trophy (shared base + shelf-specific top piece); 4 states: locked silhouette, bronze 3 packs, silver 10, gold 25. **Changed 2026-11-22 → bronze 3 / silver 6 / gold 10 (see §27).** **Superseded 2026-11-23: bronze 5 / silver 10 / gold 15 (whole shelf), 15 packs per shelf, exactly 20 topics per pack (rules sheet).**
- **Packs:** 20–30 puzzles by topic richness; a published pack never changes; popular topics get a sequel ("Sea Life 2"). Packs can be finished, shelves never. **Superseded 2026-11-23: bronze 5 / silver 10 / gold 15 (whole shelf), 15 packs per shelf, exactly 20 topics per pack (rules sheet).**
- **Stamps per difficulty:** bronze edge Relaxed, silver Classic, gold Expert. Triples honest content for heavy players. Content pace: 240 launch puzzles ≈ 2.5 months casual / 6 weeks regular / 12 days heavy per difficulty; the bottleneck is native review per language, not writing.
- **Ad rule (strictest ever, may only loosen):** forced ad break only if ALL: past the first 3 puzzles of the day, not the first puzzle after opening the app (session = app open, ends after 30 min away), 3+ puzzles AND 3+ minutes since the last ad. Reason others are aggressive: they buy installs (€1–5 each) and must recoup; we grow organically.
- **Money target math (rough):** ~€0.35–0.55 ad income per daily player per month with our rules → €5k/month needs ~7–12k daily players with Plus/sets (≈150–300k installs over time). Real edge: localized store search in less crowded languages.
- **Game-day calendar:** Daily screen says "Game day: Sat 21 Nov · new one in …" with an ⓘ.
- **Feature unlock ladder:** day 1 daily/packs/Quick Play/friend codes · level 2 tasks · level 3 shop · level 10 join a club · level 15 create · duets once you have a friend. Tune XP so level 10 ≈ 1–1.5 weeks, level 15 ≈ 3–4 weeks.
- **Clubs:** Open / Ask to join / Invite only; leader + 2 helpers can remove (no rejoin 7 days); inactive leader 14 days → helper takes over; one club at a time; rewards count 24 h after joining and need 50+ words that week; inactive 30 days flagged to leader.
- **Duets:** turns of up to 3 words (live if both online); nudge after 12 h; finish alone after 24 h (normal reward for you); both rewarded when done; max 5 at once.
- **Monthly Journey ticket (later, needs the journey):** ~€2.99–3.99/month, inspired by 8 Ball Pool's pass but cosmetic only: free row for all + ticket row (premium reactions/phrases, animated frame, outfit, the month's postcard). Never coins, hints, boxes or speed-ups; one price; buying late unlocks all reached stops; free row finishable at 4–5 days a week; old items return later as sets; not in Plus. Estimate 2–5% of monthly players → ~€1.4–3.6k/month at 10k daily players. Art: ~10–15 items a month.

## 24. Symbols, accessibility, trademark plan (2026-11-22, wireframes v28)

- **One meaning per symbol:** stars = how well a puzzle was solved · ribbon = difficulty · metal = how many packs.
- **Difficulty ribbons, ski style, colour + shape:** ● green Relaxed · ■ blue Classic · ◆ black Expert. On stamps and shelf trophies. Expert also counts for the easier ones. "Gold ◆ Expert" looks different from "Gold ● Relaxed"; the Album shows each shelf's best per difficulty; the player picks one for the showcase.
- **Metals change shape too (corrected 2026-11-22):** the shelf top piece never changes; the shared base grows: bronze 1 step, silver 2 steps, gold 3 steps + laurel wreath around the top piece; locked = grey silhouette; tier name shown under it. (An earlier draft said cup/handles; that clashed with per-shelf trophy designs.)
- **Colour-blind rule everywhere:** never colour alone (shape, label or number). Duet colours blue + orange, never red + green. Check themes and found-word colours.
- **Trademark plan:** word mark "LetterLyn" (classes 9 + 41) at OSIM just before launch; Lyn will be the brand face, so Lyn's image mark is planned too, filed once the art is final, ideally together with the word mark (same priority date). 6-month Paris priority: claim it explicitly, same mark/goods/owner. Copyright on all art is automatic; keep dated source files. Details in the launch checklist.
  - **Ownership (option B, Doru 2026-11-23):** Remus transfers the copyright on Lyn + art to Doru personally (permanent, in writing per Romanian law, Remus stays credited); Doru files both marks at OSIM in his own name; Doru gives smartdevsolutions a free licence and assigns the code/content he makes. Remus (50% B shares) must agree; ask the accountant about the free licence. Papers at launch, checked by a lawyer.
  - **Image mark (2026-11-24):** one mark = **full-body Lyn**: the winning variant (**variant 11**, chosen 2026-11-25 by the vote), final polished drawing, final colour, alone on a plain background (no number, text or frame). File **in colour** (EU common practice: a black-and-white filing does not cover colour versions), so only once art and colour are final. Keep it separate from the word mark (no combined logo mark: copying just the name or just the character must each hit a mark).
  - **Head-only app icon:** the icon will likely show only Lyn's head (a full body is too small at icon size). No separate head mark for now: the full body counts as used (game, splash screen, store screenshots, ads), the head is its dominant part so a copied head on a new body is very likely confusingly similar, and the copyright covers the drawing in any form (an earlier copyright can also cancel someone else's mark). Add a head-only mark later only if the icon becomes famous on its own.
  - **Watching:** OSIM does not block similar marks by itself. Watch new filings (lawyer or cheap watch service, at least yearly) and oppose within **2 months** of publication; after that only invalidation (slower, costlier).
  - **Classes:** 9 (apps) + 41 (games); 28 (toys) / 25 (clothing) only if merch is really sold.

## 25. Kids, words, learning, economy (2026-11-22, wireframes v30)

**Principle for all features:** everything gets fully specified now (wireframes, logic, data, place in the app), even if it ships later. The roadmap, written after the specs are settled, decides order and timing per feature.

- **Lyn has no gender.** Standard look stays neutral; in texts Lyn is always "Lyn" (no he/she). Outfits let players style Lyn (bow, dress, moustache, bow tie, top hat). Romanian copy must avoid gendered adjectives about Lyn ("Lyn s-a bucurat!", "Lyn: Bravo!").
- **Age question (first run, after language):** Lyn holds a sign "Hatched: 2026… already eaten 1,000 books", asks "And you? When were you born? I'll keep it secret". Book-spine year picker. Neutral (no answer unlocks anything; one friendly line per decade). Asked once, change via Support only.
- **Kids policy:** we're a general-audience game, not the Kids category. Child = under the country's consent age (RO 16, IE 16, UK 13, US 13…; country from store region); becomes adult automatically. Five differences only: (1) non-personalised child-safe ads (ad network flagged); (2) no purchase pop-ups / offer banners / countdowns, shop only when opened, store asks parent; (3) anonymous totals only, no marketing notifications; (4) custom puzzles stay on the device; (5) rude words never shown or allowed. Leagues, clubs, friends and reactions stay (nothing typed). Code: `ageGroup` → one `policy` object `{personalisedAds, showOffers, detailedAnalytics, customPuzzleSharing, rudeWords}`; features read the policy, never the age; server stores `ageGroup`.
- **Already covered (checked):** bad-word scan of every grid line in 8 directions (admin content); club names from lists; Settings item renamed "Delete my account and data" (store requirement wording).
- **Report a puzzle:** ⚑ from the puzzle menu or "Well done": reason list (wrong spelling / doesn't match topic / not really in grid / offensive / too hard / other) + optional note seen only by us; app attaches puzzle id, word, language, difficulty, app version → admin Reports.
- **Accessibility:** Settings → Accessibility: letter size Normal/Medium/Large, high contrast, reduce motion (follows the phone; confetti, stamp landing, count-ups, animated frames, Lyn's moves become fades), sounds / haptics / read-aloud switches, screen-reader labels on all menus (playable grid later). No left-handed layout (nothing to mirror). **Tap mode:** off by default, never together with drag; same letter again = deselect, a letter not in line = new start, wrong word shakes and clears; turning it on runs a tap tutorial.
- **Launch plan (decided 2026-11-22):** Phase 0 closed test ~2 weeks (friends, family, Remus, Doru's friend in Ireland; Play closed testing + TestFlight). Phase 1 soft launch **Romania + Ireland**, 4–6 weeks (Romania: Doru's feedback, word of mouth, RO content; Ireland: English content + near-UK ad income; the friend there helps test and spread the word). Judge on strangers (~500–1,000 installs), not friends. Bars before worldwide: next-day return ≥ 35%, week ≥ 12%, crash-free ≥ 99.5%, tutorial ≥ 85%, no outlier puzzle/screen, Ireland ad income ≈ €0.35–0.55 per daily player per month; under a bar → fix and extend. Phase 2: worldwide at once (not country by country), minus licence-required countries (China iOS, Vietnam).
- **Measuring (decided: measure everything we can, own server, no per-use cost):** returning after 1/7/30 days (word-game targets ~40% / 15% / 6%); puzzles per day, session length, streaks; where people quit (tutorial step, puzzle, difficulty); ads per player per day, optional-ad use, purchases, income per daily player; per-puzzle time, hint use, quit rate; crashes, load times, offline vs online. EU: detailed tracking only with consent; otherwise anonymous totals (listed on the Consent screen).
- **Word card (LAUNCH):** tap any found word → meaning, example, 🔊 phone voice (free, offline), Lyn's fun fact, save. **Word of the day (LAUNCH):** after the daily, Lyn presents one of its words.
- **Meanings:** our own short text per concept and language, drafted offline once and checked. Not DEX (its definitions belong to publishers; can't be used commercially).
- **No-repeat rules:** daily topic not again for 60 days; a word not in any daily for 90 days; word of the day never within 365 days, only from approved meanings. Server plans ahead; admin calendar warns when the pool runs low.
- **Content moves to the database** (managed in admin; feed built from it; apps unchanged, still ship a built-in copy): concepts · words (concept, language, display, meaning, example, status, pronunciation later) · shelves · packs (kind universal/local, learning directions, sequel of) · pack_words · puzzles (generator version, frozen grid) · dailies (with word of the day) · reports. A pack can't publish until every word has an approved meaning + example.
- **Learn mode (two languages; roadmap decides launch vs later, likely launch):** Play → Learn shelf → pair; grid in the language you learn, list in yours (CÂINE → find DOG). Built on concept ids. Romania-only packs only in the direction whose grid is Romanian, with a description clue; set per pack; left out at first. First shelf of every pair free. Learn puzzles give XP, never coins; not ranked.
- **My words + repeat to remember:** save from any card (free). Boxes 1–5: found with no hint = up a box; miss / hint / gave up = back to box 1. Next review 1 / 3 / 7 / 14 / 30 days; after box 5 = learned. Max 10 per review, oldest overdue first; skipping days loses nothing. Review = small 6×6 grid of due words with clues in your language; no coins, no ads. Later: listening review, recorded native voices.
- **Learning prices:** one-time pair ~€4.99 forever (both directions, all universal packs incl. future ones, cards, voice, review). Later (3+ pairs): Learn subscription ~€3.99/month or €24.99/year for all pairs + recorded voices; pair buyers keep theirs. Both stay available. Separate from Plus and the Journey ticket.
- **Custom puzzles (first version):** Me → My puzzles → Make: title, optional "from", 6–15 words, difficulty; grid size automatic. Rude-word check blocks in child mode, warns adults. Played by handing over the phone ("A puzzle from Mom"). No coins / XP / streak / tasks. Saved up to 50: play, edit, copy, **print as PDF**, delete. Not shareable yet. Later: send to friends (friends only, slurs always blocked, mild swearing only between consenting adults, report + block, never children).
- **Widget (later):** home-screen countdown + streak (+ word of the day on medium size); tap opens the daily; no server cost.
- **Holiday dailies (later):** themed words + grid background + a stamp and postcard only that day; still ranked; Romanian dates for Romanian players.
- **Journey ticket:** no 4th daily task or anything that pays coins; 6–8 cosmetic items a month (not 10–15).
- **Slow to earn (starting rule, only ever loosened):** nothing big in a day; regular free player gets something noticeable every 1–2 weeks and a theme every ~3–4 weeks; the launch catalogue (~30,000 coins) takes a regular ~9 months, heavy ~5. Earn: pack puzzle 3/5/7, no-hint +2, mystery +2, daily 10 + 1 per streak day (max +10), Quick Play 5 (first 3 a day), tasks 5/10/15 + 20 for all 3, level +25, streak gifts 30/60/120, league 150/100/75/40, optional ad +10 (max 5 a day). Prices: hint 25, first letter 10, freeze 150, past daily 50, picture 300, frame 500, outfit 800–1,500, theme 1,500–2,500; sets €2.99 (~1,000 coins of items per €1). Free gifts: picture/frame every 5 levels, outfit at levels 10/25/50, theme at 20/40. Day earnings ≈ casual 45 / regular 120 / heavy 200. Full tables and examples: Content & Coins page §3. **(2026-11-25: item gifts replaced by coins, see §27h; proposed level/streak-goal/invite amounts on the content page.)**
- **Friends abroad and languages (2026-11-22):** Doru has friends in Ireland, Italy (living in Vietnam), Poland, Czechia, Spain, Hungary and a UK friend in Hong Kong. Uses: closed test (each test round has its own country list, so friends abroad can join; confirm Vietnam), native-language opinions, word of mouth at the worldwide launch. Their friends and acquaintances count as real "strangers" for the soft-launch bars; close friends don't.
- **Countries:** mainland China out (iOS game licence). Hong Kong fine (own stores, no licence rule). Vietnam to check near launch (licence rule mainly for games with in-app purchases).
- **Language friends:** native speakers check word lists, meanings, examples and app texts before a language goes live. Thank-you: lifetime Plus, given from the admin site. No money, no credits list.
- **Admin gifts:** Players → Give a gift: Plus (lifetime), a learning pair, a look set, coins (max 1,000) or hints (max 50); reason required (language friend, tester, support fix, prize, other); signed-in players only; player sees "A gift from the LetterLyn team"; logged with admin + reason, reversible, shown in Purchases as "gift · €0" so income stays true. **Next languages are chosen by who can check them:** Polish, Czech, Spanish, Italian, Hungarian; order set in the roadmap.

## 26. Everything we can offer, and the full content catalogue (2026-11-22, wireframes v32)

**Goal (Doru):** plan every feature we can think of now, however far away (1, 2, 3 years), until only "more content" is left. The roadmap then decides when. All ideas below are approved and marked **later**; all are in the wireframes (sections "More ways to play", "Family, school, friends", "Collections, memories, content extras", "Help, live settings, roles").

- **Modes:** clue mode (meanings instead of words) + no-list Expert mode; picture reveal; shaped grids (heart, tree, egg, country outlines, Lyn); monthly mega puzzle (20×30, ~60 words, over the month, stamp + frame, not timed); Blitz (60 s, weekly board, coin reward once a day only); live 1-vs-1 race (websocket server); story chapters with Lyn. Modes get their own small stamp sets.
- **Family, school, friends:** up to 5 profiles per device (adult PIN, child profiles use kids rules, Plus covers the device); classroom mode (teacher words, class code, printable sheets, results; no pupil personal data; later a paid school licence); gift codes for Plus (website, redeem in Settings, store offer codes, admin code batches); **Family Sharing for Plus: to decide**; ghost replay of a friend's solve; invite a friend (both get a frame at the friend's level 5, never coins).
- **Collections and memories:** "Your year in words" card; personal stats; word collection (all unique words per shelf, feeds Lyn's bookshelf); Lyn's letters inbox; welcome back after 7+ days (freeze or 50 coins, max monthly, never guilt); vote for next month's pack (catalogue options, signed-in, one vote).
- **Content extras:** little-readers picture shelf (picture clues, read aloud, big grids, across/down); specialist vocabulary learning packs (medicine, cooking, geography, programming); local packs for every new language.
- **Behind the scenes:** live settings from the server (prices, rewards, ad timing only within the promise) + A/B tests + messages to everyone (needed early, for soft-launch tuning); admin roles: owner, admin, **language checker** (own language only, approve/suggest), support; help centre (FAQ from admin, contact form with player ID); download my data (GDPR); dyslexia-friendly font; app language separate from puzzle language.
- **Outside the app:** printed puzzle books (Amazon print on demand) and printable PDF packs on the website (passive income, no running cost); daily puzzle licensed to websites/newspapers; store promo codes.
- **Platforms:** tablet/iPad layout, Discord Activities, Telegram mini app, Facebook Instant Games, Steam/PC, Game Center / Play Games achievements.
- **Getting known:** website + press kit, store trailer, social accounts, keywords/screenshots per language, Apple/Google featuring nominations, opt-in newsletter.

**Content volume (researched 2026-11-22):** Wordscapes Search advertises "over 6,000 free puzzles"; for the original Wordscapes players report that after ~6,000 levels puzzles repeat (the level counter goes past 24,000 with recycled grids). Our plan: ~300 packs ≈ 7,500 topics ≈ **22,500 playable puzzles** (3 difficulties), plus 365 dailies a year and endless Quick Play; packs have no ceiling (more shelves, narrower topics, sequels). 7,500 is a release total, not a stock: casual players (~1,100 puzzles/year) match 4 packs/month; regular (~2,200/year) and heavy (~7,300/year) players catch up and use other difficulties, daily, Quick Play, modes. **Pace target: 4 packs/month at first, 6–8 once language friends + the checker role work.**

**Content catalogue (decided):** plan every shelf, pack and puzzle topic now (~30 shelves, ~300 packs, ~7,500 topics; English titles first, other languages added with the words). Words + meanings are written for launch packs now and for every other pack 2–3 months before its release, then checked. **Changed 2026-11-22: all English words are drafted now (see §27).** The catalogue is data in the letterlyn repo (`packages/content/catalog/`), same shape as the future database, with a browsable page.

## 27. Catalogue v2: freshness, data checks, rules sheet (2026-11-22)

- **Rules sheet:** `letterlyn/rules.md` holds every decided rule and number (newest wins). It's checked before any rule is stated. Reason: a square-grid mistake taken from the old prototype code, when tall grids were already decided.
- **Whole catalogue drafted now (Doru):** every shelf, pack, topic and English word, so words are settled across all packs before any pack is published. Published packs are locked, so finding duplicates later would be too late. Drafts can change. Before publishing, run the checker against all drafts. Romanian words come in a second pass.
- **Packs per shelf:** ~10–12 in the plan (337 packs ≈ 4 years at 6–8 per month). 30 per shelf would be 11+ years of releases. Shelves stay open.
- **Trophies:** bronze 3 / silver 6 / gold 10. Platinum 15 and a tier at 20 are added when shelves really hold that many (never remove a trophy). **Superseded 2026-11-23: bronze 5 / silver 10 / gold 15 (whole shelf), 15 packs per shelf, exactly 20 topics per pack (rules sheet).**
- **Topics per pack:** 20–30, set by how many fresh words a pack can hold.
- **Pack names:** no "X and Y". Split (Sharks + Whales), rename (Insects) or merge (Natural Disasters). Each pack has `covers` and `leaves` notes so every topic has one owner.
- **Checker:** `letterlyn/packages/content/scripts/check-catalog.mjs` → `catalog/report.json`. Rules:
  - topic titles unique in the whole catalogue;
  - 16–18 words per topic, letters only, no doubles;
  - a word in at most 3 topics per pack;
  - at least 60% of a pack's words new to its shelf;
  - level fit per word.

  The admin "Content health" screen reads the same report later.
- **Lesson from the Animals draft:** each pack along a shelf is less fresh (100% → 35%). Generic words wear out (TINY, NEST, TAIL, NIGHT…). Concrete topics stay fresh; vague topics don't. Packs that only re-angle other packs can't be fresh: Baby Animals 35%, Animal Homes 41%. They're replaced by Asian Animals and Animals of the Americas; baby animals move to the kids picture shelf (later).
- **Word length vs tall grids** (7×9 / 9×12 / 11×14):
  - A word fits a level if it fits across: up to 7 letters for Relaxed, 9 for Classic, 11 for Expert.
  - At most 1 longer word per puzzle goes down only: up to 9, 12 and 14 letters.
  - 15–20 letters: the 20×30 mega puzzle only. Over 20: never.
- **Two-word names:** joined in the grid, with a space in the word list.

### 27b. Repeats in play order, two-word names, hidden words (2026-11-22)

- **Play order rule (Doru):** repeats only feel boring puzzle after puzzle (the first draft had FISH in 3–4 consecutive puzzles). A word may not come back within the next 4 puzzles in play order (shelf order, then pack order, as the Continue button plays them), including across pack boundaries. Shelf-wide freshness is information only.
  - Measured on Animals: 46 back-to-back repeats and 187 within 5 puzzles. Reordering topics (`order-topics.mjs`) brought it to 7, and word swaps to 0.
  - A pack's first topic is its headline topic and stays first.
  - The generator will also skip recently seen words when choosing a puzzle's subset (to build).
- **Two-word names:** stored with proper spacing ("GUINEA PIG"), joined only in the grid; none in Relaxed, at most 2 in Classic and 4 in Expert; a first-time tip; watched in the soft launch.
- **Hidden-inside pairs:** the engine drops a word that sits inside another one in the same grid. The Animals draft had 180 of them (BEE + BUMBLEBEE, SEAL + HARP SEAL). The checker now counts the topic the way the engine does, and every case was fixed: keep the headline word, drop the compound.
- **Animals result:** 294 topics, 4,867 word slots, 3,195 different words, 0 warnings.

### 27c. Bonus words (decided 2026-11-22, wireframes v34)

Idea from Doru (his kid asked about it). A real word traced in the grid that isn't on the list fills **Lyn's bonus jar**. Nothing is marked in the grid; a small "+1 bonus: OCEAN" toast shows.
- **Reward:** every 10 bonus words pay 10 coins (about 1 coin per word, in line with a puzzle paying 3/5/7). The jar restarts after paying.
- **Badge:** "Sharp eyes" in the Album at 50 / 250 / 1,000. Also a metric: bonus words per puzzle.
- **Rules:**
  - 4+ letters; counts once per puzzle.
  - First solves of pack puzzles, the daily and the first 3 Quick Plays a day only, so replays can't be farmed.
  - Not inside a list word, and rude words never count (kids get no message).
  - No effect on daily rank or time. Learn mode: XP only.
- **Screens:** jar chip on the puzzle screen → Bonus jar screen (this puzzle's bonus words, all bonus words, badge progress, rules).
- **Build needs:** see §27d (our own word list, every grid made in advance). The server re-checks bonus words with the other earnings.
- Generic genre mechanic; our own design (Lyn's jar). The roadmap decides when it ships.

### 27d. Every grid made in advance; our own word lists (2026-11-22)

- **Words are free; files aren't.** Nobody owns a word, but someone's compiled dictionary file is protected (copyright on selection and definitions; the EU database right against copying large parts). So we don't copy any dictionary. Our word lists are our own work.
- **How bonus words are recognised:** the script reads every line of a grid in 8 directions and looks up each run of 4+ letters in our bonus word list. A computer can only recognise words that are on its list. So one general list per language: catalogue words + our own everyday words + a frequency run (about 1M random grids on Doru's PC, count the frequent 4–7 letter strings not yet in the list; I mark the real ones, Doru checks Romanian).
  - Reading every possible Quick Play grid isn't practical: 66M grids give hundreds of millions of unique strings, about 4,000+ review passes, and it would still need a word list to narrow down.
- **Every grid is made in advance and checked**, Quick Play included:
  - Quick Play is a pool of ~50 grids per pack per size (~50,000+, growing); no repeats until all are seen; friend codes point to pool grids.
  - Each grid only varies word selection, placement, direction and fill letters; the words are always ours. A pool grid feels as fresh as one made on the spot.
  - Result: no grid reaches a phone unchecked, there's no ban list on the phone, and no unknown bonus words appear in any mode.
- **Ban list:** per language with the language friends; kept on our side; every grid scanned in 8 directions before shipping.
- **Generator:** one, fixed, tested, versioned (version stored with every puzzle).
- **Fallback (Doru):** if players say Quick Play feels repetitive, go back to grids made on the phone, with the ban list as hashes, and accept the small risk (and maybe license a big word list once there's money).

### 27e. Languages and Learn mode words (decided 2026-11-23)

- Doru's worry: English words fit the grids, but other languages are often longer. Normal puzzles are fine because **each language has its own words and its own grids** (same sizes; each level picks that language's shortest words; topics can differ or be left out per language). The real issue is **Learn mode**, where two languages meet.
- **Learn puzzles are their own puzzles** per pair and direction, frozen like all grids. Grid in the language being learned (only its lengths matter), list in the player's language (labels wrap). They use **only shared concepts**.
- **English is the hub:** every word links to an English concept, so any pair (RO–DE) works through the shared concepts. Data: `words.ro` lines up with `words.en` (`null` = not used), RO-only words in `extra.ro`.
- **Shared core:** a new language keeps at least 12 of a topic's English concepts where it can, so Learn Relaxed + Classic work. The checker counts shared concepts that fit each level per pair; topics without enough stay out of Learn for that pair (or easier level only). Two concepts sharing a word in either language (HARE/RABBIT = IEPURE) never share a Learn puzzle.
- **Fix order** for any language: shorter real word → another word → down-only/mega-only → leave the topic out in that language. Packs lock per language.
- **Test first:** Romanian words for Pets and Farm (58 topics) before writing the other 30 English shelves, to see how big the shared core really is.

### 27f. Bug: the daily timer resets when you leave (found by Doru, 2026-11-23)

- **Problem:** the daily clock lives only in the open page (`packages/engine/src/game/session.ts`). Leaving and reopening the daily starts a new session at 0:00, and the server only checks that the submitted times are consistent, not when the puzzle was first opened. Cheat: find all words, leave, reopen, re-mark them from memory → a very fast ranked time. Same for any ranked puzzle (friend codes, Quick Play).
- **Proposed fix (to decide, then build):**
  1. **Resume, never restart:** a ranked puzzle's progress (found words + elapsed time) is saved on the device the moment it changes; reopening continues where you left off, with the clock where it was.
  2. **Server start time:** the server records when it hands out today's daily key to a player (first open). Each found word is sent with its time (already so); the server rejects or flags a result whose time is clearly shorter than the plausible play time since first open, and never ranks a second "first open".
  3. **One ranked attempt per device and account:** reinstalling or clearing data doesn't give a new ranked try (the server already keeps "first try only").
- Until fixed: leaderboards can be gamed by a determined player; fine during closed testing.

### 27g. Player names: unique, built from lists, online only (decided 2026-11-23)

- Today names are random and NOT unique (`apps/api/src/players.ts` picks without checking); 32 × 32 × 90 = 92,160 names, and duplicates become likely after a few hundred players.
- **Build list:**
  1. Unique index on (nick_adj, nick_noun, nick_num); give out the shortest free number for the pair (10–99, then 100–999, then 1000–9999); retry on conflict.
  2. Number column range 10–9999 (SMALLINT is enough).
  3. Grow `packages/content/src/nicknames.ts` to ~100 adjectives + ~100 animals (append-only; Romanian adjectives in m/f forms, nouns with the article, gender set per noun). Kid-safe, no animal that is an insult in any language we ship.
  4. Name picker: adjective list + animal list + random button; server returns the name or "taken, try another word". Disabled offline ("Needs internet").
  5. First launch offline: no player and no name until the first online moment; then create the player, keep local progress (cloud save takes it over).
- Done already (2026-11-23): Romanian nouns use the article (Vidra, Ursul…), so names read "VidraCalmă42".

### 27h. Rewards, names, email (decided 2026-11-25, after Doru looked at Duolingo)
- Duolingo sells gems, uses energy and sells a monthly "no ads + unlimited" plan. That works for learning (people feel they pay for education), not for a puzzle game; we keep our rules: coins never sold, no energy, subscription only maybe later for Learn mode.
- **Rewards are coins**; cosmetics are bought with coins. Earned-only, never sold: stamps, shelf trophies, league medals, Sharp eyes badge, Plus supporter frame/badge.
- **Streak goal** (commit to 7/14/30/50 days → bonus coins) and **invite a friend → coins** (paid when the friend finishes a first pack). League tiers with promotion/demotion zones: later.
- **Names stay built from lists**; typed names only if many players ask (they need moderation).
- **Email by opt-in** (rules sheet "Email and notifications"): notification emails mirror push (on/off per type in settings, so web players get them too) and a separate newsletter opt-in with unsubscribe. Double opt-in, adults only, not on portals, deleted when both are off.
- Proposed economy v2 (content page "The math", model letterlyn/tools/economy-model.py, waiting for Doru): faucets ~40% lower (puzzle 3/4/6, daily 8 + streak up to 5, tasks 4/6/10 + 10, level +15 with 50/150/300 milestones, streak goals 30/75/200/350, invite 75, ads +8 × 3, league 100/70/50/25); prices up for looks (picture 400, frame 700, outfit ~1,500, theme ~3,000, freeze 200) and down for hints (15). Regular: first theme ~6 weeks, buys 1/3 of each month's new items; heavy 77%; shop never empties. Decided 25 Nov: no free freeze from tasks (streak goals 7/30 give one); Plus never gives coins (1 free hint/day is the limit); look sets stay €2.99.
- Updated 2026-11-25: wireframes v40 (new screen 15b Settings → Notifications; Tasks streak goal; Social invite card; Shop/Profile/Room/Journey/Complete looks bought with coins; trophies 5/10/15 and new shelf names in Packs/Album/Friend; league tiers 'later'), content & coins page v13, art list v7, launch checklist v16.

### 27i. Avatars: name animal + accessories (decided 2026-11-25)
- Doru saw Duolingo's avatar editor (layered face, hair, glasses, hats). Chosen instead: the avatar is the player's name animal plus accessories. Replaces the ~20 profile pictures. **Lyn is not dressed by players** (Doru: Lyn is our trademark, not their mascot): standard Lyn everywhere plus a few seasonal looks we choose; Lyn outfits are dropped (a worm can't wear dresses or pants, and it would double the dressing).
- Editor tabs: Animal & colours · Face · Head · Neck & clothes · Accessories · Background. Free at the start: a limited set; the rest unlocked with coins; may become free later if the game earns enough.
- Build: layered drawing from a small choice list saved with the account; editor screen with tabs (hats, glasses, neck, face…); server checks owned items. About a week of code.
- Art (Remus): one head drawing per name animal (32 now, ~100 as the list grows) with anchor points (head top, ears, eyes, muzzle, neck), a recolourable fur layer and 2–3 markings; ~40 accessories at launch, new ones monthly; Lyn: a few seasonal looks a year. Must read at 32–56 px.
- Economy: accessories replace pictures and Lyn outfits in the shop (launch shop ≈ 6 themes + ~32 paid accessories + 10 frames, about the same coin total; ~4 new accessories a month).

### 27j. Avatar and art ideas (approved as ideas 2026-11-25; the roadmap decides when/if)
1. **Streak achievements merged into streak goals:** the 3/7/30-day streak achievement badges are dropped; the streak goal badges (7/14/30/50) are the only streak badges.
2. **Animal reactions:** friend reactions (👏, "Well done!") shown by the sender's animal with a small expression/gesture (expressions are already shared avatar layers).
3. **Free accessory of the month: DECIDED for launch (Doru, 2026-11-25), harsh rule:** every day of the month done by month end (daily on the day, or later as a past daily: free with Plus, 50 coins otherwise; streak-freeze days count). Mid-month joiners can catch up the earlier days the same way (the archive goes back to launch): free with Plus, ~1,200 coins for 24 days otherwise. The one exception to "no cosmetics as rewards"; a reason to keep Plus (catch-up) and a coin sink (past dailies). Loosen later if needed.
4. **Animated Lyn cheer** on the puzzle-complete screen (1–2 s loop) instead of the still pose.
5. **Try on before buying** in the shop: preview an accessory on your animal (code only).

