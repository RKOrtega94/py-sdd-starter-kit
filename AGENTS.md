# AGENTS.md — Project Operating Framework (Modern Python + Hexagonal + SDD + ECC + Superpowers)

This file defines the operating rules for architecture, feature specs, subagent/worktree execution, security, token efficiency, and external memory for any agent working on this repository.

## 1. Repository Purpose

This repository is a cloneable **modern Python** starter kit built around **Hexagonal Architecture (Ports & Adapters)**, **Spec-Driven Development (SDD)**, **ECC (Everything Claude Code / harness engineering)**, and **Superpowers** (subagents and `git worktree` isolation)[cite: 1, 2]. It uses a RAG service with local or remote embeddings, hybrid retrieval, confidence/formatting policies, API, and CLI as a reference architecture while keeping the core domain-agnostic[cite: 1, 2].

## 2. Repository Structure

- `src/<package>/`: application code split into `domain/`, `application/`, and `infrastructure/`[cite: 1, 2].
- `tests/`: unit tests, integration tests, and evaluation suites.
- `docs/architecture/hexagonal-python.md`: hexagonal rules, layer boundaries, and migration/re-index guidance[cite: 1, 2].
- `docs/workflows/sdd-ecc.md`: SDD + ECC + Superpowers workflow, token efficiency skills (`ponytail`, `caveman`), and feature folder rules.
- `docs/security/python-security-baseline.md`: modern Python security baseline[cite: 1, 2].
- `docs/memory/external-memory.md`: pluggable external memory conventions[cite: 2].
- `docs/decisions/`: Architecture Decision Records (ADRs).
- `docs/templates/`: official templates (`SPEC_TEMPLATE.md`, `PLAN_TEMPLATE.md`, `TASKS_TEMPLATE.md`).
- `docs/features/<feature>/`: per-feature SDD workspace containing `SPEC.md`, `PLAN.md`, and `TASKS.md` (created before starting any new feature or task).
- `README.md`: cloning, adoption, configuration, token-saving skills, and external memory guide.
- **Path Adaptation for Existing Projects**: In new projects the canonical structure is `src/<package>/` and `tests/`. In existing projects, adapt the real package and test directory paths to match your layout — the mandatory `docs/features/<feature>/` creation, hexagonal layer boundaries (`domain/`, `application/`, `infrastructure/`), and SDD flow remain unchanged.

## 3. Mandatory Feature Start Rule

Before starting any new feature or iteration task:

1. Create `docs/features/<feature>/` (for example, `docs/features/user-login/`).
2. Generate `SPEC.md`, `PLAN.md`, and `TASKS.md` inside `docs/features/<feature>/` from `docs/templates/SPEC_TEMPLATE.md`, `docs/templates/PLAN_TEMPLATE.md`, and `docs/templates/TASKS_TEMPLATE.md`.
3. Isolate work using a `git worktree` and delegate independent subtasks to subagents (`superpowers`) when iterating across components, tests, or reviews.

## 4. Non-Negotiable Rules

1. **Strict Hexagonal Architecture**:
   - `domain/`: models, ports (`Protocol`/ABC), domain services, and domain exceptions. No web frameworks, DB drivers, third-party SDKs, or `os.environ`[cite: 1, 2].
   - `application/`: use cases and DTOs. Depends only on `domain/` and standard library/typing.
   - `infrastructure/`: `outbound/` adapters, `inbound/` entry points (API, CLI), config, and composition root[cite: 1, 2].
2. **No Duplicate or Stray Files**: keep each responsibility in its single canonical module; do not leave stray files in the package root or duplicate folders.
3. **Modern Python & Typing**: enforce explicit type annotations, explicit error handling, and bounded concurrency/resources[cite: 1, 2].
4. **Security by Default**: never expose secrets, API keys, tokens, or sensitive data in code, logs, errors, or memory; validate inputs, paths, and limits[cite: 1, 2].
5. **Token Efficiency (`ponytail`, `caveman`)**: keep context reads targeted, state updates compact, and technical responses direct without dropping requirements or security rules.

## 5. SDD + ECC + Superpowers Flow

1. **Specify (`docs/features/<feature>/SPEC.md`)**: define problem, scope, functional/non-functional requirements, contracts, security, and acceptance criteria.
2. **Plan (`docs/features/<feature>/PLAN.md`)**: map hexagonal layer impact, ports/adapters, `git worktree` and subagent delegation, risks/migrations, and test strategy[cite: 2].
3. **Execute (`docs/features/<feature>/TASKS.md`)**: execute tasks in an isolated worktree (with subagents where helpful), run tests and security/architecture checks, and update task status.
4. **ECC Loop**: plan with focus, verify/test, implement incrementally, review quality/security, and record key learnings in external memory or `docs/decisions/`.

## 6. Required References

- `docs/architecture/hexagonal-python.md`
- `docs/workflows/sdd-ecc.md`
- `docs/security/python-security-baseline.md`
- `docs/memory/external-memory.md`
- `docs/decisions/README.md`
- `docs/templates/SPEC_TEMPLATE.md`
- `docs/templates/PLAN_TEMPLATE.md`
- `docs/templates/TASKS_TEMPLATE.md`
- `README.md`
