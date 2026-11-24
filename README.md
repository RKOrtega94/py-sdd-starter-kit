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
├── AGENTS.md              # Project operating framework (hexagonal + SDD + ECC + superpowers)
├── README.md              # This file — cloning, adoption, configuration, token-saving skills
├── pyproject.toml         # Project config: deps, python version, setuptools
├── docs/
│   ├── architecture/      # Hexagonal rules, layer boundaries, migration guidance
│   │   └── hexagonal-python.md
│   ├── workflows/         # SDD + ECC + Superpowers workflow, token efficiency
│   │   └── sdd-ecc.md
│   ├── security/          # Modern Python security baseline
│   │   └── python-security-baseline.md
│   ├── memory/            # Pluggable external memory conventions
│   │   └── external-memory.md
│   ├── decisions/         # Architecture Decision Records (ADRs)
│   │   └── README.md
│   └── templates/         # Official templates for new features
│       ├── SPEC_TEMPLATE.md
│       ├── PLAN_TEMPLATE.md
│       └── TASKS_TEMPLATE.md
├── src/
│   └── <package_name>/   # <-- RENAME this to your target package
│       ├── domain/        # Models, ports (Protocol/ABC), domain services, exceptions
│       │   └── __init__.py
│       ├── application/   # Use cases, DTOs. Depends only on domain + stdlib
│       │   └── __init__.py
│       └── infrastructure/ # outbound adapters, inbound entry points, config, composition root
│           ├── config.py
│           └── __init__.py
└── tests/                 # Unit tests, integration tests, evaluation suites
```

> **Important**: Replace `<package_name>` with your actual package name. Update all imports consistently across `domain/`, `application/`, and `infrastructure/`. See `AGENTS.md` for the mandatory rename workflow.

---

## Quick Start & Adoption

### 1. Clone the repository

```bash
git clone <your-repo-url> my-python-service
cd my-python-service
```

### 2. Set up Python environment & dependencies

```bash
# Create and activate a Python 3.12+ virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install project and dev dependencies
pip install -r requirements.txt  # or: pip install .[dev]
```

### 3. Rename / adapt the package

**Rename the package directory:**

```bash
# On Windows PowerShell
Rename-Item -Path "src\_example_package" -NewName "my_service"
# (resulting path: src/my_service)

# Or using mv (Git Bash / terminal)
mv src/_example_package src/my_service
```

**Update imports consistently:**

- Edit all files under `src/my_service/` to replace `_example_package` with `my_service` (or your chosen name)
- Update `pyproject.toml` if the package name/entry points change
- Ensure `src/my_service/__init__.py` has proper `__all__` exports

> **Tip**: Use `find`/`replace` across the codebase, but respect the hexagonal boundary: `application/` depends only on `domain/`, and `infrastructure/` depends on both. Don't cross dependency lines during rename.

### 4. Configure environment variables

Create a `.env` file (local dev only — never commit):

```
# Model & RAG
MODEL_ENDPOINT=https://your-model-endpoint.ai
EMBEDDING_DIM=768 or 2048
SIMILARITY_THRESHOLD=0.7

# Database / Vector store
VECTOR_PROVIDER=local  # or: redis, supabase, pinecone, qdrant
REDIS_URL=redis://localhost:6379

# Security — never commit these!
API_KEY=your-api-key-here
SECRET_KEY=your-secret-key-here
```

> **Security**: Add `.env` to `.gitignore`. Load values via `python-dotenv` or a dedicated secret manager (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault). Never store secrets in source code, `docs/`, logs, or external memory.

### 5. Start a feature with SDD + Worktree

```bash
# Create a git worktree for the feature/branch
git worktree add ../my-service-feature feature/DESARROLLO-2

