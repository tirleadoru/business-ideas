# CLAUDE.md

This repo is a workspace for brainstorming, validating and building low-maintenance income products.

## Rules
- **Read `MEMORY.md` at the start of every session.** It holds the goals, constraints, idea pipeline and decision log.
- **Update `MEMORY.md` after every meaningful discussion:** new ideas, analysis, research findings (with dates), decisions, and open questions. Keep it organized, not append-only chat logs.
- **Git must use the personal account only.** Before any commit/push, verify:
  - `git config user.email` → `tirlea.doru@gmail.com`
  - `git remote get-url origin` → uses host `github-personal` (not `github.com`)
  - Never use the business identity (smartdevsolutions / DoruTirleaSD).
- **Repo layout:**
  - This root repo, on the personal account, tracks only shared notes: `MEMORY.md`, `CLAUDE.md`, `notes/`.
  - Each business gets its own top-level folder with its **own separate git repo**, on the company account chosen for that business. The root `.gitignore` ignores those folders.
  - The personal-only rule above applies to this root repo.
  - **Business folders use the company account `DoruTirleaSD` (smartdevsolutions).** That company publishes the products: it has App Store accounts and a D-U-N-S number. Set each business repo's local identity and remote explicitly before its first commit.
- **Never add AI attribution** (no `Co-Authored-By: Claude`, no "Generated with Claude Code") to commits or PRs, in any repo.
- Budget constraint: avoid solutions with per-usage costs (e.g. paid LLM APIs at runtime).
