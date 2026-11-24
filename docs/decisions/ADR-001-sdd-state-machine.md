# ADR-001: SDD State Machine

**Status**: Accepted  
**Date**: 2026-11-24  
**Author**: RKOrtega94

## Context

This repository uses Spec-Driven Development (SDD) with a mandatory feature folder flow:
- `docs/features/<feature>/SPEC.md`
- `docs/features/<feature>/PLAN.md`
- `docs/features/<feature>/TASKS.md`

The project requires explicit state tracking and approval gates between phases to prevent unapproved work from progressing to implementation.

## Decision

Adopt a 4-state machine for all SPEC, PLAN, and TASKS files:

### States

| State | Description |
|-------|-------------|
| `draft` | Initial state; content being prepared; not yet reviewed |
| `review` | Content complete; awaiting feedback/approval from user |
| `approved` | User has explicitly approved; ready for next phase transition |
| `rejected` | User has rejected; content needs rewriting or abandonment |

### State Invariants (Critical Rules)

1. **SPEC → PLAN Gate**: PLAN may only be created after SPEC reaches `approved` state. If SPEC is `rejected`, work returns to `draft`.

2. **PLAN → TASKS Gate**: TASKS may only be created after PLAN reaches `approved` state. If PLAN is `rejected`, work returns to `draft`.

3. **Approval Must Be Explicit**: Transitions `review → approved` and `review → rejected` require explicit user consent. Saying "ok", "sure", "implement it" does NOT automatically approve - the user must use the word "approved" or equivalent explicit affirmation.

4. **Plan Approval ≠ Auto-Implementation**: Approving the PLAN (`PLAN: approved`) does NOT mean tasks should be implemented automatically. The user must separately say "implement tasks", "start implementation", or equivalent explicit command. Only then does the TASKS state transition from `draft` → `review` → `approved`.

5. **Task Completion**: TASKS may transition to `completed` only after `approved` state is reached AND user explicitly says "tasks are complete" or "finished".

### Transitions

```text
SPEC:      draft → review → [approved/rejected]
           │              ↑
           │              │
           └─[user says "approved"]↑
           (explicit)         │
                            │
PLAN:      draft → review → [approved/rejected]
           │              ↑
           │              │
           └─[user says "approved"]↑
           (explicit)         │
                            │
TASKS:     draft → review → [approved/rejected/completed]
           │       ↑              ↑
           │       │              │
           └─[user says "approved"]─┘
           (explicit for approved)
           └─[user says "completed"]─┘
           (explicit for completed)
```

### On-Hold State (Optional)

- `on_hold`: May be used when work is paused temporarily (waiting on external info, product decision). Does not block other transitions permanently; may be resumed back to `review`.

### Consequences

#### Positive

- **Explicit handoffs**: No ambiguity about when one phase ends and another begins
- **User control**: User must consciously approve each transition, preventing accidental progression
- **Clear audit trail**: Git history shows exactly when each state was set and by what signal
- **Safety guardrail**: Prevents "half-implemented" features without proper approval
- **Scalable**: Works with sub-agent driven or inline implementation modes

#### Negative / Trade-offs

- **Requires conscious user interaction**: Each transition needs user saying the magic word
- **Additional overhead**: Slightly slower for very small/simple features
- **State management discipline**: Templates must carry the `State:` field consistently

### Related

- `docs/templates/SPEC_TEMPLATE.md` — now includes `State: draft` frontmatter
- `docs/templates/PLAN_TEMPLATE.md` — now includes `State: draft` frontmatter
- `docs/templates/TASKS_TEMPLATE.md` — now includes `State: draft` frontmatter
- `AGENTS.md` — path adaptation and adoption guidelines
- `README.md` — adoption section (Option A: new project, Option B: incremental)

---

**Tags**: sdd, state-machine, spec-driven, workflow, approval-gates

**Supersedes**: (none — first ADR for this repository)