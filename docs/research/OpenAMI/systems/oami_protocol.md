# OAMI Protocol Specification

The Open AMI (OAMI) protocol standardizes communications between orchestrated agents, the compliance backend, and ancillary services, extending recent work on multi-agent coordination for LLM applications.[^autogen]

## Objectives

- Provide a transport-agnostic interface for task orchestration, knowledge sharing, and compliance evidence exchange.
- Ensure every interaction emits auditable metadata aligned with the Compliance Manifest.[^nist-ai-rmf]

## Core Concepts

- **Sessions** — logical conversations bound to manifest directives and risk context.
- **Tasks** — units of work annotated with compliance requirements and evidence hooks.
- **Knowledge Objects** — structured artefacts exchanged between agents; include provenance hashes.

## Methods

| Method | Purpose | Status |
|--------|---------|--------|
| `task.create` | Register new work with manifest linkage | Planned |
| `task.submit_evidence` | Upload evidence blobs for directive checks | Future |
| `knowledge.query` | Retrieve knowledge graph entries respecting access control | Research |
| `compliance.signal` | Report SDS runtime events to backend monitors | Planned |

## Transport and Security

- Encourages gRPC/HTTP/WS implementations with mutual TLS.
- Requires integration with SDS cryptographic primitives (signatures, attestations).[^zkml]

## Relation to Base Module

- Reuses FastMCP patterns (`base/backend/mcp/`) for message framing and authentication.
- Compliance MCP (`compliance/backend/mcp/`) will expose a subset of OAMI methods with compliance-centric guards.

## Development Notes

- Start with internal API definitions inside `compliance/backend/protocol/` (**Planned**).
- Align request/response schemas with consolidated evidence requirements and audit logging expectations.

### References

[^autogen]: Qian Liu et al. “AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.” *arXiv preprint* arXiv:2308.08155, 2023. https://arxiv.org/pdf/2308.08155.pdf.

[^nist-ai-rmf]: National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (NIST AI 100-1)*, 2023. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf.

[^zkml]: Mohit Kumar et al. “A Survey of Zero-Knowledge Proof Based Verifiable Machine Learning.” *arXiv preprint* arXiv:2502.18535, 2025. http://arxiv.org/pdf/2502.18535v1.
