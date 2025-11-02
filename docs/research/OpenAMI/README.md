# Open AMI Research Dossier

> **⚠️ RESEARCH FRAMEWORK**: These documents describe **theoretical research concepts**. The Open AMI framework is not implemented in AMI-ORCHESTRATOR. See `/docs/openami/` for the main research vision and implementation status.

The Open AMI framework is a theoretical blueprint for delivering demonstrably trustworthy AI/ML systems, grounded in current regulatory and governance expectations.[^eu-ai-act][^nist-ai-rmf][^winfield]
This dossier provides detailed research specifications that align with:

- Consolidated regulatory research (`compliance/docs/research/consolidated/`), including EU AI Act, ISO/IEC 27001, and ISO/IEC 42001 obligations.
- Active and planned components inside the AMI-Orchestrator codebase (see `integration/codebase_alignment.md`).
- The pluggable compliance backend design captured in `compliance/docs/research/COMPLIANCE_BACKEND_SPEC.md`.

## Document Map

- `architecture/` — Theoretical pillars, process theory, and ML lifecycle guidance.
- `systems/` — Specifications for the Secure Distributed System (SDS), Compliance Manifest, OAMI protocol, and simulation stack.
- `compliance/` — Crosswalks to external standards and governance practices.
- `integration/` — Mappings between Open AMI capabilities, current code, and roadmap items.

Use these files as the authoritative reference when implementing compliance services or updating consolidated research. Any mechanism that is not yet represented in the codebase is marked **Research** so that future engineering work can prioritize the gaps.

### References

[^eu-ai-act]: European Parliament and Council. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence* (EU AI Act), 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689.

[^nist-ai-rmf]: National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (NIST AI 100-1)*, 2023. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf.

[^winfield]: Alan F. T. Winfield. “Ethical governance is essential to building trust in robotics and artificial intelligence systems.” *Philosophical Transactions of the Royal Society A*, 377(2134), 2019. https://royalsocietypublishing.org/doi/pdf/10.1098/rsta.2019.0162.
