# Pluggable External Memory Conventions

This document defines the pluggable external memory conventions for this repository. External memory stores long-term context (ADRs, constraints, resolved issues, and session summaries) outside the active prompt window.

## 1. What to Store vs. Exclude

### Store These

- Architectural decisions (ADRs)
- Layer/port conventions
- Environment constraints
- Index/schema changes
- Verified technical learnings
- Session summaries at task completion

### Exclude These

- API keys, tokens, credentials
- PII/sensitive data
- Noisy raw logs
- Raw embedding vectors (store only metadata/references)

## 2. Supported Memory Backends

| Backend | Best For | How to Configure in Your Workflow |
| --- | --- | --- |
| **Engram** | Structured observations, decisions, and session summaries | Configure your Engram MCP/CLI integration in your agent harness and record key ADRs, conventions, and milestone summaries at the end of tasks. |
| **Graphiti** | Temporal knowledge graphs of entities, decisions, and changes | Connect your Graphiti server/client and persist architectural entities, relationships, and time-scoped changes as specs/plans evolve. |
| **claudemem** | Session history and working context for Claude workflows | Enable `claudemem` in your Claude setup so session context, prior fixes, and recurring project patterns remain searchable across runs. |
| **Obsidian** | Local Markdown vault (`ADRs`, notes, backlinks, runbooks) | Point your vault or sync scripts to a dedicated project folder/notes and link ADRs, specs, and operational notes using Markdown/backlinks. |

## 3. Memory Storage Format

### ADR Format (Markdown)

```markdown
# ADR 001: Choice of Framework

## Status
Superseded

## Context
We considered using Flask vs. FastAPI for the inbound adapter layer.

## Decision
Adopt FastAPI for its automatic API docs and better async support.

## Consequences
- Pros: automatic docs, better type safety
- Cons: heavier dependency footprint
```

### Session Summary Format (JSON)

```json
{
  "session_id": "ses_abc123",
  "date": "2026-01-15T10:30:00Z",
  "accomplished": [
    "Created SPEC.md for user-auth feature",
    "Implemented user repository adapter",
    "Added unit tests for domain layer"
  ],
  "discoveries": [
    "FastAPI dependency injection differs from Flask's",
    "Need to validate environment variables at startup"
  ],
  "next_steps": [
    "Implement password hashing with Argon2",
    "Add rate limiting to auth endpoints"
  ]
}
```

## 4. Migration Between Backends

- When switching from one backend to another (e.g., Engram → Graphiti), export existing data in a neutral format first.
- Update `docs/memory/external-memory.md` to reflect the new backend's conventions.
- Run migration scripts before cutting over; keep old data read-only during transition period.
