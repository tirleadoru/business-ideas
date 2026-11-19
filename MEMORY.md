# Business Ideas — Shared Memory

This is the running log of everything discussed in this repo: who we're building for, the constraints, the ideas, the analysis and the decisions. **Claude keeps this file updated after every meaningful discussion.** Newest decisions go in the Decision Log at the bottom.

_Last updated: 2026-11-19_

---

## 1. Goal & constraints

- **Goal:** build products that bring in income with low ongoing effort. Target: about 1 week/month of maintenance, instead of the current ~20h/day work. This isn't about retiring. It's about freedom: being able to take a day or a week off without anything breaking or stopping.
- **Skills:** full web + mobile development (any stack).
- **Time:** will commit fully as soon as there's a specific plan with a credible path to success.
- **Budget:** ideally time only. Small upfront costs are OK. **No ongoing costs that scale with usage** (e.g. paid LLM API calls per user). Running costs must stay flat or close to zero as users grow.
- **Market:** no fixed preference for B2B vs B2C. Leaning B2C because there are more people than businesses, if we can find something catchy.
- **Market reach:** **global by default**, for both B2B and B2C. No single-country products. Translations are considered solved.
- **Monetization rule:** free offerings are fine, as a free tier, a freemium funnel or ad-supported, **but every product must have a clear, built-in way to make money.** No pure "free things for nothing".
- **Values:** dislikes pay-to-win mobile game models. Fine with people spending lots of *time* in a product.

## 2. Guiding principles (Claude's analysis)

1. **Distribution is the real problem, not building.** Prefer products where customers come through channels we don't pay for: SEO, marketplaces/app stores, game portals.
2. **Marginal cost ≈ 0.** Static hosting, client-side search, no per-request paid APIs.
3. **Low support surface.** No uptime-critical promises, minimal sensitive data, self-serve.
4. **Assets that compound.** Content/SEO pages and app store presence keep growing over time. Paid ads stop the moment you stop paying.
5. **B2C vs B2B is about willingness to pay, not headcount.**
   - B2C: huge volume but low conversion → monetize with ads, affiliate links, one-time purchases.
   - B2B: small volume but pays monthly and churns less (100 shops × $30 = $3k/month).
   - Hybrid that works well: B2C traffic via SEO, monetized with ads + affiliates + an optional pro tier.

## 3. Research notes

### Flappy Bird (verified 2026-11-19)
- Dong Nguyen pulled Flappy Bird in Feb 2014 at the height of its success, citing its addictiveness. Widely reported at ~$50k/day in ad revenue.
- **Correction to an assumption:** the *genre* was never banned. In Feb 2014 Apple and Google rejected clones with **"Flappy" in the name**: Apple because it "leveraged a popular app", Google treating it as keyword spam. Clones without the name (e.g. "Splashy Fish", "Ironpants") hit #1/#2 in the charts. Lesson: simple one-tap games are allowed. Copycat names and assets aren't.
- 2024–2025: the "Flappy Bird Foundation" (Gametech Holdings) took over the abandoned trademark and relaunched it (web first, then mobile in 2025, with crypto/Solana ties at first). Nguyen publicly said he's not involved.
- Takeaway: Flappy Bird's success was viral luck. The game being simple made it *possible*, but simplicity didn't *cause* the success.

### Car warning lights app/site (researched 2026-11-19) — verdict: ❌ as a standalone product
- **Crowded market:**
  - Generic guides from KBB, Haynes, Halfords, Auto Express and CarGurus dominate Google.
  - By-make/model/year databases already exist (warninglights.co, built by its community; dashboardsymbols.com).
  - Dozens of app store apps (generic, plus paid per-brand ones like Ford/Nissan/Toyota/BMW at about $1.99). Most have few ratings. The biggest Google Play one has about 316 ratings and about 150 installs/month, so demand for a *dedicated app* is low.
- **Free built-in competition:** iOS 17+ Visual Look Up identifies dash symbols from a photo, and Google Lens does it on Android.
- **Symbols are mostly standardized** (ISO 2575:2021 + Amd 1:2024), so generic content is a commodity. Only some symbols are make-specific.
- **Weak business shape:** people look it up once, in a stressful moment, then leave. That means low value per visit and no recurring use.
- **Data/legal:** manual *text* is copyrighted; facts aren't. We'd have to rewrite everything, and manually verifying thousands of model/year variants risks accuracy.
- Possible angles left: a non-English market with weak competition, or bundling it into a wider "car problem → can I drive? → likely cost" tool.

### Principle learned: accuracy should come from the source
- The user's concern: a knowledge product with wrong information is dead.
- So for idea A, prefer domains where **authoritative, structured, public data already exists** (government/open datasets, official APIs). Accuracy then comes from the source, not from us writing thousands of facts by hand. Our value is in organizing, searching and presenting it.

