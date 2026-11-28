@AGENTS.md

# Multi-Agent SDD Orchestration (default profile)

**OPUS THINKS, SONNET WRITES, HAIKU READS.**

| Role | Agent (`.claude/agents/`) | Default model | Tools |
|------|---------------------------|---------------|-------|
| Think / decide / coordinate | `sdd-orchestrator` (main session via `.claude/settings.json`) | `opus` | Read, Grep, Glob, Agent |
| Write / implement / test | `sdd-implementer` | `sonnet` | Read, Write, Edit, Grep, Glob, Bash |
| Read / explore / extract | `sdd-explorer` | `haiku` | Read, Grep, Glob (read-only) |

Rules:
1. Opus thinks and coordinates; architectural decisions stay with it.
2. Sonnet writes and implements; no unilateral change to decisions or requirements.
3. Haiku reads and investigates; strictly read-only, no decisions.
4. Delegation is explicit and by responsibility. Reads -> Haiku. Writes -> Sonnet.
5. No task is complete without verifying results (tests, file refs).
6. Agents share structured results (see each agent's report format).
7. Keep traceability: requirement -> SPEC -> implementation -> test.
8. SPEC -> PLAN -> TASKS gates follow `docs/decisions/ADR-001-sdd-state-machine.md`.

Models are defaults, not fixed. To change them see `docs/workflows/multi-agent.md`. Never set `CLAUDE_CODE_SUBAGENT_MODEL` (forces one model on all subagents).
