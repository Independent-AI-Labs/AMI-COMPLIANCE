# Core Pillars

Open AMI is organized around four pillars that bind theoretical guarantees to compliance outcomes, mirroring contemporary regulatory and safety scholarship.[^eu-ai-act][^concrete]
Each pillar references obligations tracked in `compliance/docs/research/consolidated/`.

## Compliance

- Governs legal, ethical, and policy constraints. Encapsulated via the Compliance Manifest (see `../systems/compliance_manifest.md`).
- Supports EU AI Act Article 26 deployer duties and ISO/IEC 42001 Clause 6 orchestration by requiring explicit control objectives and evidence trails.[^eu-ai-act]
- Interfaces with the planned compliance backend (`compliance/backend` — **Future Implementation**) through policy evaluation services and MCP tooling.

## Integrity

- Ensures data, model, and execution fidelity. Builds on cryptographic attestations and immutable logging.[^scone]
- Leverages existing `base/backend/dataops/security/audit_trail.py` functionality (see `../../integration/codebase_alignment.md`).
- Ties into ISO/IEC 27001 Annex A.12 logging controls and consolidated risk management requirements.

## Abstraction

- Provides explainability, transparency, and controllable complexity through layered representations.[^cbm]
- Drives human oversight interfaces and cognitive mapping techniques. Marked **Research** until the simulator and knowledge graph services are available.
- Satisfies consolidated EU AI Act transparency provisions when paired with explainability tooling.

## Dynamics

- Handles adaptive behaviour, continual learning, and runtime governance.[^concrete]
- Requires monitoring loops (SDS runtime monitors) and policy hooks for post-market monitoring.
- Currently **Research**; engineering work will land in the compliance backend incident and adaptation services.

### References

[^eu-ai-act]: European Parliament and Council. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence* (EU AI Act), 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689.

[^scone]: Sergei Arnautov et al. “SCONE: Secure Linux Containers with Intel SGX.” *Proceedings of the 26th Symposium on Operating Systems Principles (SOSP)*, 2016. https://arxiv.org/pdf/1703.04387.pdf.

[^cbm]: K. Koh et al. “Concept Bottleneck Models.” *Proceedings of ICML 2020*. https://arxiv.org/pdf/2007.04612.pdf.

[^concrete]: Dario Amodei et al. “Concrete Problems in AI Safety.” *arXiv preprint* arXiv:1606.06565, 2016. https://arxiv.org/pdf/1606.06565.pdf.
