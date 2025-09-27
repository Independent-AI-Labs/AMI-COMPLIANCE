# Compliance Module Code Quality Snapshot

- **Implementation status:** Documentation-only. All executable compliance features
  (audit trail, evidence storage, MCP tooling) live in `/base`.
- **Checks in use:** Inherits the orchestrator pre-commit stack (ruff, ruff-format,
  mypy, pytest). No module-specific exemptions remain.
- **Outstanding work:** Implement the `/compliance/backend` services described in
  `docs/research/COMPLIANCE_BACKEND_SPEC.md` and add targeted tests once code ships.
- **Deviation policy:** Any new asset that does not follow `/base` patterns should be
  placed under `docs/research/` with a clear "research" label until it is production-ready.

No further code-quality tracking is needed until the backend exists.
