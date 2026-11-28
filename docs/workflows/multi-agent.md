# Multi-Agent SDD (Opus / Sonnet / Haiku)

Default profile. **OPUS THINKS, SONNET WRITES, HAIKU READS.** Native Claude Code subagents in `.claude/agents/` plus `.claude/settings.json` (`model`, `agent`).

## Roles

| Agent | Model | Tools | Owns |
|-------|-------|-------|------|
| `sdd-orchestrator` | `opus` | Read, Grep, Glob, `Agent(sdd-explorer, sdd-implementer)` | analysis, planning, architecture, delegation, review, gates |
| `sdd-implementer` | `sonnet` | Read, Write, Edit, Grep, Glob, Bash | specs, code, tests, refactors, docs, verification |
| `sdd-explorer` | `haiku` | Read, Grep, Glob (`permissionMode: plan`) | exploration, symbol/ref search, log/config extraction |

## SDD phases -> agents

| Phase | Lead | Support |
|-------|------|---------|
| 1 Discovery | Orchestrator | Explorer |
| 2 Thinking & Planning | Orchestrator | Explorer |
| 3 Specification | Implementer (writes), Orchestrator (reviews) | Explorer |
| 4 Implementation | Implementer | Explorer |
| 5 Validation | Orchestrator | Implementer (fixes), Explorer (context) |
| 6 Completion | Orchestrator | - |

## Parametrizing (default stays opus/sonnet/haiku)

Per-role model: edit `model:` in the agent frontmatter. Accepted: `opus`, `sonnet`, `haiku`, a full model ID, or `inherit` (main session model).

| Profile | orchestrator | implementer | explorer |
|---------|--------------|-------------|----------|
| default | opus | sonnet | haiku |
| economy | sonnet | sonnet | haiku |
| single-model | inherit | inherit | inherit |

- Main session model / default agent: `.claude/settings.json` -> `"model"`, `"agent"`.
- Personal override without touching the repo: `.claude/settings.local.json` or `claude --model <alias>`.
- Disable orchestration: remove `"agent"` from `settings.json` (agents stay available for manual delegation).
- Never use `CLAUDE_CODE_SUBAGENT_MODEL`: it forces every subagent to one model.
- Per-feature deviations: record in `PLAN.md` section "Agent & Model Assignment".

## Verify from a Claude Code session

- `/agents`: three `sdd-*` agents listed under Project with their models.
- Prompt: "Use sdd-explorer to map `src/` with file:line refs." Must not edit anything.
- Prompt: "Plan feature X with SDD." Orchestrator delegates reads to explorer, writes to implementer.

## Limitations

- Subagents cannot spawn subagents. Orchestration works because `sdd-orchestrator` runs as the **main session** (`"agent"` in settings). Invoked as a subagent it cannot delegate.
- `sdd-explorer` has no Bash (no `git log`, etc.): trade-off for strict read-only.
