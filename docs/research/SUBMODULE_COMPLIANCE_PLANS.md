# Submodule-Specific Compliance Implementation Plans
## AMI-ORCHESTRATOR Detailed Module Analysis

**Document Version:** 2.0**  
**Last Updated:** September 26, 2025  
**Classification:** Internal

---

## 1. Base Module (`/base`)

**What Exists**
- Blockchain-backed audit chain (`backend/dataops/security/audit_trail.py`).
- DataOps DAO factory and storage configuration (PostgreSQL, Dgraph, etc.).
- MCP infrastructure using `FastMCPServerBase` (DataOps, SSH servers).

**Actions for Compliance Alignment**
- Expose reusable DAO helpers for compliance repositories (shared configuration).
- Provide sample tests/utilities that compliance backend can import.
- Document integration hooks for audit exports once compliance server is live.

---

## 2. Compliance Module (`/compliance`)

**Target Structure**
- Implement `compliance/backend/` per `COMPLIANCE_BACKEND_SPEC.md` (config, models, repositories, services, MCP tooling).
- Follow Base patterns: Pydantic models, DAOFactory usage, FastMCPServerBase inheritance.

**Key Deliverables**
1. Control catalogue loader linking consolidated docs to runtime data.
2. Evidence registry with audit logging.
3. Risk and incident workflow covering EU AI Act Article 73 timelines.
4. Compliance MCP server exposing `get_control`, `list_gaps`, `submit_evidence`, `export_audit_packet` tools.

**Dependencies**
- Consolidated documents kept current (already in place).
- Storage backend credentials and secrets configured via `.env` and `compliance/default.env`.

---

## 3. Browser Module (`/browser`)

**Current Controls**
- Session/profile isolation documented in module README.

**Planned Compliance Integration**
- Register isolation evidence (test logs, config snapshots) using `submit_evidence` once available.
- Automate MCP calls within module setup or CI to keep evidence fresh.

---

## 4. Files Module (`/files`)

**Current Controls**
- File-system MCP server with logging.

**Planned Compliance Integration**
- Provide storage integrity evidence (hash checks, access logs) via compliance backend.
- Map controls to ISO/IEC 27001 Annex A references surfaced in consolidated docs.

---

## 5. Domains, Nodes, Streams, UX Modules

- Each module has a setup contract referencing `/docs/Setup-Contract.md`. Once compliance MCP exists, these modules must:
  - Publish environment hardening evidence (configs, test results).
  - Update setup contracts to reference compliance MCP tooling rather than manual steps.

---

## 6. Timeline Alignment

| Sprint | Modules Impacted | Deliverables |
|--------|------------------|-------------|
| Sprint 1 | Compliance | Backend scaffolding, control loader |
| Sprint 2 | Compliance + Base | MCP MVP, audit hook integration |
| Sprint 3 | Compliance + Browser/Files | Evidence submissions, risk workflow pilots |
| Sprint 4 | Compliance + All modules | Automated audit packet, evidence automation |

Module owners must coordinate with the Compliance WG to ensure evidence expectations are met once the MCP workflows are rolled out.
