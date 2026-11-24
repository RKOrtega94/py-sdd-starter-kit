# Hexagonal Architecture (Ports & Adapters) for Python

This document defines the hexagonal architecture rules, layer boundaries, and migration/re-index guidance for this repository.

## 1. Layer Structure

### 1.1 `domain/` — Core Domain Layer

- **Responsibilities**: Entity models, value objects, domain ports (Protocol/ABC), domain services, domain exceptions.
- **Dependencies**: NO web frameworks, DB drivers, third-party SDKs, or `os.environ`.
- **Rules**: Pure Python, testable in isolation, framework-agnostic.

### 1.2 `application/` — Application Layer

- **Responsibilities**: Use cases, DTOs, orchestrates domain layer, applies business rules.
- **Dependencies**: Depends only on `domain/` and standard library/typing.
- **Rules**: No framework code, no DB access, no external SDKs.

### 1.3 `infrastructure/` — Infrastructure Layer

- **Sub-divisions**:
  - `outbound/`: Adapters for external systems (DB, APIs, message queues, file systems).
  - `inbound/`: Entry points (FastAPI/Flask controllers, CLI commands).
  - `config/`: Configuration loading, environment variable handling (validated only).
  - `composition_root/`: Wiring/assembly of ports and adapters.

### 1.4 `tests/` — Test Layer

- Unit tests for domain, application, and infrastructure.
- Integration tests testing use cases end-to-end.
- Evaluation suites for RAG/service integration.

## 2. Dependency Rules

- `domain/` ← depends on nothing external
- `application/` ← depends on `domain/` + standard library
- `infrastructure/` ← depends on `domain/` and `application/`
- NO circular dependencies allowed

## 3. Ports (Interfaces) in `domain/`

- Define `Protocol`/ABC interfaces for all external dependencies.
- Example:

  ```python
  from typing import Protocol
  
  class UserRepository(Protocol):
      def get_by_id(self, user_id: str) -> User: ...
      def save(self, user: User) -> None: ...
  ```

## 4. Adapter Implementation in `infrastructure/`

- Implement the ports defined in `domain/` using concrete frameworks/drivers.
- Keep adapter code thin; delegation to domain services.

## 5. Migration & Re-Index Guidance

- When switching embedding providers/dimensions: plan clean migration, NOT mixed vectors.
- Update `docs/memory/external-memory.md` for backend-specific conventions.
- Run re-index scripts before deploying with new vector schemas.

## 6. Entry Point Pattern (inbound adapters)

- FastAPI/Flask apps should be thin, delegating to application use cases.
- Use dependency injection at composition root.

## 7. Configuration Handling

- Load from environment variables only in `infrastructure/config/`.
- Validate all inputs; never trust `os.environ` directly.
- Use pydantic-style validation with explicit error handling.
