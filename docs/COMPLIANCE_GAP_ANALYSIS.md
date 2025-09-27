# Compliance Gap Analysis & Remediation Plan
## AMI-ORCHESTRATOR Platform

**Document Version:** 2.0**  
**Last Updated:** September 26, 2025  
**Classification:** Internal

This analysis reflects the post-consolidation view of regulatory requirements and highlights the work needed to operationalise the compliance backend and MCP server.

---

## 1. High-Priority Gaps

| Gap ID | Requirement Source | Description | Current State | Target Remediation | Priority |
|--------|--------------------|-------------|---------------|--------------------|----------|
| GAP-AI-001 | EU AI Act Article 9 (`consolidated/eu_ai_act/high_risk_ai_systems/requirements/risk_management_system/risk_management_system.md`) | Lifecycle risk management workflow | No dedicated service or datastore; only audit trail primitives in `/base` | Implement `risk_service.py` + DAO + MCP reporting (per `COMPLIANCE_BACKEND_SPEC.md`) | P0 |
| GAP-AI-002 | EU AI Act Articles 72-73 (`.../post_market_monitoring/post_market_monitoring.md`) | Post-market monitoring + serious incident reporting | Logging exists in `/base`; no deployer/provider interfaces or deadline tracking | Add incident models, notifications, and MCP export tooling | P0 |
| GAP-ISO42001-003 | ISO/IEC 42001 Clause 7.2 & 9.3 (`consolidated/ISO_42001/support/support.md`, `.../performance_evaluation/performance_evaluation.md`) | Competence evidence retention & management review artefacts | No system of record; tracked in ad-hoc docs | Backfill evidence service with storage for competence records and management review minutes | P1 |
| GAP-ISO27001-004 | ISO/IEC 27001 Clause 6.1.3 (`consolidated/ISO_27001/planning/planning.md`) | Risk treatment approval by risk owners | Missing workflow to capture approvals/residual risk acceptance | Extend control/risk models + MCP tool to document approvals | P1 |
| GAP-NIST-005 | NIST AI RMF Manage 4 (`consolidated/NIST_AI_RMF/manage/manage.md`) | Continuous monitoring metrics surfaced to operators | No dashboard/API; insights only in Markdown | Build `list_gaps` + `export_audit_packet` responses with NIST-aligned metrics | P2 |

---

## 2. Secondary Gaps & Housekeeping

- **Evidence Traceability:** Consolidated docs reference evidence expectations, but there is no structured storage or link to Git commits/logs. Addressed by `EvidenceService` (Sprint 3).
- **Control Catalogue Governance:** No seed process for importing consolidated control lists into runtime data. Requires loader during backend scaffolding.
- **Module Status Reporting:** `CURRENT_IMPLEMENTATION_STATUS.md` manually curated; needs automation via MCP server once backend exists.
- **Obsolete Docs:** Legacy references to non-existent validators removed; remaining documents updated to point to `compliance/backend` spec.

---

## 3. Remediation Roadmap (Aligned with Backend Spec)

| Sprint | Focus | Key Deliverables | Dependencies |
|--------|-------|------------------|--------------|
| Sprint 1 | Backend scaffolding | `compliance/backend` package, config, models, DAO stubs, control catalogue loader | Consolidated docs ready (done) |
| Sprint 2 | MCP MVP | `compliance_server.py` (`get_control`, `list_gaps`), integration with Base audit logging | Backend scaffolding |
| Sprint 3 | Evidence & Risk | `EvidenceService`, `submit_evidence`, risk lifecycle + Article 73 tracking | Sprint 2 tools |
| Sprint 4 | Audit packet + automation | `export_audit_packet`, SoA/risk approval workflows, automated status updates | Evidence + risk services |

Testing and documentation updates must accompany every sprint; no production deployment before MCP contract tests and integration tests pass.

---

## 4. Tracking & Review

- **Weekly Stand-up:** Validate progress against sprint deliverables and update `CURRENT_IMPLEMENTATION_STATUS.md`.
- **Bi-weekly Gap Grooming:** Confirm priority levels, owners, and due dates, recording changes back into this file.
- **Monthly Management Review:** Ensure ISO/IEC 42001 Clause 9.3 evidence is captured (temporary in Markdown until backend available).

---

Contact the Compliance Working Group for clarifications before changing gap priorities or interpretations.
