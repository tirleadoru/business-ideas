# Game Design: Local-First Word Search (v0.1, 2026-11-19)

> Research behind this: see `MEMORY.md` §4 → "Word-search deep-dive", "Word-game deep-dive".
> Status: **draft for review**. Nothing is built yet.

## 1. One-line pitch
A calm, fair word search that feels *made in your language*. It uses native themes, correct diacritics and ads that never get in your way. It also has a mode that teaches you another language while you play.

## 2. Why this can win (evidence)
- **Big, proven demand.**
  - The app the user found (Italic Games): 10M+ installs, about $50K+/month estimated, 100% ads.
  - The leaders (Explorer, Journey, Quest): 100M+ installs each.
- **Weak local competition.**
  - **No native Romanian word search exists.** Search "careu de cuvinte" on Google Play: no native result.
  - The best Turkish native app has about 50K installs. German, Brazilian Portuguese and Spanish native apps are tiny.
  - Global apps translate only the store listing, not the content.
- **Fixable complaints.**
  - Loud ads that ignore mute, fake "virus" ads, ads in the middle of a puzzle.
  - Repetitive or too-easy puzzles, and an unclear language switch.
- **Learning gap.** Word search for vocabulary learning exists only as tiny paid iOS apps.
- **Open portal slot.** Poki and CrazyGames run one 2020 word search (4.1★ on Poki, 8.5 on CrazyGames) with a timer, no levels and no hints.
- **Caveat.** "No ads / large print" alone does not win (2026 indie apps with those pitches have tiny installs). Distribution comes from **portals + local store keywords + content quality**.

## 3. Name (checked 2026-11-19, user to pick)
One brand name everywhere: stores, portals, domain, social. Store titles add the local keyword:
`<Brand>: Word Search` / RO `<Brand>: Careu de cuvinte` / DE `<Brand>: Wortsuche` / TR `<Brand>: Kelime Avı` / PL `<Brand>: Wykreślanka` / PT-BR `<Brand>: Caça-palavras`.

**Shortlist** (.com free per whois; no app with the same or a near name on Google Play or the App Store):
| Name | .com | .game / .io / .net | Feel |
|---|---|---|---|
| **Letter Moss** | free | free | cozy, nature, calm |
| **Letter Hush** | free | free | quiet, "the calm one" (matches the fair-ads pitch) |
| **Letterlyn** / **Wordlyn** | free | not checked | short, brandable, sounds like a name |
| Letter Still | free | free | calm, a bit flat |
| Word Sanctum | free | free | "a quiet place for words", a bit heavy |

