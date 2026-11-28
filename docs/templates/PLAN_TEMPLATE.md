# PLAN_TEMPLATE.md

State: draft

This is the official PLAN template for feature planning. Copy this file to `docs/features/<feature>/PLAN.md` when starting a new feature.

## 1. Hexagonal Layer Impact

- `domain/`: changes needed (new models, ports, services)
- `application/`: use cases, DTOs to create/modify
- `infrastructure/`: adapters, entry points, config changes

## 2. Ports & Adapters Map

### 2.1 Outbound Adapters

- Repository interfaces: `...`
- External service integrations: `...`

### 2.2 Inbound Entry Points

- API endpoints: `...`
- CLI commands: `...`

## 3. Risks & Migrations

- Known risks and mitigation strategies
- Data migration requirements (if applicable)
- Backward compatibility considerations

## 4. Worktree & Subagent Plan

- Feature branch name: `...`
- Git worktree directory: `...`
- Subagent delegation plan (if applicable)

## 4.1 Agent & Model Assignment

Default profile (see `docs/workflows/multi-agent.md`): OPUS thinks, SONNET writes, HAIKU reads. Change only if this feature needs a deviation.

| Role | Agent | Model | Override reason |
|------|-------|-------|-----------------|
| Think / decide | `sdd-orchestrator` | opus | default |
| Write / implement | `sdd-implementer` | sonnet | default |
| Read / explore | `sdd-explorer` | haiku | default |

## 5. Verification Strategy

- Unit test coverage targets
- Integration test requirements
- Architecture boundary checks
- Security boundary checks
