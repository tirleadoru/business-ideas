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
  - The personal-only rule above applies to this root repo. Inside a business folder, confirm with the user which identity and remote to use before the first commit there.
- Budget constraint: avoid solutions with per-usage costs (e.g. paid LLM APIs at runtime).
