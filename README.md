# Hexagonal Python Starter Kit (SDD + ECC + Superpowers)

A cloneable modern Python starter repository built around **Hexagonal Architecture (Ports & Adapters)**, **Spec-Driven Development (SDD)**, **ECC (Everything Claude Code / harness engineering)**, and **Superpowers** (subagents and `git worktree` isolation)[cite: 1, 2]. It uses a RAG service with local or remote embeddings, hybrid retrieval, confidence/formatting policies, API, and CLI as a reference architecture while keeping the core domain-agnostic[cite: 1, 2].

## Key Features

- **Strict Hexagonal Architecture**: Isolates `domain/` and `application/` from frameworks, databases, external SDKs, and environment variables[cite: 1, 2].
- **Per-Feature SDD Workspace (`docs/features/<feature>/`)**: Every new feature or task starts by creating `docs/features/<feature>/` with `SPEC.md`, `PLAN.md`, and `TASKS.md` from `docs/templates/`.
- **Superpowers (Subagents & Git Worktrees)**: Isolates iterations in dedicated `git worktree` directories and delegates scoped subtasks to subagents.
- **ECC Discipline**: Enforces focused context, verification, quality/security review, and persistent learnings across sessions.
- **Token-Efficiency Skills (`ponytail`, `caveman`)**: Reduces token consumption across context reads, status updates, and technical responses without dropping accuracy or security rules.
- **Pluggable External Memory**: Supports memory backends such as **Engram**, **Graphiti**, **claudemem**, and **Obsidian** without hardcoding a single vendor.
- **Modern Python & Security Baseline**: Enforces explicit typing, clean contracts, bounded concurrency, safe configuration handling, and input/path validation[cite: 1, 2].

---

## Repository Layout

```text
.
├── AGENTS.md
├── README.md
├── pyproject.toml
├── docs/
│   ├── architecture/
│   │   └── hexagonal-python.md
│   ├── workflows/
│   │   └── sdd-ecc.md
│   ├── security/
│   │   └── python-security-baseline.md
│   ├── memory/
│   │   └── external-memory.md
│   ├── decisions/
│   │   └── README.md
│   └── templates/
│       ├── SPEC_TEMPLATE.md
│       ├── PLAN_TEMPLATE.md
│       └── TASKS_TEMPLATE.md
├── src/
│   └── <package>/
│       ├── domain/
│       ├── application/
│       └── infrastructure/
└── tests/

```

---

## Quick Start & Adoption

1. **Clone the repository**:

```bash
git clone <your-repo-url> my-python-service
cd my-python-service
```

1. **Set up Python environment & dependencies**:
Create and activate a Python 3.12+ virtual environment and install project and dev dependencies from `pyproject.toml`.
2. **Rename / adapt the package**:

- Rename `src/<package>/` to your target package name and update imports and entry points consistently.

- Adapt the reference RAG models, ports, and adapters to your domain.

1. **Configure environment variables**:
Set required environment variables (model endpoints, API keys, database/vector settings, similarity thresholds, and concurrency limits). Never commit secrets to git.

2. **Start a feature with SDD + Worktree**:

- Create a `git worktree` for the feature/branch.

- Create `docs/features/<feature>/` and copy `SPEC_TEMPLATE.md`, `PLAN_TEMPLATE.md`, and `TASKS_TEMPLATE.md` from `docs/templates/` into `SPEC.md`, `PLAN.md`, and `TASKS.md`.

---

## Configuration & Security Notes

- **Secrets & Environment**: Load API keys, tokens, and credentials strictly from environment variables or a secret manager. Never store secrets in source code, `docs/`, logs, or external memory.

- **Re-indexing / Schema Migrations**: When switching embedding providers or dimensions (for example, moving between local `768`-dim embeddings with HNSW and remote `2048`-dim embeddings with exact search), plan a clean migration/re-index rather than mixing incompatible vectors.

- **Input & Resource Boundaries**: Validate external payloads and file paths (preventing path traversal), enforce timeouts and concurrency semaphores, and treat retrieved or LLM-generated text as untrusted input.

---

## Token-Efficiency Skills (`ponytail`, `caveman`)

- Read `AGENTS.md` first, then load only the `docs/` guide and `docs/features/<feature>/` files (`SPEC.md`, `PLAN.md`, `TASKS.md`) needed for the active step.
- Use `ponytail` and `caveman` to keep context reads targeted and technical outputs concise while preserving layer rules, tests, and security checks.

---

## External Memory Configuration

External memory stores long-term context (ADRs, constraints, resolved issues, and session summaries) outside the active prompt window.

### What to Store vs. Exclude

- **Store**: Architectural decisions (ADRs), layer/port conventions, environment constraints, index/schema changes, and verified technical learnings.

- **Exclude**: API keys, tokens, credentials, PII/sensitive data, and noisy raw logs.

### Supported Memory Backends

| Backend | Best For | How to Configure in Your Workflow |
| --- | --- | --- |
| **Engram** | Structured observations, decisions, and session summaries | Configure your Engram MCP/CLI integration in your agent harness and record key ADRs, conventions, and milestone summaries at the end of tasks. |
| **Graphiti** | Temporal knowledge graphs of entities, decisions, and changes | Connect your Graphiti server/client and persist architectural entities, relationships, and time-scoped changes as specs/plans evolve. |
| **claudemem** | Session history and working context for Claude workflows | Enable `claudemem` in your Claude setup so session context, prior fixes, and recurring project patterns remain searchable across runs. |
| **Obsidian** | Local Markdown vault (`ADRs`, notes, backlinks, runbooks) | Point your vault or sync scripts to a dedicated project folder/notes and link ADRs, specs, and operational notes using Markdown/backlinks. |

---

## Working with SDD + ECC + Superpowers

1. Create `docs/features/<feature>/` and populate `SPEC.md`, `PLAN.md`, and `TASKS.md` from `docs/templates/`.
2. Work inside an isolated `git worktree` and delegate independent subtasks to subagents (`superpowers`) when helpful.
3. Run tests, type/lint checks, architecture boundary checks, and security checks before marking tasks complete.
