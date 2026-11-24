# Modern Python Security Baseline

This document defines the modern Python security baseline for this repository. All code must adhere to these guidelines.

## 1. Secrets & Credentials

- **Never** hardcode API keys, tokens, passwords, or certificates in source code.
- Load all secrets from environment variables or a secret manager (e.g., AWS Secrets Manager, Azure Key Vault, HashiCorp Vault).
- Use `python-dotenv` only for local development — never commit `.env` files.
- Rotate credentials regularly; treat expired credentials as security incidents.

## 2. Input Validation

- Validate ALL external inputs (HTTP payloads, file paths, user uploads, database results).
- Prevent path traversal: sanitize and restrict paths used with `open()`, `os.path`, `pathlib`.
- Enforce size limits on all payloads (JSON bodies, file uploads, query parameters).
- Treat retrieved/LLM-generated text as untrusted input.

## 3. Error Handling & Logging

- Never expose stack traces, internal paths, or database details in HTTP error responses.
- Use structured logging (e.g., `structlog` or `logging` with JSON format).
- Mask or omit sensitive data from log output (API keys, PII, passwords).
- Log security-relevant events (auth failures, authorization violations, input validation errors).

## 4. Dependency Management

- Pin dependency versions in `requirements.txt`/`pyproject.toml`; use `pip-audit` regularly.
- Avoid pinning to exact `==` versions for major deps; use `~=` or `>=` with periodic updates.
- Remove unused dependencies promptly.
- Lockfile must be committed (e.g., `requirements-lock.txt` or `poetry.lock`).

## 5. Concurrency & Resource Boundaries

- Use bounded concurrency (semaphores, connection pool limits).
- Set timeouts for all external calls (HTTP, DB, message queues).
- Validate thread-safe access to shared state.
- Reject requests exceeding resource limits (payload size, computation time).

## 6. API Security

- Use HTTPS for all external communications.
- Implement authentication middleware (e.g., OAuth2, JWT) at the inbound adapter layer.
- Authorize every request — don't assume authenticated = authorized.
- Rate-limit endpoints exposed to external clients.

## 7. Data Protection

- Encrypt sensitive data at rest (using `cryptography` or KMS-backed solutions).
- Use parameterized queries — never interpolate values into SQL strings.
- Hash passwords with Argon2 or bcrypt (never store plaintext passwords).
- Handle personal data per applicable privacy regulations (GDPR, CCPA, etc.).

## 8. Environment Isolation

- Development, staging, and production must use separate configuration.
- Never lower security defaults for "convenience" in any environment.
- Feature flags must be validated before enabling/disabling.