**Trademark/collision check (2026-11-19):**
- ❌ **Letter Moss** (the user's first pick) is **dropped**.
  - Another developer, Blackline Studio Art, already has **"LetterMoss: Филворд"**. It's a word search game ("Филворд" = Russian for word search) in a Google Play closed test, with a privacy policy dated 17 Oct 2026 (github.com/blackline-studio-art/lettermoss).
  - Same name, same genre, earlier use → too risky.
  - Also, Polyarc holds a live US mark **MOSS** for games in classes 9 and 41 (Reg. 5846030).
- ✅ **Letterlyn**: no web, GitHub or store hits. It's a coined word, the **strongest type of trademark**.
- ✅ **Letter Hush**: no web, GitHub or store hits.
  - Plain "HUSH" marks exist in classes 9 and 41 (HUSHTech, Hush Communications…), but none is confirmed for games.
  - "Letter Hush" as a whole is distinct. Risk is low but not zero.
- ⚠️ The TMview/EUIPO API blocks automated queries → **the user must run a 5-minute manual search** at tmdn.org/tmview (offices EM, RO, US, GB, WO) and on the USPTO Trademark Search, before registering the domain.

**Rejected:**
- Domain taken: Wordfield, Wordhaven, Wordnest, Wordgrove, Wordloom and about 25 others.
- Too close to an existing app:
  - Letter Lanes (*Word Lanes*).
  - Letter Breeze (*Word Breeze*).
  - Letter Pebble (*Word Pebbles*, *Pebble Word Puzzle*).
  - Letter Sprig (*Sprig: Queens Logic Puzzles*).
  - Letter Mosaic (*Word Mosaic* by Fugo).

**Before locking the name:**
1. Trademark search in EUIPO/TMview and USPTO, classes 9 and 41.
2. Check CrazyGames/Poki and social handles.
3. Register the .com under the company.
4. Reserve the Play package ID (e.g. `com.smartdevsolutions.<brand>`) and the App Store name.

Note: whois reported .app as taken for every name, which is probably a parsing issue, so check .app manually at a registrar.

## 3b. Languages (decided 2026-11-19)
- **English is the main, default language.** It's the biggest audience and the highest-paying ads (US/UK eCPM). We accept the crowding.
- **Romanian is the first extra language,** and it's in the app at launch. The app follows the device language, with an in-game language switch (a common complaint: "how do I change the language?").
- Store listings are localized per language, so the RO listing still ranks for "careu de cuvinte", where no native competitor exists.
- After launch: TR, PL, PT-BR, DE… The local theme packs stay the edge in each language.

## 4. Core loop (one puzzle = 1–4 minutes)
1. Pick a **theme pack**, e.g. "Romanian dishes", "Carpathian animals", "Football: Liga 1", "In the kitchen".
2. The grid shows 6–12 hidden words. **Drag** across letters to select a word.
3. A found word is highlighted, crossed off with a satisfying sound and haptic, and (optionally) shows a **mini fact card** (definition, or translation in learning mode).
4. Puzzle complete → stars (based on hints used, never a timer by default) → coins → the next puzzle.
5. Finishing a theme pack (10–20 puzzles) earns a **stamp** in the player's "album". That's the collection meta and the long-term goal.

**Modes**
| Mode | Description | When |
|---|---|---|
| **Journey** | Theme packs with a gentle difficulty curve | MVP |
| **Daily puzzle** | One puzzle a day, the same for everyone in that language (seeded by date, works offline), with a streak counter | MVP |
| **Learn mode** | Clues in *your* language, grid in the *target* language ("dog" → find **CÂINE**), translation cards, an offline review list | v1.1 |
| **Custom puzzle** | Type your own words (teachers, parents, birthdays) and share via a link or code; printable PDF | v1.2 |
| **Relaxed / Challenge** | Relaxed (default): no timer. Challenge: optional timer and a "find bonus words" target | MVP / v1.1 |

## 5. Difficulty curve
| Stage | Grid | Directions | Words |
|---|---|---|---|
| Intro (packs 1–2) | 6×6 – 7×7 | → ↓ | 4–6 |
| Easy | 8×8 | → ↓ ↘ | 6–8 |
| Medium | 9×9 – 10×10 | + ↗ | 8–10 |
| Hard | 11×11 – 12×12 | + backwards ← ↑ ↖ ↙ | 10–12 |

- Filler letters are drawn from the **language's own letter frequency**, so grids look natural and don't give words away.
- Filters stop accidental offensive words from appearing in the filler.
- Words must not overlap in confusing ways, and each grid should have only one valid solution path per word.

## 6. Content model (the real moat)
Use **concept-based packs**: one concept ID with a native form in each language.

```
concept: animal.dog
  ro: CÂINE   de: HUND   tr: KÖPEK   pl: PIES   pt-BR: CACHORRO   en: DOG
```

- **Universal packs** (animals, food, home, body, nature) share concepts across languages. Each new language reuses the structure, and the learning mode becomes cheap because every concept has a translation.
- **Local packs** exist per language only, and are the identity layer: RO dishes, RO cities, Liga 1 clubs, proverbs, Romanian writers and so on. These are what global apps don't have.
- **Sources:**
  - Frequency lists (hermitdave FrequencyWords, CC-BY-SA-4.0, with attribution).
  - Hunspell dictionaries for spelling checks (license varies by language).
  - Wiktionary/kaikki translations (CC BY-SA).
  - ⚠️ **No official Scrabble lists** (they're licensed).
  - Content can be drafted with AI **at build time only** (no runtime cost). Every pack gets reviewed: by the user for RO, and by a native reviewer (paid per pack, small one-off cost) for other languages.
- **Text rules:**
  - Locale-aware upper-casing (Turkish i→İ, ı→I).
  - Romanian uses **comma-below ș ț** (U+0219/U+021B), not the cedilla forms.
  - Grids show the real letters with diacritics. An optional setting "ignore diacritics" lets Â=A and so on.
- **Target per language at launch:** 30 packs × 15 puzzles = **450 puzzles** plus endless daily puzzles. Grids are generated, packs are curated.

## 7. Monetization: the "fair ads" contract
Shown on the store page as a selling point.
- **Rewarded ads (opt-in):** extra hint, double coins at the end of a puzzle, unlock a pack early.
- **Interstitials:** **never mid-puzzle**. At most one every 3 completed puzzles, and none in the first 5 puzzles of a session (subject to change after data).
- **Every ad respects the device mute or in-game sound setting** where the SDK allows. Muting is the default when sound is off.
- **No fake "virus" or scam ad categories.** Block sensitive categories in the AdMob/portal ad settings.
- **"Remove ads" in-app purchase:** about €2.99–4.99 one-time. It **really removes interstitials, forever, restorable**. Rewarded ads stay available as opt-in.
- **Optional later:** paid premium pack bundles, plus a "Supporter" option.
- **Portals:** CrazyGames/Poki ad SDKs only (no in-app purchases on Poki).
- **No pay-to-win, no energy system, no fake events, no dark patterns.**

## 8. Platforms & tech stack (one codebase)
- **Game:** TypeScript + a light renderer. Recommended: **plain DOM/CSS grid or Canvas, with Vite**. Word search is UI-like and doesn't need a game engine. That makes it small, fast to load (portals reward fast loads) and accessible (large fonts, high contrast, screen-reader labels).
- **Platform adapters:** one `ads` / `storage` / `analytics` interface, with implementations for:
  - CrazyGames SDK v3.
  - Poki SDK.
  - **Capacitor** (Android/iOS) + AdMob (`@capacitor-community/admob`) + store in-app purchases + Google UMP consent (**GDPR consent is required in the EEA/UK**).
- **Content pipeline:** build-time scripts turn word sources and curated packs into compact JSON per language. Puzzles are generated deterministically from seeds (also used for daily puzzles and shared custom puzzles).
- **No backend.** Progress is stored locally, with optional cloud save via Google Play Games / Game Center later. Analytics: Firebase (free tier) plus the portal dashboards.
- **Store accounts:**
  - Google Play $25 one-time.
  - Apple $99/year.
  - ⚠️ A *personal* Play account requires a closed test with 12 testers for 14 days; an **organization account** skips this (needs a D-U-N-S number). Decide which account the product ships under (see the repo note on the company account).

## 9. Milestones
| # | Milestone | Output | Rough time |
|---|---|---|---|
| M0 | **Engine prototype** | Grid generator, drag selection, word validation, 3 test packs in EN + RO, playable in the browser | 1–2 wks |
| M1 | **EN + RO content + polish** | 30 packs per language, daily puzzle, stars/stamps, sound/haptics, settings (size, contrast, diacritics) | 2–3 wks |
| M2 | **Portal launch** | Submit to CrazyGames (+ Poki) with the EN + RO + 2–3 languages | 1 wk + review time |
| M3 | **Measure** | Retention and playtime from the portal data; fix the curve | 2–4 wks |
| M4 | **Mobile** | Capacitor Android (+ iOS), AdMob, remove-ads purchase, store listings per language | 2–3 wks |
| M5 | **Languages** | TR, PL, DE, PT-BR, CZ, HU…, ~1 week each mostly content | ongoing |
| M6 | **Learn mode** | Bilingual mode + review list; listings per language pair | 2–3 wks |

**Go / no-go gates (decide after M3):**
- **CrazyGames metrics:** about 15+ minutes average playtime, and day-1 retention at least on par with similar puzzle games there.
- **If weak:** fix the curve and content first, then re-test, before investing in mobile.

## 10. Open decisions for the user
1. Working name. Pick or suggest one, then check trademarks and stores.
2. First languages after RO. Proposal: TR, PL, PT-BR, DE (mix of underserved and good-eCPM markets) plus EN as a baseline.
3. Which account or entity publishes (Play/Apple/portals, AdMob payouts), and who signs native-reviewer contracts.
4. Art direction: proposal is **calm and clean** (soft paper texture, one accent color per theme pack, large readable letters).
