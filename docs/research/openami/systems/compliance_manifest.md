# Compliance Manifest Lifecycle

The Compliance Manifest (CM) is the canonical store of obligations, constraints, and evidence rules inside Open AMI, reflecting obligations defined across emerging AI governance instruments.[^eu-ai-act][^nist-ai-rmf]

## Concept

- Modeled as a structured catalogue of directives (controls, metrics, workflows) mapped to standards.[^standardizing-ai]
- Drives Compliance State Transitions defined in `architecture/process_theory.md`.

## Lifecycle Stages

1. **Authoring** — ingest consolidated requirement entries (`compliance/docs/research/consolidated/**`).
2. **Validation** — policy linting and conflict resolution (**Planned** service `compliance/backend/policy_validator.py`).
3. **Activation** — publish CM snapshots to runtime components via the compliance MCP (**Future Implementation**).
4. **Monitoring** — SDS runtime reports compliance signal deltas.
5. **Review** — periodic governance reviews documented in `compliance/docs/research/CURRENT_IMPLEMENTATION_STATUS.md`.

## Data Model

- `Control` — normalized representation of a standard requirement (source: consolidated docs).
- `Directive` — executable rule referencing controls and target systems.
- `EvidenceRule` — specification of required data artifacts (e.g., logs, reports).
- `Exception` — formally approved deviations with expiry.

## Alignment with Standards

- EU AI Act Articles 9, 10, 26, 72 (see consolidated high-risk requirement files).[^eu-ai-act]
- ISO/IEC 27001 Clause 6.1.3 (risk treatment) and Annex A (control catalogue).[^standardizing-ai]
- ISO/IEC 42001 Clause 7 (human oversight) and Clause 9 (performance evaluation).

## Implementation Status

- **Research**: CM exists as documentation only. No parser or storage layer.
- **Next Step**: Build loader that transforms consolidated Markdown into CM JSON for backend seeding (Sprint 1 in `CURRENT_IMPLEMENTATION_STATUS.md`).

### References

[^eu-ai-act]: European Parliament and Council. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence* (EU AI Act), 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689.

[^nist-ai-rmf]: National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (NIST AI 100-1)*, 2023. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf.

[^standardizing-ai]: J. Mökander et al. “Standardising AI: The Case of ISO/IEC JTC 1/SC 42.” *IEEE Technology and Society Magazine*, 40(4):34–41, 2021. https://arxiv.org/pdf/2106.10316.pdf.
