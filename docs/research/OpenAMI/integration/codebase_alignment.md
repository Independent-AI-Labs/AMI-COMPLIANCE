# Codebase Alignment

This matrix links Open AMI capabilities to existing, planned, and future components within AMI-Orchestrator, following guidance on regulated DevOps transformations and risk-managed system engineering.[^devops-iso][^nist-800-37]

| Open AMI Capability | Code Location | Status | Notes |
|---------------------|---------------|--------|-------|
| Immutable Compliance Logging | `base/backend/dataops/security/audit_trail.py` | Operational | Extend to emit manifest-aware events. |
| Compliance Manifest Loader | `compliance/backend/loader/` (new) | Planned | Transforms consolidated docs into manifest objects. |
| Policy Validation Engine | `compliance/backend/policy_validator.py` (new) | Planned | Resolves conflicts; depends on consolidated clause metadata. |
| Compliance MCP Server | `compliance/backend/mcp/` (new) | Planned | Reuses FastMCP stack from `base/backend/mcp/`. |
| Evidence Registry Service | `compliance/backend/evidence_service.py` (new) | Future | Stores artefacts from OAMI protocol submissions. |
| Risk Management Service | `compliance/backend/risk_service.py` (new) | Future | Implements ISO/IEC 27001 Clause 6.1.3 workflow. |
| SDS Monitoring Adapters | `compliance/backend/runtime/` (new) | Future | Subscribes to base telemetry; triggers incident workflows. |
| OAMI Protocol Schemas | `compliance/backend/protocol/` (new) | Planned | Align with architecture specification. |
| Simulation Gateway | `compliance/backend/simulation_gateway.py` (new) | Research | Bridges OASIM to compliance MCP. |
| Knowledge Graph Storage | `base/backend/graph/` (new) | Research | Needed for Cognitive Mapping evidence. |
| UX Compliance Reporting | `ux/` (existing) | Pending Review | Out of scope until UX documentation stabilized. |

Keep this table updated as implementations land. Tag incomplete rows with **Research** or **Planned** to match roadmap terminology used in `CURRENT_IMPLEMENTATION_STATUS.md` and `EXECUTIVE_ACTION_PLAN.md`.

### References

[^devops-iso]: Nilay Karat et al. “DevOps in an ISO 13485 Regulated Environment: A Multivocal Literature Review.” *arXiv preprint* arXiv:2007.11295, 2020. http://arxiv.org/pdf/2007.11295v1.

[^nist-800-37]: National Institute of Standards and Technology. *Risk Management Framework for Information Systems and Organizations (NIST SP 800-37 Rev. 2)*, 2018. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-37r2.pdf.
