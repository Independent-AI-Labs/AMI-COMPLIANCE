# Secure Distributed System (SDS)

The SDS is the technical foundation that enforces Integrity and Compliance guarantees across distributed workloads.

## Purpose

- Provide cryptographically verifiable execution, storage, and messaging.
- Supply runtime telemetry to the compliance backend for continuous assurance.

## Key Components

1. **Trusted Execution Layer** — enclaves/isolated runtimes capable of attestation (**Research**; evaluate integration with `nodes/` orchestrations).[^scone]
2. **Immutable Logging** — already available through `base/backend/dataops/security/audit_trail.py`; extend to compliance events (**Planned**).
3. **Compliance State Transition Engine** — validates every state change against the Compliance Manifest (future `compliance/backend/runtime/state_engine.py`).
4. **Monitoring and Response Loop** — anomaly detection + automated mitigations tied to Articles 72–73 reporting workflows.[^eu-ai-act]

## Cryptographic Tooling

- Utilises hashing, signatures, and optional zero-knowledge proofs for evidence packaging (aligns with `COMPLIANCE_BACKEND_SPEC.md` cryptography requirements).[^zkml]
- Future evaluation of zkML and verifiable computation stacks (**Research**).

## Implementation Roadmap

| Milestone | Description | Status |
|-----------|-------------|--------|
| SDS Adapter | Wrap existing base audit trail + messaging for compliance backend | Planned |
| Attestation MVP | Add host identity verification in `nodes/` setup scripts | Research |
| Incident Pipeline | Wire anomaly detections to compliance MCP with Article 73 timers | Future |

Corresponding consolidated guidance: see `consolidated/EU_AI_Act/high_risk_ai_systems/requirements/risk_management_system/` for risk controls and `consolidated/ISO_27001/operations/` for logging and monitoring expectations.

### References

[^scone]: Sergei Arnautov et al. “SCONE: Secure Linux Containers with Intel SGX.” *Proceedings of the 26th Symposium on Operating Systems Principles (SOSP)*, 2016. https://arxiv.org/pdf/1703.04387.pdf.

[^eu-ai-act]: European Parliament and Council. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence* (EU AI Act), 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689.

[^zkml]: Mohit Kumar et al. “A Survey of Zero-Knowledge Proof Based Verifiable Machine Learning.” *arXiv preprint* arXiv:2502.18535, 2025. http://arxiv.org/pdf/2502.18535v1.