# Or, the mandatory SDD flow:
# 1. Create docs/features/<feature>/
# 2. Copy templates from docs/templates/ into SPEC.md, PLAN.md, TASKS.md
# 3. Start development in the worktree
# 4. When done, merge and remove the worktree
```

> **Mandatory Feature Start Rule** (from AGENTS.md): Before starting any new feature, create `docs/features/<feature>/` and generate `SPEC.md`, `PLAN.md`, and `TASKS.md` from the templates in `docs/templates/`.

---

## Adopting Into a New vs. Existing Project

### Option A: Starting a New Project
1. Clone this repository and create a Python 3.12+ virtual environment.
2. Rename `src/_example_package` to `src/<your_package>`, update internal imports and `pyproject.toml`, and run baseline tests.
3. Copy `.env.example` to `.env` locally (never commit `.env` or secrets).
4. Create a `git worktree` for your first task, create `docs/features/<feature>/`, copy `SPEC_TEMPLATE.md`, `PLAN_TEMPLATE.md`, and `TASKS_TEMPLATE.md` from `docs/templates/`, and start iterating.

### Option B: Adding to an Existing Project (Incremental Adoption)
1. Copy `AGENTS.md` and `docs/` (`architecture/`, `workflows/`, `security/`, `memory/`, `decisions/`, `templates/`, and `features/`) into your existing repository without breaking current files or tests.
2. Update package/test path references in `AGENTS.md` if your project already uses a different directory layout.
3. Keep existing code working as-is; apply hexagonal separation (`domain/`, `application/`, `infrastructure/`) incrementally to new modules or extracted components rather than rewriting everything at once.
4. Align environment handling with your security baseline without exposing secrets in code, docs, logs, or external memory, and configure your preferred external memory backend (`Engram`, `Graphiti`, `claudemem`, or `Obsidian`).
5. For every new feature or refactor task, create a `git worktree` and initialize `docs/features/<feature>/` (`SPEC.md`, `PLAN.md`, `TASKS.md`) before changing production code.

---

## Configuration & Security Notes

### Secrets & Environment

- Load API keys, tokens, and credentials strictly from environment variables or a secret manager.
- Never store secrets in source code, `docs/`, logs, or external memory.
- Use `.env` only for local development — add it to `.gitignore`.
- Rotate credentials regularly; treat expired credentials as security incidents.

### Re-indexing / Schema Migrations

- When switching embedding providers or dimensions (e.g., moving between local `768`-dim embeddings with HNSW and remote `2048`-dim embeddings with exact search), plan a **clean migration/re-index** rather than mixing incompatible vectors.
- Update `docs/memory/external-memory.md` to reflect the new backend's conventions.
- Run re-index scripts before deploying with new vector schemas.

### Input & Resource Boundaries

- Validate external payloads and file paths (preventing path traversal).
- Enforce size limits on all payloads (JSON bodies, file uploads, query parameters).
- Set timeouts and concurrency semaphores for all external calls.
- Treat retrieved or LLM-generated text as untrusted input.

---

## Token-Efficiency Skills (`ponytail`, `caveman`)

- **Read `AGENTS.md` first**, then load only the `docs/` guide and active `docs/features/<feature>/` files (`SPEC.md`, `PLAN.md`, `TASKS.md`) needed for the current step.
- Use `ponytail` and `caveman` to keep context reads targeted and technical outputs concise while preserving layer rules, tests, and security checks.
- This project applies these skills directly to reduce token usage across context reads, status updates, and technical responses.

## Skills Reference (`ponytail`, `caveman`, `ECC`, `superpowers`)

How to obtain/activate these skills in your agent environment:

- **`ponytail`**: Lazy senior developer mode. Activated by default in this harness. Use `/ponytail` or prefix with `ponytail:` for concise, no-fluff technical responses. Levels: `lite`/`full`/`ultra`. Reduces token consumption by compressing outputs while preserving technical accuracy.

- **`caveman`**: Ultra-compressed communication mode. Activated with `/caveman` or `full`/`ultra` mode. Drops articles, filler, pleasantries, hedging. One-line comments: `location, problem, fix`. Reduces token usage ~75% while keeping full technical substance. Compress memory files with `/caveman-compress FILEPATH`.

- **`ECC`** (Everything Claude Code / harness engineering): The operating framework for this repository. Enforced through AGENTS.md, SDD flow (SPEC.md → PLAN.md → TASKS.md), ECC loop (plan → verify → implement → review → record), and mandatory session summaries via `mem_session_summary`. Read `AGENTS.md` §5 for the full flow.

- **`superpowers`** (subagents & git worktree isolation): Use a dedicated `git worktree` per feature/branch (`git worktree add ../<feature> <branch-name>`) to keep active iterations isolated from `main`. Delegate bounded, parallelizable subtasks to subagents using the `subagent` tool (e.g., test authoring, adapter wiring, security review). Each subagent runs with fresh context but integrates results cleanly into the main workspace.

**When cloning this repo**: Ensure your agent harness has these skills enabled. The `AGENTS.md` file serves as the operating framework — read it first before starting any feature. The `docs/workflows/sdd-ecc.md` guide covers the SDD + ECC + Superpowers workflow in detail.

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

### Migration Between Backends

- When switching from one backend to another (e.g., Engram → Graphiti), export existing data in a neutral format first.
- Update `docs/memory/external-memory.md` to reflect the new backend's conventions.
- Run migration scripts before cutting over; keep old data read-only during the transition period.

---

## Working with SDD + ECC + Superpowers

### 1. Create feature workspace

```bash
# From repo root, create the feature directory structure
mkdir -p docs/features/user-login

# Copy templates from docs/templates/ into the new feature folder
cp docs/templates/SPEC_TEMPLATE.md docs/features/user-login/SPEC.md
cp docs/templates/PLAN_TEMPLATE.md docs/features/user-login/PLAN.md
cp docs/templates/TASKS_TEMPLATE.md docs/features/user-login/TASKS.md
```

### 2. Work inside an isolated git worktree

```bash
git worktree add ../my-service-feature feature/DESARROLLO-2
# Or: git checkout -b feature/DESARROLLO-2
```

### 3. Delegate independent subtasks to subagents

Use subagents for bounded, parallelizable tasks such as:
- Test authoring
- Adapter wiring
- Security/boundary review
- Documentation generation

### 4. Run quality gates before marking tasks complete

- Unit tests passing
- Integration tests passing
- Architecture boundary check (hexagonal dependency rules)
- Security boundary check (inputs/paths/secrets validated)
- Type/lint check passing (black, ruff, mypy)

### 5. Definition of Done (DoD)

- **Feature Docs Ready**: `SPEC.md`, `PLAN.md`, and `TASKS.md` exist in `docs/features/<feature>/` and reflect actual decisions.
- **Architecture & Security Verified**: hexagonal dependency rules respected, inputs/paths/secrets checked, and required tests passing.
- **Tracked & Clean**: `TASKS.md` updated, key decisions/learnings recorded (in ADRs or external memory), and temporary worktrees cleaned up when merged.

---

## License

This project is licensed under the MIT License — see the `LICENSE` file (or add one) for details.

---

## References (required, from AGENTS.md)

- `docs/architecture/hexagonal-python.md`
- `docs/workflows/sdd-ecc.md`
- `docs/security/python-security-baseline.md`
- `docs/memory/external-memory.md`
- `docs/decisions/README.md`
- `docs/templates/SPEC_TEMPLATE.md`
- `docs/templates/PLAN_TEMPLATE.md`
- `docs/templates/TASKS_TEMPLATE.md`
- `README.md`
- `AGENTS.md`