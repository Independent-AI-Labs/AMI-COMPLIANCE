# Executive Action Plan for AI Compliance
## AMI-ORCHESTRATOR Platform

**Last Updated:** September 26, 2025  
**Audience:** Executive sponsors, Compliance WG, Engineering leads

---

## 1. Situation Overview

- Regulatory obligations for EU AI Act, ISO/IEC 42001, ISO/IEC 27001, and NIST AI RMF are consolidated in `compliance/docs/consolidated`.
- `/base` delivers foundational infrastructure (DataOps, audit trail, MCP framework) but `/compliance` contains no runtime code.
- `COMPLIANCE_BACKEND_SPEC.md` defines the target architecture for the compliance backend and pluggable MCP server.

**Risk:** Without the backend, we cannot evidence compliance nor surface Article 73 incident timelines or ISO management review records.

---

## 2. Immediate Actions (Next 30 Days)

| Week | Owner | Outcome | Notes |
|------|-------|---------|-------|
| Week 1 | Compliance Engineering | Scaffold `compliance/backend` (config, models, repositories) per spec | Use Base module patterns (Pydantic models, DAO factory). |
| Week 2 | Compliance Engineering | Seed control catalogue from consolidated docs; wire Base audit logging helpers | Validate hashes/IDs against documentation. |
| Week 3 | Compliance + QA | Deliver MCP MVP (`get_control`, `list_gaps` tools) with contract tests | Extend `FastMCPServerBase`; smoke through module setup harness. |
| Week 4 | Compliance + QA | Author unit/integration tests; document deployment steps in module README | No release before pytest suite passes locally. |

---

## 3. 90-Day Strategic Plan

### Month 1 – Foundation
- Backend scaffolding & control loader complete.
- Read-only MCP tooling available to pull requirements/gap lists.
- Documentation updated (`CURRENT_IMPLEMENTATION_STATUS.md`, `SUBMODULE_COMPLIANCE_PLANS.md`).

### Month 2 – Evidence & Risk Automation
- Implement evidence submission workflow, residual risk approvals, Article 73 deadline tracking.
- Integrate MCP write tools with Base audit trail.
- Connect module setup scripts to compliance MCP for automatic evidence registration (where feasible).

### Month 3 – Reporting & External Readiness
- Deliver `export_audit_packet` to generate regulator-facing bundles.
- Run ISO/IEC 42001 management review and EU AI Act post-market simulations using the new backend.
- Prepare for pre-assessment audit (internal) leveraging MCP outputs.

---

## 4. Resourcing & Budget

- **Team:** 4 engineering FTE (backend + QA) + 1 compliance analyst for control mapping.
- **Budget Envelope:** €250k – €300k (dev effort, standards acquisition, audit preparation).
- **Dependencies:** Storage infrastructure (PostgreSQL/Dgraph) provisioned, Base team available for integration support.

---

## 5. Governance & Reporting

- Weekly status sync with executive sponsor; update this document and `COMPLIANCE_GAP_ANALYSIS.md`.
- Bi-weekly demo of MCP capabilities to stakeholders.
- Monthly checkpoint against consolidated requirements, ensuring documentation and backend stay aligned.

---

Escalate blockers (infrastructure, staffing, regulatory interpretation) immediately to the Compliance Working Group for resolution.