### Global + multilingual strategy (2026-11-19)
- **Global ≠ English-only.** English is where competition is fiercest. The edge is launching **multilingual from day one**. Non-English versions of the same tool face weak competition and rank much faster. English is the hardest market, not the default.
- **Translate at build time, not runtime.** Translate content and UI once with AI tools during development and store it as static content, so there's no per-user cost. This fits the budget constraint.
- **Caveats:**
  - Have safety- or money-critical text reviewed (a native speaker for the top languages, or a source dataset that's already multilingual).
  - Google penalizes mass auto-generated low-value pages ("scaled content abuse"). Every page must solve a real problem, not just exist in another language.
  - Selling globally means VAT/sales tax in many countries. Use a **Merchant of Record** (Paddle, Lemon Squeezy) or app store billing, which handles tax for you.
  - Proper multilingual SEO: hreflang tags, a localized URL for each language, translated slugs and metadata.

## 4. Idea pipeline

Status: 💡 idea · 🔍 validating · 🛠 building · 🚀 live · ❌ dropped

### ⭐ Top 5 from research round 1 (2026-11-19)
Filters: global + multilingual, no per-user cost, accuracy from authoritative sources, low maintenance.

| # | Idea | Model | Time to first $ | Competition | Data accuracy | Passiveness |
|---|------|-------|-----------------|-------------|---------------|-------------|
| 1 | **Global recall monitor for e-commerce sellers** (Shopify → WooCommerce/Etsy) | B2B subscription | Fast (app store traffic) | Medium: several new GPSR apps in 2026, mostly 0 reviews | High (official feeds) | High |
| 2 | **Used-car "check before you buy" hub** (recalls + known issues by model/year, multilingual) | B2C SEO + affiliate (carVertical etc.) + ads | Slow (SEO 6–12 months) | Medium: carcomplaints.com is US/English; weak multilingual | High for recalls; complaints are raw user data | Very high once it ranks |
| 3 | **Casual HTML5 game** → web portals (Poki/CrazyGames) → mobile | Ad revenue share | Medium | Hit-driven | n/a | High if it hits |
| 4 | **Consumer "is anything I own recalled?" alerts app** | B2C freemium / ads | Slow | Low for global multilingual | High | High |
| 5 | **Medicine names abroad translator** | B2C ads/affiliate | Slow | Medium: Pillintrip, Drugs.com, Convert Drugs apps | Risky (brand ≠ same drug across countries) | Medium, with liability ⚠️ |

**Key insight:** #1, #2 and #4 share one **"global recall data engine"**:
- It ingests official feeds: EU Safety Gate (weekly XML), US CPSC (API), NHTSA, FDA, Health Canada, UK OPSS/DVSA, Australia ACCC, Japan, Korea, Brazil and more.
- It normalizes and translates them once, at build time.
- One engine, three products: B2B app (fast revenue) + B2C SEO site + alerts app (compounding traffic).

**Recommended plan:** build the engine, launch #1 first (fastest path to paying users), then put #2/#4 on the same data. #3 is an optional weekend side bet.

#### Research details
- **#1 Recall monitor:**
  - **Regulation:** the EU GPSR (Reg. 2023/988, applies since Dec 2024) requires online marketplaces to register with Safety Gate and check it, notify buyers of recalls and publish recall info. This creates sustained compliance pain for EU-selling merchants.
  - **Shopify competitors:**
    - Conformica GPSR (Safety Gate nightly scan + email, launched June 2026);
    - Alnage GPSR (Safety Gate matching, launched Aug 2026);
    - Recall Watch (general recalls by barcode/brand/model);
    - many label-only GPSR apps (Vellona, ComplyDock, Kedalion, GPSR Shield, SafetyMark).
    - Mostly 0 reviews, so the market is early and unproven.
  - **Our edge:** global coverage (EU + US + UK + CA + AU + Asia) for merchants selling worldwide, plus multi-platform support.
  - **To verify:** competitor pricing, whether merchants actually pay for this (read reviews and forums), and the exact GPSR duties for small sellers vs marketplaces.
  - **Data:** ProductGuru offers a free CC-BY-4.0 API over about 32 authorities (licence to verify). Several Apify scrapers exist. The data is easy to get, so the moat is the product/UX, not the data.
- **#2 Car hub:**
  - **Data:** NHTSA recalls/complaints are public domain with an API, but cover US models. UK MOT history API needs an application (DVSA withdrew open failure-rate data in 2017).
  - **Monetization:** carVertical affiliate: from €4/sale, no cap, 90-day cookie (Awin lists 30 days), many countries.
  - **Risk:** EU-only models are poorly covered by US data. National recall databases (e.g. Germany's KBA) still need checking.
- **#3 Web games:** Poki is reportedly 50/50 on portal traffic and 100% on your own traffic, with exclusivity deals possible. CrazyGames' split is unclear (50–60% quoted). A decent casual game typically earns about $200–2,000/month, and top games far more. These figures come from third-party guides, not official terms.
- **#5 Medicine abroad:** existing tools are Pillintrip, Drugs.com International, and the Convert Drugs / World Drugs apps. Brand names don't map one-to-one across countries, so there's real safety liability.

#### Validation of #1 (2026-11-19) → ❌ DROPPED
- **The user checked the Shopify listings:**
  - Conformica is free with everything included;
  - others are freemium, with paid tiers for more languages/products;
  - Recall Watch is paid from the start;
  - all have 0 reviews.
- **Follow-up search:** 15+ GPSR apps (GPSReady $7.99/mo, Tracewell $14.99/mo, GPSR Shield free/$9.99, Kedalion, Complyo, GPSR Kit, GPSR Suite, EUReady, PriceProof…), **essentially all with 0 reviews**.
- **Interpretation:**
  - There are too many apps and too little demand.
  - Merchants' real GPSR pain is labelling (EU responsible person, manufacturer info), not recall monitoring. They solve labelling with free metafields or a paid responsible-person service.
  - Recall monitoring isn't clearly mandatory for small sellers. The obligations sit mainly on marketplaces (Amazon/Etsy), which build it themselves.
  - A free competitor sets the price at $0.
- **LESSON → new validation rule:** an empty or zero-review market is a **red flag**, not an opportunity. Prefer **proven demand + beatable incumbents**: competitors with many reviews/users but bad recent ratings, price hikes, missing features or abandoned updates. That's the signal people already pay and want better.
- This also weakens #4 (consumer recall alerts) somewhat. #2 (car hub) is unaffected because it relies on consumer search demand, which still needs keyword validation.

### ⭐⭐ Research round 2: "proven demand + beatable incumbent" scan (2026-11-19)
Four marketplaces scanned in parallel. Figures come from live listings/APIs on 2026-11-18/19 unless marked unverified.

**Combined ranking (Claude's synthesis):**

| Rank | Opportunity | Market | Demand proof | Weak incumbent | Build | Who handles billing | Score |
|------|-------------|--------|--------------|----------------|-------|---------------------|-------|
| 1 | **Flat-price digital downloads app** (no sales caps, no bandwidth fees; files on Cloudflare R2, which doesn't charge for downloads) | Shopify | SendOwl $39–159/mo; Sky Pilot 445 reviews | SendOwl 3.4★ ("$15 → $175"); Sky Pilot bills $1–2/GB bandwidth | 4–6 wks | Shopify Billing (built in) | 8 |
| 2 | **ModHeader replacement** (HTTP header modifier, local-only, open source) | Chrome | ModHeader had 900K users + a paid Pro tier | Removed as malware 2026-07-10; Requestly (300K) needs an account | 3–5 wks | ExtensionPay / Paddle | 8 (window closing; clones arriving) |
| 3 | **Google Docs heading numbering + table of contents** | Google Workspace | 4M+ users | LumApps TOC 3.4★, broke around June 2026; alternatives tiny/buggy | 3–5 wks | DIY (Stripe) | 7.5 (users expect free) |
| 4 | **Confluence Mermaid/Markdown macro** (Forge) | Atlassian | ~18K installs across apps; paid peers $0.23–0.50/user | 2.8–3.5★ ("tiny and blurry") | 3–5 wks | Atlassian (per user) | 7.5 |
| 5 | **Lightweight broken-link checker** (runs locally on the customer's server) | WordPress | 500K + 200K installs | WPMU DEV 3.8★ ("database crashed", false positives, pushes users to its cloud) | 6–8 wks | DIY (Freemius/Paddle) | 7.5 |
| 6 | Flat-price size charts | Shopify | Kiwi 1,242 reviews | Surprise usage fees ("$25 → $145") | 3–5 wks | Shopify | 7 |
| 7 | Social share buttons (no JS, no tracking) | WordPress | Sassy (~100K, closed Nov 2026) | Social Warfare stale | 3–5 wks | DIY | 7 (low price ceiling) |
| 8 | Dev toolkit: JSON viewer + cookie editor | Chrome | 2M + 2M users | JSON Formatter 1.5★ (adware); EditThisCookie removed | 2–4 wks each | ExtensionPay | 7 |

**Also found (lower score):**
- Shopify: Zapiet pickup/delivery scheduling (7; checkout edge cases); Uploadery file upload (6.5); Stocky replacement (5.5, crowded); Sufio invoices (5).
- Atlassian: Labs Jira gadgets (6.5); Recurring Tasks for Jira (5).
- Google: Calendar→Sheets export (6.5); Autocrat replacement (5).
- WordPress: YITH quote/badges for WooCommerce (7); migration plugin (6); analytics (5); thumbnail regeneration (5).
- Chrome: Wappalyzer-like (6); SEO toolbar (5.5); screenshot/recorder (4–4.5).

**Useful context:**
- Atlassian Connect reaches end of support on 2027-01-31, and Data Center end of life is 2029-03-28. Many old apps won't migrate, which creates openings.
- Forge has charged above a free tier since Jan 2026. Apps that work in the browser stay at ~$0.
- Neither the Chrome Web Store nor Google Workspace handles payments. Use ExtensionPay or Paddle/Lemon Squeezy (merchant of record).
- Shopify and Atlassian bill for you, which is a big plus for passiveness.
- Shopify roll-up owners (e.g. Shop Circle) buy apps and may degrade them later. Re-scan quarterly.

**Claude's recommendation:** #1 (Shopify digital downloads) as the main bet: highest willingness to pay, platform billing, a clear "flat price" wedge, near-zero infra. #2 (ModHeader replacement) as a fast first ship if we move within weeks.
**Must verify before building #1:**
- Shopify's own free "Digital Downloads" app and its limits;
- other competitors (e.g. Filemonk, FetchApp; unverified) and their ratings/prices;
- R2 storage cost per merchant;
- abuse risk (piracy/file hosting).

### Research round 3: whole-category checks (2026-11-19)

| Candidate | Score | Key finding |
|---|---|---|
| **WP local broken-link checker** | **6/10** | Only 2 dedicated plugins with meaningful installs (500K + 200K), **both 3.8★**, both moved to cloud/SaaS ("credit card required", "database crashed"). No well-rated alternative ≥10K installs. Against: users expect free, slow ranking, SEO suites absorbing the feature. Est. **$5–15K/yr in year 2**, more with agency/multisite tiers. Pro pricing $49–79/yr per site; Freemius for licensing. |
| Confluence Mermaid/Markdown | 4/10 | 105 "mermaid" apps, ~20 new (mostly AI-built) clones in 2025–26. Atlassian's own free Labs viewer is actively updated. Prices $0.23–0.50/user. Wedge: "paste AI/Git Markdown with Mermaid → it just works" (crisp SVG, zoom, dark mode); orphaned Render Markdown (3.8K installs, Connect, last updated 2021). Forge revenue share: 0% until $1M lifetime. Est. $1–2.5K/mo after 12–18 months. |
| Shopify size charts | 3/10 | MP Size Chart **5.0★/877** with a free recommender; SmartSize $12 unlimited / $19 recommender; ESC $4.99 unlimited; themes can do basic charts natively. Only niche left: a vertical recommender (shoes/bras across EU/US/UK/JP sizes). |
| Shopify pickup/delivery | 3/10 | 6+ BFS apps at 4.8–5.0★ for $6–20; one8 (launched Dec 2025) $5.99 with 200 free orders. Checkout extensions are Plus-only, so widgets depend on the theme and are fragile, meaning heavy support with seasonal peaks. Shopify could add it natively. |

**Big-picture insight (Claude):**
- In 2026 building software is cheap for *everyone*. AI-built clones flood every marketplace utility category within months (seen in GPSR, Mermaid, ModHeader).
- **Pure "better utility" plays are commoditizing.** Durable advantages now come from:
  - **distribution** (an audience, SEO, partnerships);
  - **domain knowledge / access** (an industry you know from the inside);
  - **proprietary data or network effects**;
  - **trust/brand in a niche**.
- So the next search should start from the **user's unfair advantages** (day-job industry problems, client base, hobbies, communities), not from scanning marketplaces.
- The **WP broken-link checker is a reasonable low-risk "first ship"** to learn the full loop (build → launch → reviews → revenue) in about 6 weeks, without expecting it to replace the income.

#### Deep check of #1, Shopify digital downloads (2026-11-19) → ⬇️ DOWNGRADED (score 8 → 3)
- **Shopify's own "Digital Products" app:** FREE, 4.8★, **1,489 reviews**. Covers files/links, download limits, email delivery, 21 languages. Gaps: no bulk upload, files can't be reused across variants, and a recent "accidental file deletion" incident.
- **Filemonk (Artos):** 4.9★, 511 reviews, Built for Shopify.
  - Free up to 50 orders/mo; **$10/mo for unlimited orders**; **$25/mo for unlimited storage**.
  - Includes license keys, PDF watermarking and fraud checks.
  - **The "flat price, no limits" angle is already taken.**
- **Sky Pilot:** 4.9★, 445 reviews. Free / $9 / $24.99 / $54.99, with bandwidth overage of $1–2/GB. Its few 1–2★ reviews cite confusing setup, emails landing in spam, and fraud/fake accounts.
- **SendOwl:** the price-hike complaints are mostly from **spring 2025**, so displaced users have had about 18 months to switch (named: "Easy Digital Products", "a flat $29 service").
- **Conclusion:**
  - One incumbent is bad, but the category is well served by free and cheap, highly rated apps.
  - The only remaining wedge is heavy video sellers who hit Sky Pilot's bandwidth overage. That's too narrow.
- **Useful facts kept:**
  - Shopify revenue share is **0% on the first $1M lifetime app revenue** (counted from 2025-01-01), then 15%, plus a 2.9% processing fee.
  - Cloudflare R2: $0.015/GB-month storage, free egress, free tier of 10 GB.
- **User's counterpoint (2026-11-19), agreed with nuance:** a market with free/cheap options is **not automatically off the list**. The world is big, a crowded market proves demand, and a copy plus "something extra" can still win customers.
  - **Claude's caveat:** in app marketplaces, ranking is driven by reviews and installs, so it's winner-takes-most. A new app with 0 reviews sinks (see the 15+ GPSR apps with 0 reviews). A crowded market is viable only with a **sharp wedge**:
    - an **underserved segment** (a vertical, country/language, store size);
    - a **missing feature** users keep requesting in reviews;
    - **distribution** the incumbents don't use (SEO, content, communities, partnerships, other platforms).
  - We also need a concrete plan to get the first 20–50 reviews.
  - So crowded markets are scored on "how sharp is our wedge", not dropped. Shopify digital downloads stays in the pipeline at a low score unless a wedge appears (e.g. bulk upload / file reuse across variants, which Shopify's free app lacks; video sellers; a niche vertical).
- **LESSON → refined rule:** "beatable incumbent" must hold for the **whole category**, not one app. Check the top 5 apps in the category, including the platform's own free app, before scoring.

#### Validation of #2, ModHeader replacement (2026-11-19) → ⬇️ DOWNGRADED (score 8 → 4)
- **The user's check:** many ModHeader-style extensions already exist on Chrome, and they're all free.
- **What ModHeader actually charged (third-party sources, unverified on the official page):**
  - Pro was about $4/mo, ~$2/mo billed yearly, or $60 one-time.
  - Pro gave unlimited rules/profiles, team/organization sharing, a bundled sister extension (ModResponse) and no ads.
  - The free tier was **ad-sponsored**. That ad pressure is likely what pushed it into shady data collection.
- **Requestly** earns from **team plans** (~$10/user/mo, billed yearly): collaboration, access control, audit logs, API client/mocks. That's a broad dev platform with servers, not a simple header tool.
- **Freemium extension conversion rates (self-reported anecdotes):** 0.5–3% overall free → paid. Example: 10K users → ~150 paying.
- **The math:** $2K/mo at $4/mo needs ~500 payers, which means about 20K–100K active users. Free clones already compete for the same users.
- **LESSON:**
  - Single-user, local-only browser tools are commodities. People don't pay for them, which is why owners drift to ads/adware.
  - People pay for **team/sync/collaboration**, and that needs servers and support.
  - So prefer markets where **paying is the norm**: platform billing plus incumbents already charging monthly, like the Shopify ecosystem.
- The same logic weakens #3 (Google Docs numbering, users expect free) and #8 (JSON/cookie dev toolkit).

#### Researched and rejected (round 1)
- Car warning lights: saturated, and iOS/Google Lens do it free (see §3).
- PTO/vacation-day optimizer: many free tools already (Holiday Optimizer, toools.cloud, rapidtoolset, holidaydb bridge-days API).
- E-number vegan/halal checker: the answer is often "depends on source" (e.g. E471), so a confident answer isn't possible. Accuracy problem.
- Cosmetic ingredient decoder (INCI): crowded (INCIDecoder, Yuka, EWG Skin Deep, SkinSort, Think Dirty).
- Recall data API sold on its own: a dozen Apify actors + a free CC-BY aggregator already exist.

### A. Non-AI "knowledge engine" in a niche (user's idea) — 💡 ⭐ Claude's top pick
- **Concept:** we (the user + Claude during development) build a large, curated, structured database for one domain. Users get a chat-like UI that answers questions with classic search + rules, **no LLM at runtime**, so per-user cost is zero.
- **Feasible without AI? Yes.** Pre-LLM stack:
  - Full-text search with BM25 ranking, typo tolerance, synonyms: **Meilisearch / Typesense** (self-hosted, cheap) or fully **client-side** (MiniSearch / Orama / Lunr) for static hosting.
  - Intent matching: a curated question→answer bank with many phrasings per answer + synonym dictionaries + keyword rules.
  - Guided flows: decision trees ("What symptom? → When does it happen? → …") for diagnosis-type domains.
  - Templated answers built from structured fields (e.g. "{part} for {car} costs about {price}").
  - Optional middle ground: a small embedding model running **in the user's browser** (transformers.js). Semantic search with zero server cost.
- **The key multiplier:** the same database generates thousands of static SEO pages (one per question/entity). **Google brings the traffic; the chat is the UX on top.** This is programmatic SEO + a search tool in one.
- **Monetization:** display ads, affiliate links (products, parts, services), lead-gen, a paid "pro" tier/app.
- **What makes a good domain:** many repetitive questions, info that's stable over time, structured data, high search volume, a natural affiliate/commercial angle, low liability.
- **Candidate domains (to evaluate):**
  - Car OBD-II fault codes + symptoms per make/model → affiliate links to parts/tools.
  - Cooking substitutions/conversions ("what can I use instead of buttermilk").
  - Plant care / pest identification by species.
  - Country-specific bureaucracy (visas, residency, freelancer tax rules) → affiliate links to services. Needs updating when rules change.
  - Hobby/game databases (builds, items, recipes for popular games).
- **Risks:** SEO takes 6–12 months to ramp; Google's AI answers reduce clicks for simple facts (so favour interactive/diagnostic value over plain facts); content accuracy.

### B. Simple, catchy casual game — 💡 lottery ticket, cheap to buy
- **Reality check:**
  - Hyper-casual is a hit-driven business and most prototypes fail.
  - Ad revenue per user fell after Apple's tracking changes (2021). The market shifted to "hybrid-casual": simple core + light progression + rewarded ads + an IAP to remove ads.
  - Organic virality like Flappy Bird is rare. Mobile normally needs paid user acquisition.
- **Zero-budget routes to distribution:**
  1. **Web game portals (Poki, CrazyGames):** HTML5 games, the portal brings players and shares ad revenue. No user acquisition cost. Web stack = user's strength.
  2. **Hyper-casual publishers (Voodoo, SayGames, Homa, CrazyLabs):** submit prototypes. They pay for marketing tests (cost per install) and publish the winners on revenue share.
  3. Same codebase → mobile later (Capacitor / native wrapper) once a game proves itself.
- **Monetization (fair, not pay-to-win):** rewarded ads, a "remove ads" purchase, cosmetics.
- **Why not pay-to-win/strategy:** huge content + live-ops + multi-million user acquisition budgets. The opposite of passive, and against the user's values.
- **Strategy:** build many tiny prototypes fast (1–2 weeks each) and let data pick the winner.

### C. Marketplace B2B apps (Shopify / Chrome / Figma / Notion) — 💡
- The marketplace provides discovery. Mine 1-star reviews of existing apps for gaps. Recurring revenue, low churn.

### D. Others from first brainstorm — 💡 parked
- Developer APIs (usage-based), digital products (templates/boilerplates), buying an existing small SaaS (Acquire.com).
- AI wrapper — ❌ for now (per-usage costs violate the budget constraint).

### 🎮 Games deep-dive (2026-11-19)

**User context:**
- No repeatable domain edge from client work: presentation sites across retail/real estate/healthcare/logistics, one-off WooCommerce customizations, and recently Drupal, where clients refuse to pay for add-ons.
- **The user's strategy:** build things that live on someone else's store/platform at no ongoing cost to us, then leave them. Some will get traction.
  - Claude agrees: a **portfolio of small bets**.
  - Each one must be low-maintenance and have built-in monetization.
  - "Forget" really means occasional updates for platform changes.
  - Games on portals are closest to fire-and-forget.

**How web portals pay (researched):**
- **CrazyGames:**
  - Scale: ~300M gameplays/month, ~35M users.
  - Money: ad revenue share; CrazyGames doesn't publish its standard split. Their 2026 jam terms gave devs 60% of ads and 70% of in-game purchases.
  - Per-play value: community estimate ~**$1 per 1,000 plays** (varies hugely by country, genre and session length).
  - Payouts: monthly via Tipalti, €100 minimum.
  - SDK support from 50K plays.
  - **In-game purchases:** invite-only, via the **Xsolla** SDK. Signed-in users only (`CrazyGames.SDK.user.getXsollaUserToken()` → Xsolla catalog purchase).
- **Poki:** ~50/50 on portal traffic, 100% on your own traffic. **No in-app purchases allowed**, only Poki's ads (commercial breaks + rewarded). Curated, and rejects many games.
- **Rough math:**
  - 1M plays ≈ $1K gross → $500–600 for us.
  - A game with tens of millions of plays ≈ tens of thousands of dollars total.
  - Typical decent casual game: $200–2K/month.
- **Mobile later:** wrap the same code (Capacitor), with AdMob ads + store IAP (Apple/Google take 15–30%).
- HTML5 IAP outside the portals: Xsolla, or Stripe on our own site.

**Why Flappy Bird exploded:**
- Instantly understood; one input; 2–5 second rounds; instant restart; brutal difficulty turned frustration into "one more try"; scores worth bragging about.
- Then YouTube reaction videos and a chart feedback loop in 2014.
- The ~$50K/day came from tens of millions of daily players × banner ads. That virality is luck and can't be designed. We can only design the *ingredients*.

**"Catchy game" ingredients (research + design consensus):**
1. Understood in 3 seconds.
2. One-touch or simple input.
3. Short sessions with instant restart.
4. Near-misses and "one more try".
5. **Numbers going up**: upgrades, visible progression (the incremental loop).
6. **"Oddly satisfying"** sensory feedback: clearing, cleaning, cutting, ASMR sounds, particles. An Oxford/FuturLab study found 72% of PowerWash Simulator players had a mood lift.
7. Flow: clear goal + immediate feedback.
8. Shareable moments.
9. Ads that are true to the gameplay keep players better: 32% day-1 retention vs 14% for fake-ad games.

**The user's 3 game ideas, assessed:**
1. **"The fake ad, but the real game"**, e.g. *Stone Grass: Mowing Simulator* (FreePlay LLC):
   - CrazyGames rating 9.1, **420K likes**, released Apr 2025, also on iOS/Android.
   - Loop: mow → storage fills → sell → upgrade speed/power/capacity → unlock zones.
   - The trend is real: a Steam compilation of the real games behind fake ads exists, and "Hero Rescue" became the real pin-pull game.
   - ⭐ **Strongest idea.** Proven demand, hybrid-casual sweet spot, fits rewarded ads (2× income, auto-mower, etc.).
   - Pick a *different* satisfying activity, not mowing (Stone Grass owns that). Options: snow plowing, power washing, rust/sand blasting, leaf blowing, carpet cleaning, excavation/digging, ice resurfacing.
   - Needs 3D (three.js/Babylon.js/PlayCanvas, or Godot/Unity web export).
2. **Vertical "falling" game:**
   - The user's memory is probably **Nohzdyve**, the game-within-the-film in *Black Mirror: Bandersnatch*: falling down a skyscraper dodging objects. Netflix released a playable version. We can't reuse its name or look, but the mechanic is generic.
   - The genre exists: Helix Jump (Voodoo, 2018, **~800M downloads**, falling through a tower), Downwell (an acclaimed roguelike), FallDown! 2, many itch.io titles.
   - Viable only with a strong twist (e.g. a progression/upgrade layer, a collection meta-game, a physics gimmick).
   - Medium potential; cheap to build in 2D (Phaser).
3. **Turn-based artillery duel** (Scorched Earth / Pocket Tanks / Worms / *Tank Stars* (Playstack→Azur), Bowmasters):
   - Proven, evergreen genre, and Tank Stars still earns thousands per week per region.
   - On the web, mostly small or old clones were found (portal popularity unverified).
   - Zero-cost formula: **vs AI + local 2-player on the same device** (portals love "2 player" games). Real-time online multiplayer needs servers, so skip it at first.
   - Monetization: unlock weapons/tanks, rewarded ads for special shots, cosmetics.
   - Strong candidate, 2D (Phaser + destructible terrain).

**Claude's recommendation:**
- Run games as a portfolio: ship 2–3 small games fast and let portal data pick the winner.
- Order: **#1 satisfying-upgrade 3D game** (highest proven demand) or **#3 artillery** (2D, cheaper, evergreen), then #2.
- Engines: Phaser for 2D; three.js/Babylon for 3D (or Godot web export).

### 🎮 Games round 2: the user's findings (2026-11-19)
**The user's passion pick is the Nohzdyve-style falling game.** They have wanted to make it since seeing Bandersnatch. Their 2027 focus is building income so they can stop working 20h/day and spend more time with family.

**Downwell (paid, ~$3, 100K+ Android downloads):**
- The user's math was 100K × $3 = $300K. Reality check:
  - "100K+" on Google Play means 100K–499K installs.
  - Many copies sell at sale prices.
  - Google keeps 15% (30% above $1M).
  - Devolver (the publisher) takes its share before the developer gets anything.
- Net to the developer from Android is likely well under half of $300K. It's still a real success.
- But Downwell was an award-winning Steam/console hit first. Unknown paid mobile games rarely sell, because nobody pays $3 blind.
- → **Lesson:** for an unknown developer, use **free + ads + a one-time "remove ads / premium" purchase**. A paid version on Steam can come later if the game earns fans.

**The word-search YouTuber (10M downloads, AdMob):**
- Claimed numbers: ~$34K gross in one month, then about $24K after invalid-traffic deductions and US tax withholding, then about $18K after $6K of paid user acquisition (UA).
- Caveats:
  - Survivorship bias.
  - These videos also make money from the audience: sponsor-like tool promotion (Abacus AI), a Discord.
  - None of the numbers are verified.
- Real lessons:
  1. **Evergreen "boring" genres have huge search demand** (word search, sudoku, solitaire, mahjong, nonograms). Players are often older, with lots of US traffic, so ads pay well (high eCPM) and sessions are long.
  2. **Store keywords (ASO) are the marketing**: the title, short and long descriptions, and screenshots.
  3. **Monetization = rewarded ads (hints) + interstitials, and nothing else.** Too many ads causes uninstalls.
  4. **Paid UA is a lever for later**, used only when data shows a player earns more than they cost to acquire (LTV > CPI). Fund it from revenue, never savings, so the no-usage-cost rule still holds.
  5. **Google Play rules:** a one-time $25 developer account. New *personal* accounts must run a closed test with **12 testers for 14 days** before production; organization accounts don't need to. Apple costs $99/yr.
  6. Tax: AdMob withholds US tax on US-sourced revenue. A W-8BEN can lower it if the user's country has a tax treaty with the US (verify).
- **Our angle on evergreen puzzles: languages.** English word search is crowded, but word search, crosswords and word games in Romanian, Polish, Turkish, Indonesian, Portuguese and so on are far less served. Word lists are free and public (open dictionaries, Hunspell). One engine can ship in 20–30 languages, which fits the user's global/multilingual principle.

**Updated games plan (Claude's proposal):**
1. **Game 1: the falling game** (the user's passion). 2D in Phaser, a 4–6 week build.
   - Ship to the web portals (CrazyGames/Poki) first: free traffic and real retention data.
   - Then wrap it with Capacitor for Android/iOS, with AdMob plus a "remove ads" purchase.
   - The twist to design: a progression/collection layer between runs.
2. **Game 2: a multilingual word-search/word-puzzle engine** for the mobile stores. AdMob-heavy, driven by store keywords, one build per language or one app with many languages.
3. **Game 3: the satisfying-upgrade 3D game or the artillery duel**, chosen after the data from games 1 and 2.

### 🔤 Word-game deep-dive (2026-11-19)
**com.wordfight** is actually **Word Rush: Race with friends** (*Kelime Savaşı*, by Vuvy Teknoloji, Istanbul). It's a real-time 1v1 category game where you type answers.
- 5M+ downloads; 2.4★ on the US listing, 1.8★ on the Turkish one.
- AppGoblin estimates only **<$10K/month** (unverified). That's because it's Turkish traffic, where ad rates are low. **Many downloads does not mean much money.**
- 1★ reasons:
  - Crashes on launch.
  - Too many ads.
  - An energy system (about 3 matches, then you wait).
  - Correct answers rejected.
  - Suspected bots.
- Real demand, served badly.

**Subgenres (Google Play, today):**
- **Crossword-connect** is the money subgenre: Words of Wonders 100M+ / 4.9, Wordscapes 100M+, CodyCross 100M+, Word Cookies 50M+, Zen Word.
- Word Stacks: 10M+.
- Duels: Words With Friends, Wordfeud, Kelimelik (Turkey 10M+).
- **Word search leads downloads in Brazil and Poland** (PlaySimple).
- US weekly revenue (Sensor Tower): NYT about $575–765K on iOS, Wordscapes about $517K at peak, Zen Word about $150K.

**Localization:**
- Words of Wonders is already in **about 36 languages** → being multilingual is necessary but **not a moat**.
- Wordscapes has only 5 languages; Wordfeud has 10.
- Wordle clones exist in 149 languages; Portugal's Termo reached 200K daily players in 3 weeks.
- Romania's top 5 word games are all foreign and small.
- In-app purchase revenue in lower-income (Tier-3) markets is tiny (Turkey's No. 1 earns about $966/week), so **ads are the business there**.

**Most common 1★ complaints (our design brief):**
- An ad after every level; unclosable or loud ads.
- Paid "remove ads", then the ads came back.
- Rigged events or races, bots, pay-to-win.
- Valid words rejected.
- Pop-up and notification bloat.
- Crashes; energy limits.

**Word lists:**
- hermitdave FrequencyWords (CC-BY-SA-4.0, attribution; share-alike scope unclear, so get advice).
- Hunspell dictionaries: license varies per language.
- Wiktionary/kaikki: CC BY-SA.
- ENABLE (English): public domain.
- ⚠️ Official Scrabble lists (NASPA/Collins) need a license.

**AdMob eCPM:**
- Tier 1: rewarded $15–30, interstitial $5–8.
- Brazil and India: $0.3–3.
- 4–10× spread by region; Q4 is 20–40% higher than Q1.

**Concepts:**
1. ⭐ **Multilingual crossword-connect, offline, "the fair one".**
   - Ads: an interstitial only every 3–4 levels, all ads closable, "remove ads" that really works.
   - No fake races; a "suggest a word" button.
   - Native-quality, culture-themed levels per language.
   - Includes a **daily puzzle mode** for retention.
2. Daily Wordle + endless mode in 30 languages (cheap, saturated) → built in as a mode of #1, not a separate product.
3. Fair async word/category duel for underserved languages (Turkish, Romanian, Polish): no energy system, honestly labelled AI opponents. Needs a free-tier backend (Firebase/Supabase), so there's a cost risk at scale → later.

**Claude's recommendation:**
- Build #1 (with #2 as a mode).
- Language mix: high-paying non-English (German, French, Dutch, Nordic, Japanese?) plus underserved (Romanian, Polish, Turkish, Portuguese). English last, or as a bonus.
- The user is a native Romanian speaker, so use Romanian as the quality-test language.

### 💼 Ideas from an entrepreneur video (likely Chris Koerner; added 2026-11-19)
Scored against *our* goals (low-touch, global, ~1 week/month of upkeep, no usage costs), not against "can it make money at all".
1. **AI voice receptionist for local trades** (the "gutter cleaner who misses a 10pm call" example). **3/10 for us.**
   - Demand is real, but the market is crowded and cheap: Smith.ai from $150/mo, Goodcall $79, Rosie and Marlie $49, all self-serve.
   - The pitch of "$3K setup + monthly fee" is hard now that owners can sign up for $49.
   - It's an **agency/sales business**: cold-selling local firms, plus support when the AI books a job wrong. It also has per-minute voice/LLM costs, passed to the client but still a usage cost.
   - That's the opposite of "forget about it". Kernel worth keeping: *missed calls = lost money*. (A non-AI "missed-call text-back" tool also exists, e.g. inside GoHighLevel.)
2. **Niche directories / maps** ("all dog parks in Seattle" → ads → paid priority listings). **5/10, worth a niche hunt.**
   - Fits our model: data + SEO + multilingual + ads, later paid listings. Same family as idea A (a curated database).
   - Risks:
     - Google Maps already lists the basics, so we must hold **attributes Google lacks** (off-leash? fenced? water? shade? surface?).
     - AI Overviews are cutting informational clicks. Local/transactional queries seem less affected (vendor data, directional).
     - Ad income is slow until traffic exists.
     - Selling priority listings is sales work.
   - Make it global and multilingual: one engine, many cities and countries, using open data (OpenStreetMap) as the base.
3. **Vending machines.** **1/10 for us.**
   - Physical, local, restocking, breakdowns, location deals.
   - Fine as a hands-on local business, but it breaks the global/low-touch rule. Parked.
4. **Online shop for a beloved store with no e-shop** (Buc-ee's → **TexasSnax.com**, reportedly $161K in sales in month 1 and $250–300K/month after; 2023 article).
   - **3/10 for us** as-is: physical inventory, shipping, thin margins.
   - Brand risk: Buc-ee's made him rename the store and add a disclaimer, and it sues over logo copies.
   - Pattern worth remembering: *"loved regional product + no online channel"*.
   - Possible variant: regional/national products for a **diaspora** (e.g. millions of Romanians abroad). Still logistics-heavy, and existing diaspora shops need checking.

### 🔎 Word-search deep-dive (2026-11-19)
- **The user's example, com.mobilegame.wordsearch** (Italic Games / Doodle Mobile SG):
  - 10M+ downloads, 4.6–4.7★ from about 472K ratings.
  - 100+ categories, Time/Classic modes, daily challenges, offline.
  - AppGoblin estimate (unverified): about 754K monthly users, **about $50K+/month, 100% ads**.
  - Store text in DE/RO/PT-BR is machine-translated English.
  - Complaints: **loud ads that ignore mute**, fake "virus" ads, ads that open Shopee.
- **Leaders (each 100M+ downloads):**
  - Word Search Explorer (PlaySimple, 4.9★, about $500K+/month est.).
  - Word Search Journey (about $200K+/month).
  - Word Search Quest (10 languages, about $200K+/month).
- **Senior and accessibility segment:** Senior Games (Tellmewow) 10M+; Lezigame 10M+ (a dementia review says it helps).
- **Lots of 2026 indie apps pitch "no ads / large print"** and all have tiny installs → that pitch alone doesn't get distribution.
- **Requests and gaps:**
  - Loud ads and broken mute; ads in the middle of a puzzle.
  - Repetitive puzzles, too easy.
  - "How to change languages?"
  - Custom word lists only in small paid apps.
  - **Word search for language learning exists only as tiny paid iOS apps**; nothing at scale on Android.
- **Native local apps are weak:**
  - **RO:** none at all.
  - TR: natives ≤50K installs.
  - DE: tiny.
  - BR: ≤500.
  - ES: ≤10K.
  - IT: Cupral 100K+.
  - The global apps only translate. → The opening is **native-quality local content**; plain multilingual is table stakes.
- **Web portals:** Poki and CrazyGames run the same single 2020 word search (Code This Lab): 4.1★ on Poki, 8.5 on CrazyGames, with a timer and no levels or hints. **An open slot.**
- **Concepts:**
  1. **Local-first word search** for underserved languages (RO, TR, PL, CZ, HU, GR…): correct diacritics, native themes (local football, dishes, cities, proverbs), ads that respect mute, no ad mid-puzzle.
  2. **Bilingual vocab hunt:** the grid is in the target language and the clues are in your language ("dog" → find CÂINE). Translation/definition cards and an offline review list. Every language pair is its own store keyword.
  3. **Calm large-print edition** plus custom word lists and printable PDFs; an HTML5 build to replace the old portal game.
- **Claude's pick:** one engine that ships concept 1 as the base game, concept 2 as a mode or a sibling app, and concept 3's accessibility settings. Launch **web portals first** (free traffic and data), then Android/iOS.

### 🛍️ "Loved offline brand, no e-shop" research (2026-11-19)
The user wants other shops or brands, in Romania or worldwide, that are strong offline but don't sell online. This is not a Buc-ee's copy.

**The model**
- **TexasSnax:** launched Nov 2020. Buc-ee's tolerated it on condition of a "not affiliated" notice. Its legal basis is the first-sale doctrine. Self-reported sales were $250–300K/month in 2023, and about 15 copycats appeared on Amazon. No coverage from 2025–26 was found.
- **Trader Joe's** Amazon resellers mark prices up 200–400%. Pirate Joe's was sued and closed in 2017.
- **Bokksu**, a Japanese snack box, made $4.8M in 2019 and raised a $22M Series A. That's proof the curated-box version scales.

**Law**
- **EU:** goods first sold in the EEA can be resold freely (exhaustion), but repackaging can let the brand object.
- **Food labels:** Reg. 1169/2011 requires mandatory info in the buyer's language, and the same info on the web page.
- **Amazon:** grocery is gated.
- **UK** (since Apr 2025): no personal imports of EU meat or dairy. Chocolate, biscuits and bread are OK.

**Romania**
- **Big brands are already available abroad:**
  - Eugenia is on Amazon and in Tesco UK.
  - Răureni and Borsec are on Amazon.
  - Gerovital is sold in 30+ markets.
  - Sibiu salami and zacuscă are sold in ethnic shops.
  - eMAG ships only to Hungary and Bulgaria.
- The real gaps are **small regional producers** (artisan cozonac, cheeses, local sweets), which are also the hardest to ship.

**Diaspora**
- About 4.6M people (UN, 2024), up to 5.6M+ (Romanian government). It's the largest diaspora in the EU.
- Main countries: Italy about 1.07M, Germany 0.8–1M, UK 0.71M, Spain 0.61M.
- Served by 1,000+ physical shops (MagazineRomanesti.eu), some online shops (A&S Market UK), van and parcel networks, and family food parcels that peak at Christmas.
- **Gaps (inferred):** no Romanian snack or gift **subscription box** was found, and no pan-EU Romanian online grocer.
- Shipping: GLS takes 4–7 days, and about €25 for 5 kg Romania → Spain. That's heavy on a €40 box.
- Other diasporas (Polish, Asian) are already served by supermarkets or VC-backed apps (Waysia, Yababa, Oja).

**Verdict**
- Holding inventory is **not low-touch**: expiry dates, labels, VAT once sales pass the €10K EU OSS (one-stop-shop VAT) threshold, seasonality, thin margins after shipping.
- Lean options, ranked:
  1. A curated "taste of home" gift and subscription box, using only shelf-stable sweets, fulfilled by a Romanian 3PL (warehouse that packs and ships orders). Also sold to families in Romania for gifting.
  2. A marketplace where producers ship themselves; we take a commission.
  3. An affiliate/SEO "where to buy X abroad" hub (most passive, lowest ceiling).
- **Claude's score: 4/10 for our goals.** Possible later as a seasonal Christmas test of option 1, not a first bet.

### 📦 Dropshipping research (2026-11-19)
**How it works:** we run the store and marketing, and the supplier ships each order. Legally **we are the seller**: EU 14-day returns (refund including shipping), GPSR liability, VAT.

**Costs**
- Shopify about $29–39/month plus apps: DSers free to $20, Spocket $24–40 + 2.9%.
- Print-on-demand (Printify/Printful/Gelato) has free tiers.
- Shopify Collective (brand-to-brand) is free.

**Reality**
- Net margin after ads: about 5–20%.
- Only an estimated 1–5% of stores make consistent profit (unverified).
- Meta ads: median cost per purchase about $39 and median ROAS (revenue per ad dollar) 1.88 (Triple Whale, 2025–26, secondary). So products under $30 don't work with paid ads.
- Returns 16–20%, and 25–40% for apparel.
- PayPal holds up to 21 days; Stripe reserves can run 90–180 days.
- Ongoing "where is my order?" support.

**Rule changes 2025–26**
- US de minimis gone: China from May 2025, all countries from Aug 2025.
- **EU €3 duty per item on parcels ≤€150 from 1 Jul 2026.**
- IOSS/OSS VAT since 2021.
- Temu/Shein have commoditized generic products.
- GPSR (since Dec 2024) requires an EU responsible person.

**Romania setup**
- Needs a PFA or SRL.
- Micro-SRL taxed on revenue, 1% or 3% (verify), with a €100K cap.
- VAT exemption threshold RON 395K.
- Above €10K of EU cross-border B2C sales → OSS VAT.

**Fit scores**
| Variant | Score |
|---|---|
| Generic AliExpress/CJ | 2 |
| EU-warehouse niche store | 4 |
| B2B dropship | 4 |
| Brand marketplace where we are seller of record | 4 |
| **POD on Etsy with EU fulfilment** | **6** |
| **Affiliate curated site** (brands sell and ship) | **7** |

- POD on Etsy: free marketplace traffic, but the median shop earns about £300–700/month, and 5–10% of designs bring most sales. Specific identity niches work best.
- Affiliate: Romanian shops pay 6–25% per sale via **2Performant** (which absorbed Profitshare). Returns, VAT and GPSR stay with the brand.

**Cheapest test (about €0–50)**
1. 20 Etsy POD designs with Romanian-diaspora themes (bilingual, regional, *ie* motifs).
2. Plus 15 "where to buy Romanian X abroad" SEO pages with affiliate links.
3. After 90 days, check impressions, clicks and sales.
- **Never use paid ads.**

**Claude's view:** dropshipping proper is out. The affiliate "taste of home / where to buy abroad" site plus diaspora POD is a cheap side test. It merges with the diaspora research above (affiliate = option 3 there).

## 5. Open questions for the user
- ~~Which country/language market?~~ → Answered: global, multilingual.
- Any personal hobbies/domain knowledge (cars, cooking, gaming, sports, finance…)? An insider edge makes idea A much stronger.
- Interest in running A (main bet) + B (side bet) in parallel?

## 6. Repo / git setup
- Remote: `git@github-personal:tirleadoru/business-ideas.git` (personal GitHub account **tirleadoru** via SSH key `~/.ssh/id_ed25519_personal`).
- Local git identity: `Doru Tirlea <tirlea.doru@gmail.com>` (set in the repo's local config).
- ⚠️ The global git config and the default `github.com` SSH key belong to the **business** account (DoruTirleaSD / smartdevsolutions). Never use them here.

- **Layout (2026-11-19):**
  - **Restructured (2026-11-19):** `~/Business Ideas/` is a plain folder.
  - The notes repo lives in `business-ideas/` (personal): `MEMORY.md`, `CLAUDE.md`, `notes/`.
  - Each product is a **sibling** folder with its own repo on the company account (e.g. `letterlyn/`). No repo-in-repo.
  - A root `CLAUDE.md` (untracked) imports `business-ideas/CLAUDE.md`.
  - **letterlyn/** (2026-11-19): repo `git@github.com:SmartDevSolutionsLimited/letterlyn.git` (the default github.com SSH key = DoruTirleaSD). The local identity is pinned to `DoruTirlea <doru@smartdevsolutions.net>`.
  - The domain letterlyn.com is being registered by Remus (pending).
  - Identity per business repo is confirmed before its first commit.
  - **Decided:** business repos go on the company account **DoruTirleaSD** (smartdevsolutions). The company publishes everything, and it already has App Store accounts and a D-U-N-S number.
  - No AI co-author lines in commits, ever.

## 7. Decision log
- **2026-11-19:** **No repo on the Letterlyn server** (user's preference). A deploy script on the Mac builds and uploads only outputs (site, web game, bundled API) over SSH. Releases folder + `current` link for rollback. Server checklist artifact: https://claude.ai/artifact/3RZVW5eDurcLFqf1Rdh33u
- **2026-11-19:** Remus does whatever we specify, so we hand him a decided spec instead of questions: `notes/letterlyn-server-setup.md` (Ubuntu 24.04, Frankfurt, 2 GB plan, nginx + Node 24 + MariaDB local, staging + prod API on ports 3001/3000, Lightsail snapshots + bucket DB dumps, support@/privacy@ email, monitoring).
- **2026-11-19:** Hosting decided: **Letterlyn gets its own setup on the company's AWS Lightsail** (Remus is the user's business partner and server admin). It's a separate business from red-assistance (EC2); don't compare or copy its infrastructure. One instance: nginx for site + web game, Node API (+ staging), DB on-box or Lightsail managed, Lightsail snapshots + bucket backups. Details: plan §12b.
- **2026-11-19:** **letterlyn.com bought.** Remus is preparing a server. Deployment explained: only build outputs go out (site → letterlyn.com, web game → play.letterlyn.com, API → api.letterlyn.com, mobile → stores). Claude recommends Cloudflare Pages + Workers instead of a self-managed server. Questions for Remus are in plan §12.
- **2026-11-19:** **Letterlyn M1 built** on branch `m1` (company repo, commit 1905eb5).
  - Layout: monorepo with `packages/engine` (all game rules: session, scoring/combos, daily+streaks, coins/XP/levels, achievements, save migration, share texts, friend codes), `packages/content` (packs + EN/RO strings), `apps/web` (plain TS, ~20 KB gz), `apps/mobile` (Expo SDK 58, Expo Router, Gesture Handler + Reanimated, haptics, expo-audio).
  - Tooling: Lefthook per-folder hooks, path-filtered GitHub checks (source only), red-assistance-style `scripts/build.sh`.
  - Verified:
    - 50 engine tests + 3 mobile tests; expo-doctor 20/20.
    - Web end-to-end in Chrome.
    - Android release build played end to end on the emulator (same daily, rewards and achievements as web).
    - iOS release build launches with light/dark mode (simulator touch not automated).
  - Open: real icon/splash art, `eas init` with the company account, user device testing, merge m1 → main.
- **2026-11-19:** Disk nearly full (2.4 GB free). With the user's OK, cleared the npm, Xcode DerivedData, Gradle and CocoaPods caches plus unavailable simulators → 46 GB free. Rule: delete Letterlyn's generated ios/android folders after each native test build.
- **2026-11-19:** User: no more tests; build each platform natively, two codebases OK. Claude proposes **Expo/RN for iOS+Android + plain TS web for portals/site**, sharing one TS engine (needed for identical daily puzzles and server checks). Swift+Kotlin advised against: 3 UIs + an engine ported twice + cross-language determinism risk. Waiting for the user's decision.
- **2026-11-19:** **Stack spike run** (branch spike/stack-comparison, company repo). Same 12×12 screen in Capacitor vs Expo.
  - Web: both 60 fps; Capacitor ready in ~0.5 s vs Expo ~2.4 s (both OK for portals).
  - Mobile (emulator/simulator): Expo starts faster (0.84 vs 1.18 s median on Android), has steadier frames (worst 33 vs 67 ms), and shows the board within 1 s on iOS. Capacitor showed a blank WebView for 6+ s on first iOS launch.
  - Leaning **Expo**. Waiting for the user's real-device tests (iPhone 13/16, S20 Ultra; budget Samsung A15/A16 recommended to buy). Details: plan §10.
- **2026-11-19:** The user demanded a premium feel ("we do not do shit stuffs in this company").
  - Research: WebViews are weakest for games/gestures/animation and on budget Android; no top-chart Capacitor games found. Claude corrected its earlier overconfident "plenty fast" claim.
  - Portal limits: CrazyGames ≤50 MB (≤20 MB for mobile homepage), Poki ~8 MB (unverified), so an Expo web build fits.
  - **Stack reopened:** proposed a 1–2 day device spike (Capacitor vs Expo universal, on iPhone + mid + budget Android), measuring fps, latency, cold start and web load. Expo (option B) expected to win; option C (Expo mobile + tiny web UI) is the fallback.
- **2026-11-19:** CI = source checks only; **no app builds in CI** (user). Native Capacitor projects are committed, with build output ignored. Builds are local, with fastlane one-command release scripts; cloud builds optional later (Capawesome/Codemagic; Ionic Appflow sunsets 31 Dec 2027).
- **2026-11-19:** **Monorepo agreed.** Per-folder checks: Lefthook hooks (glob/root per workspace; engine changes trigger game + API checks) and CI with path filters + Turborepo affected runs. Native builds run on CI/release. **The Letterlyn plan is complete**, ready for M1 on the user's go.
- **2026-11-19:** Stack decided: **one codebase, web + Capacitor, React UI** (user OK).
  - The user referenced the red-assistance multi-repo split (mobile/admin/web/api).
  - Claude proposes a **monorepo** (packages/engine + content shared by game and API; apps/game, api, site, admin later). The shared engine is needed for server-side score checks. Waiting for the user's decision.
- **2026-11-19:** User decisions:
  - Content packs move to the **end** (decided together then).
  - **iOS joins the launch wave.**
  - They asked about React Native and about cross-device progress. Claude proposes **web core + Capacitor** (portals need a tiny web build; React/Preact UI OK) instead of RN + RN-web.
  - Cross-device: one player record with several identities attached (device, Google, Apple, CrazyGames). Optional "Save your progress" via Sign in with Google/Apple (no passwords stored). Link codes for CrazyGames/Poki. Defined merge rules.
- **2026-11-19:** The user approved Relax/Challenge, the coin economy, and EN + RO first.
  - They pushed back on backend phasing: how do we get data in one place and shared leaderboards across web and mobile without a backend? **They're right:** platform services are silos.
  - Revised: **small own backend from launch** (Cloudflare Workers + D1, $5/month paid plan), anonymous player ID + generated nickname, transfer code instead of logins, server-checked scores, one leaderboard per day/language everywhere.
  - Constraints: Poki blocks external requests unless approved, and allows no personal data. CrazyGames allows backends and has its own leaderboards; it forbids Google/email logins inside games.
  - Also revised: **launch Android together with the portals**, since mobile players may not visit portals.
- **2026-11-19:** User feedback on M0: works well, but needs more packs, a how-to-play and settings menu (backwards words were not obvious), monetization, long-term replayability/competition, and a backend question.
  - **Product plan v1 written:** `notes/letterlyn-plan.md`.
  - Contents: onboarding with direction cards; fair-ads placement and a soft coin economy; Daily Puzzle + streak; Relax vs Challenge (timer, score, combo); share and friend codes; Quick Play; XP and achievements.
  - Backend phases: none → Play Games/Game Center/CrazyGames → own serverless backend only if justified. No own login system.
  - Waiting for the user's decisions (plan §6). No coding until agreed.
- **2026-11-19:** **Letterlyn M0 prototype done** and pushed to SmartDevSolutionsLimited/letterlyn (`936f426`).
  - Vite + TypeScript, no framework, about 7 KB gzipped.
  - Seeded generator, EN + RO, 6 packs × 12 puzzles, hints, stars, saved progress.
  - 19 tests pass. Played end to end in headless Chrome in both languages.
  - Next: M1 (daily puzzle, 30 packs per language, sound/haptics, large print, banned-word lists).
- **2026-11-19:** The user picked Letter Moss. **The check killed it:** "LetterMoss: Филворд", a Russian word search game, is already in a Play closed test (Oct 2026), and there is a US "MOSS" game mark (Polyarc). Remaining clean options: **Letterlyn** (coined, strongest) and **Letter Hush**. Waiting for the user's choice and a manual TMview/USPTO check.
- **2026-11-19:** Word search: **English is the main language, Romanian is the first extra** (in-app switch, localized store listings). Name shortlist checked (see design doc §3): Letter Moss, Letter Hush, Letterlyn/Wordlyn, Letter Still, Word Sanctum. Waiting for the user's pick, then a trademark check.
- **2026-11-19:** Game design v0.1 written: `notes/word-search-game-design.md`.
- **2026-11-19:** Researched word search, offline-only brands/diaspora, and dropshipping.
  - Claude recommends **word search as the first product**: local-first, Romanian quality test, with a bilingual vocabulary mode; web portals first, then mobile.
  - Diaspora: an affiliate site plus Etsy POD as a cheap side test.
  - Dropshipping with inventory or paid ads: rejected.
- **2026-11-19** — The user wants the falling game (Nohzdyve-style) as their passion project, with 2027 fully focused on building income. Proposed order: falling game → multilingual word puzzle → 3D upgrade or artillery game. Model: free + ads + "remove ads" purchase, not paid up front.
- **2026-11-19** — Repo set up to use the personal git identity + personal SSH host alias.
- **2026-11-19** — Ruled out runtime AI/LLM features for now (usage-based cost). Non-AI search/rules engine accepted as an approach.
- **2026-11-19** — The user has no domain edge from client work (Drupal clients don't pay for add-ons). Strategy adopted: a portfolio of small, low-maintenance bets hosted on other platforms, each with monetization. Games deep-dive done (see §4 Games).
- **2026-11-19** — Round 3 category checks: WP broken-link checker 6/10, Confluence Mermaid 4/10, Shopify size charts 3/10, pickup/delivery 3/10. Insight: marketplace utilities are being commoditized by AI-built clones; look for unfair advantages next.
- **2026-11-19** — Every product needs a built-in way to make money (free tiers are OK only as a funnel).
- **2026-11-19** — Downgraded Shopify digital downloads: Shopify's own free app (4.8★, 1.5K reviews) and Filemonk ($10–25 flat, 4.9★) already cover the market. New rule: check the whole category before scoring.
- **2026-11-19** — Downgraded the ModHeader replacement: many free clones exist, and single-user browser tools barely monetize. New rule: favour markets where paying monthly is already normal.
- **2026-11-19** — Research round 2 (Shopify, Chrome, WordPress, Atlassian/Google) done. Leaders: Shopify flat-price digital downloads, ModHeader replacement, Google Docs heading numbering. Waiting for the user's pick and a deep-dive validation.
- **2026-11-19** — Dropped #1 (seller recall monitor): 15+ apps with 0 reviews means low demand, and there's a free competitor. Adopted the "proven demand + beatable incumbent" validation rule.
- **2026-11-19** — Research round 1 done. Top 5 ranked (see §4). Recommended a shared "global recall data engine", with the seller recall-monitor app first. Waiting for the user's pick.
- **2026-11-19** — Everything targets a global audience, multilingual from launch, with translation done at build time.
- **2026-11-19** — Car warning lights researched: saturated, and free OS features already do it. Not building it as a standalone product. Idea A now limited to domains with authoritative public datasets.
- **2026-11-19** — Shortlist: A (knowledge engine + programmatic SEO) as the main bet, B (casual web/mobile game) as a side bet, C (marketplace app) as an alternative. Waiting for the user's input on market/domain.
