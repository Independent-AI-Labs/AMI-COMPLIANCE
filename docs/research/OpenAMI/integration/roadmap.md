# Implementation Roadmap

The roadmap aligns Open AMI theory with the staged delivery plan captured in `CURRENT_IMPLEMENTATION_STATUS.md`, reflecting phased compliance adoption patterns recommended in regulated DevOps studies and AI risk-management frameworks.[^devops-iso][^nist-ai-rmf]

## Sprint 1 – Backend Foundations

- Scaffold `compliance/backend/` packages listed in `codebase_alignment.md`.
- Build manifest loader MVP sourcing consolidated docs.
- Expose manifest state through temporary CLI tools for validation (**Planned**).

## Sprint 2 – Compliance MCP MVP

- Implement read-only MCP endpoints (`manifest.get`, `controls.list`).
- Integrate base audit trail exporter for immutable records.
- Draft API docs referencing OAMI protocol fields.

## Sprint 3 – Evidence and Risk Services

- Add evidence ingestion flows with storage metadata for audit.
- Implement risk treatment approvals to satisfy ISO/IEC 27001 Clause 6.1.3.
- Begin SDS anomaly subscription for incident pre-alerts.

## Sprint 4 – Automation and Simulation

- Wire incident pipeline to Article 73 template generator.
- Pilot OASIM scenarios feeding compliance MCP for robustness checks.
- Generate compliance dashboards summarizing manifest coverage (**Future**).

Use this roadmap when prioritizing engineering work; update milestones as deliverables complete or scope shifts.

### References

[^devops-iso]: Nilay Karat et al. “DevOps in an ISO 13485 Regulated Environment: A Multivocal Literature Review.” *arXiv preprint* arXiv:2007.11295, 2020. http://arxiv.org/pdf/2007.11295v1.

[^nist-ai-rmf]: National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (NIST AI 100-1)*, 2023. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf.
