# AMI-ORCHESTRATOR Compliance Documentation Suite

## Overview
This directory curates the living compliance programme for AMI-ORCHESTRATOR. The canonical regulatory requirements live under `./consolidated/`, while the surrounding Markdown tracks platform commitments, delivery status, and implementation guidance. The `compliance` Python module currently contains documentation only; all operational primitives (audit trail, DataOps storage, MCP infrastructure) sit in `/base` and must be wired in via the new backend specification.

**Current Reality (September 2025 snapshot)**
- `/base` supplies blockchain-backed audit logging, DataOps storage orchestration, and existing MCP servers.
- `/compliance` lacks runtime code. A backend and pluggable Compliance MCP server need to be implemented following `COMPLIANCE_BACKEND_SPEC.md`.
- Consolidated requirements for EU AI Act, ISO/IEC 42001, ISO/IEC 27001, and NIST AI RMF are authoritative in `./consolidated/`.

## Key Documents

- `AI_COMPLIANCE_MASTER_REQUIREMENTS.md` – Canonical requirements catalogue mapped to consolidated docs and platform artefacts.
- `COMPLIANCE_GAP_ANALYSIS.md` – Outstanding control gaps with remediation owners and priority.
- `CURRENT_IMPLEMENTATION_STATUS.md` – Reality check against the codebase (Base, Browser, upcoming Compliance backend).
- `EXECUTIVE_ACTION_PLAN.md` – Rolling 90-day plan for resourcing and milestones.
- `SUBMODULE_COMPLIANCE_PLANS.md` – Module-level expectations, including the `/compliance/backend` build-out.
- `COMPLIANCE_BACKEND_SPEC.md` – Technical spec for the new backend and MCP server.
- `STANDARDS_TO_ACQUIRE.md` – Purchase/download tracker for standards not embedded in the repo.
- `COMPLIANCE_STANDARDS_CATALOG.md` – High-level overview with links back to consolidated references.

## How to Use This Folder

1. **Start with the consolidated library** to understand regulatory obligations (`./consolidated`).
2. **Review the backend spec** (`COMPLIANCE_BACKEND_SPEC.md`) to align engineering work with Base module patterns.
3. **Prioritise remediation** via `COMPLIANCE_GAP_ANALYSIS.md` and `EXECUTIVE_ACTION_PLAN.md`.
4. **Update status reports** (`CURRENT_IMPLEMENTATION_STATUS.md`, `SUBMODULE_COMPLIANCE_PLANS.md`) as code lands in `/compliance/backend`.

## Delivery Roadmap (Draft)

| Phase | Focus | Target Outputs |
|-------|-------|----------------|
| Sprint 1 | Backend scaffolding | `compliance/backend/` package, control/evidence models, repository stubs |
| Sprint 2 | MCP MVP | `compliance_server.py` with `get_control` / `list_gaps` tools and DataOps wiring |
| Sprint 3 | Evidence + Risk | `submit_evidence`, Article 73 workflow, audit logging integration |
| Sprint 4 | Audit packet + rollout | `export_audit_packet`, seeding from consolidated docs, module tests & README updates |

Targets and percentages will be refreshed after each sprint once the backend lands in `main`.
