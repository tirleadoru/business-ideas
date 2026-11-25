# CLAUDE.md

This repo is a workspace for brainstorming, validating and building low-maintenance income products.

## Rules
- **Read `MEMORY.md` at the start of every session.** It holds the goals, constraints, idea pipeline and general decision log. **Working on LetterLyn: also read `letterlyn/MEMORY.md`** (where we left off, LetterLyn decisions, page links).
- **One folder per product in this repo** (`letterlyn/`, …): everything specific to that product (its memory, rules, plan, page sources, tools) goes there; the root holds only general business notes.
- **LetterLyn rules sheet: `letterlyn/rules.md`.** Every decided rule and number. Check it before stating a rule or writing code, data or pages, and update it the moment a decision changes. Old prototype code is never a source of decisions.
- **Update the right memory after every meaningful discussion** (`MEMORY.md` for general topics, `<product>/MEMORY.md` for a product): new ideas, analysis, research findings (with dates), decisions, and open questions. Keep it organized, not append-only chat logs.
- **Folder layout** (`~/Business Ideas/` is a plain folder, not a git repo):
  ```
  Business Ideas/
  ├── CLAUDE.md          ← untracked pointer, imports business-ideas/CLAUDE.md
  ├── business-ideas/    ← THIS repo: shared notes (personal account); business-ideas/letterlyn/ = LetterLyn notes
  └── <product>/         ← one sibling folder + own repo per business (company account), e.g. letterlyn/
  ```
- **This repo (`business-ideas/`) uses the personal account only.** Before any commit/push, verify:
  - `git config user.email` → `tirlea.doru@gmail.com`
  - `git remote get-url origin` → uses host `github-personal` (not `github.com`)
  - Never use the business identity here.
- **Product repos use the company account `DoruTirleaSD` (smartdevsolutions).** The company publishes the products: it has App Store accounts and a D-U-N-S number. Set each product repo's local identity and remote explicitly before its first commit. Never use the personal identity there.
- Always run git with `git -C <absolute path>` so each command targets the right repo.
- **Never add AI attribution** (no `Co-Authored-By: Claude`, no "Generated with Claude Code") to commits or PRs, in any repo.
- Budget constraint: avoid solutions with per-usage costs (e.g. paid LLM APIs at runtime).
