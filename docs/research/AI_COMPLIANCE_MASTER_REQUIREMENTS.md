# AI Compliance Master Requirements Document
## AMI-ORCHESTRATOR Platform Compliance Framework

**Document Version:** 2.0  
**Last Updated:** September 26, 2025  
**Maintainer:** Compliance Working Group  

This document captures the authoritative compliance requirements for AMI-ORCHESTRATOR and maps them to consolidated source material, current implementation artefacts, and backlog items for the forthcoming `compliance/backend` build-out.

---

## 1. Regulatory Landscape & Canonical References

| Framework | Canonical Source | Consolidated Docs | Implementation Snapshot |
|-----------|-----------------|-------------------|-------------------------|
| **EU AI Act (Regulation 2024/1689)** | EUR-Lex 32024R1689 | `consolidated/EU_AI_Act/**` | Logging & audit trail implemented in `/base` (`audit_trail.py`); deployer/provider obligations tracked in docs; dedicated deployer tooling pending in `compliance/backend`. |
| **ISO/IEC 42001:2023 (AIMS)** | ISO Catalogue 81230 | `consolidated/ISO_42001/**` | Context/support/performance/improvement clauses mapped; operational controls will be surfaced through the compliance backend services. |
| **ISO/IEC 27001:2022 (ISMS)** | ISO Catalogue 82875 | `consolidated/ISO_27001/**` | Base module supplies ISMS primitives (RBAC, audit, storage controls). Risk treatment approvals and evidence tracking must be implemented in `compliance/backend`. |
| **NIST AI RMF 1.0** | NIST AI.100-1 | `consolidated/NIST_AI_RMF/**` | Governance/Map/Measure text consolidated; tooling to expose RMF posture is part of the Compliance MCP roadmap. |
| **NIST RMF (SP 800-37r2)** | NIST SP 800-37r2 | `consolidated/NIST_RMF/**` | Alignment documented; requires automation once compliance backend exists. |

Supporting standards (ISO/IEC 23894, ISO/IEC 23053, etc.) are catalogued in `COMPLIANCE_STANDARDS_CATALOG.md` and will inform future control expansions.

---

## 2. Core Requirement Sets

### 2.1 EU AI Act – High-Risk AI Systems

- **Scope Classification:** High-risk (education/vocational training use cases).
- **Key Articles & Status:**
  - **Article 9 (Risk Management):** Methodology defined in `consolidated/.../risk_management_system.md`; implementation pending `risk_service.py` in compliance backend.
  - **Article 12 (Logging):** Implemented via `base/backend/dataops/security/audit_trail.py`; needs compliance-facing APIs for review/export.
  - **Article 26 (Deployers):** Obligations updated in consolidated docs; enforcement tooling to be exposed by Compliance MCP (`get_control`, `list_gaps`).
  - **Article 72-73 (Post-Market Monitoring & Incident Reporting):** Requirements refined in consolidated docs; backend must capture incidents and deadlines (see `COMPLIANCE_BACKEND_SPEC.md`).

### 2.2 ISO/IEC 42001 – AI Management System

- Clauses 4–10 summarised in `consolidated/ISO_42001/**` after the latest editorial pass.
- Backend needs to register: context records, competence evidence (`support` clause), management review minutes, nonconformity logs (Clause 10.2 updates).

### 2.3 ISO/IEC 27001 – Information Security Management

- Clause 6 risk treatment updates (risk owner approval) captured in `consolidated/ISO_27001/planning/planning.md`.
- Compliance backend must surface SoA status, residual risk approvals, and evidence mapping.

### 2.4 NIST AI RMF & NIST RMF

- Consolidated content details Map/Measure/Manage & Prepare/Categorize/Select/... steps.
- Compliance MCP should expose KPIs and gap reports referencing these functions.

---

## 3. Implementation Responsibilities

| Area | Owner | Current Assets | Needed Enhancements |
|------|-------|----------------|---------------------|
| **Data capture & auditability** | Base | `audit_trail.py`, DataOps DAO factories | Expose compliance-specific repositories via `compliance/backend/repositories`. |
| **Control catalogue** | Compliance | Consolidated docs, Blueprint mappings | Seed control models and status store, maintain authoritative list of control IDs. |
| **Risk & incident workflow** | Compliance | None | Implement `risk_service.py`, integrate Article 73 deadlines, tie into audit trail. |
| **Evidence management** | Compliance | None | Provide evidence submission & validation pipeline aligned with ISO/IEC 27001 Clause 7.2 documentation requirements. |
| **MCP tooling** | Compliance + Base | `base/backend/mcp/*` for reference | Build `compliance/backend/mcp/compliance_server.py` per spec. |

---

## 4. Compliance Delivery Backlog (Extract)

The following backlog items anchor our execution. Full details live in `COMPLIANCE_GAP_ANALYSIS.md` and `EXECUTIVE_ACTION_PLAN.md`.

1. **Backend Scaffolding (Sprint 1)** – Create `compliance/backend/` package, config, and model skeletons.
2. **Control Catalogue Loader** – Parse consolidated docs to seed control definitions (ISO 42001, ISO 27001, EU AI Act obligations, Blueprint controls).
3. **MCP Server MVP** – Implement `compliance_server.py` with `get_control` + `list_gaps` tools backed by static data.
4. **Evidence Workflow** – Deliver `submit_evidence` + audit logging integration.
5. **Risk & Incident Tracking** – Implement Article 73 support with 15/10/2-day reminders.
6. **Audit Packet Generation** – Build `export_audit_packet` aggregator for external reporting.

---

## 5. Reporting & Review Cadence

- **Weekly:** Update `CURRENT_IMPLEMENTATION_STATUS.md` with sprint burndown and MCP tool progress.
- **Bi-weekly:** Refresh `COMPLIANCE_GAP_ANALYSIS.md` as controls move to `OPERATIONAL` or `EVIDENCE_REQUIRED`.
- **Monthly:** Run management review per ISO/IEC 42001 Clause 9.3 and document outputs in the compliance backend once available.

---

This master requirements document is authoritative for scope and traceability. Changes to regulatory interpretations must first land in `compliance/docs/consolidated`, then propagate here via explicit status updates.
