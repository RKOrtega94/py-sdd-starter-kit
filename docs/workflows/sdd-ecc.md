# SDD + ECC + Superpowers Workflow & Token Efficiency

## 1. Per-Feature Folder Requirement (`docs/features/<feature>/`)

Every time the agent begins iterating or starts a new feature/task, it must first create `docs/features/<feature>/` (for example, `docs/features/user-login/`) and initialize:

- `docs/features/<feature>/SPEC.md` from `docs/templates/SPEC_TEMPLATE.md`
- `docs/features/<feature>/PLAN.md` from `docs/templates/PLAN_TEMPLATE.md`
- `docs/features/<feature>/TASKS.md` from `docs/templates/TASKS_TEMPLATE.md`

## 2. How SDD, ECC, and Superpowers Work Together

- **SDD (`SPEC.md` -> `PLAN.md` -> `TASKS.md`)**:
  - `SPEC.md`: scope, requirements, contracts, security, and acceptance criteria.
  - `PLAN.md`: hexagonal layer changes, ports/adapters, risks/migrations, worktree/subagent plan, and verification strategy[cite: 2].
  - `TASKS.md`: actionable checklist, test/security gates, and progress log.
- **ECC**:
  - Focused context per step, test-first/verification discipline, quality and security review, and persisting durable learnings/ADRs.
- **Superpowers (Subagents & Git Worktrees)**:
  - Use a dedicated `git worktree` per feature/branch so active iterations stay isolated from `main` and other features.
  - Delegate bounded, parallelizable subtasks to subagents (for example, test authoring, adapter wiring, or security/boundary review) and integrate results cleanly.

## 3. Token-Efficiency Skills (`ponytail`, `caveman`)

Applied directly to this project to reduce token usage:

- Load `AGENTS.md` first, then read only the relevant `docs/` guide and active `docs/features/<feature>/` files (`SPEC.md`, `PLAN.md`, `TASKS.md`).
- Keep status updates and technical responses concise and structured (`caveman` / `ponytail`) while preserving exact contracts, edge cases, and security constraints.

## 4. Definition of Done (DoD)

- **Feature Docs Ready**: `SPEC.md`, `PLAN.md`, and `TASKS.md` exist in `docs/features/<feature>/` and reflect actual decisions.
- **Architecture & Security Verified**: hexagonal dependency rules respected, inputs/paths/secrets checked, and required tests passing[cite: 1, 2].
- **Tracked & Clean**: `TASKS.md` updated, key decisions/learnings recorded, and temporary worktrees cleaned up when merged.
