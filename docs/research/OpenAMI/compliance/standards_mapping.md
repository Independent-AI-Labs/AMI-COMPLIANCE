# Standards Mapping

This file summarizes how Open AMI capabilities support the regulatory content captured in `compliance/docs/research/consolidated/`.

| Framework | Relevant Consolidated Docs | Open AMI Alignment | Implementation Status |
|-----------|----------------------------|--------------------|-----------------------|
| EU AI Act | `consolidated/EU_AI_Act/high_risk_ai_systems/` | Compliance Manifest enforces Articles 9, 10, 26; SDS monitors fulfil Articles 72–73 reporting duties. | Manifest loader **Planned**, SDS reporting **Research**. |
| ISO/IEC 27001 | `consolidated/ISO_27001/` | SDS logging + OAMI protocol ensure Annex A.12 auditing; risk owners tracked via manifest metadata. | Audit logging **Operational** (base module); risk owner approvals **Planned**. |
| ISO/IEC 42001 | `consolidated/ISO_42001/` | Pillars provide AIMS controls for human oversight, competence, and performance evaluation. | Documentation live; backend automation **Future**. |
| ISO/IEC 23894 | `consolidated/ISO_23894/` | Learning lifecycle guidance ties risk analysis to adaptive systems. | Requires risk service in compliance backend (**Planned**). |
| NIST AI RMF | `consolidated/NIST_AI_RMF/` | Governance and measurement functions mapped via manifest directives and OASIM scenarios. | Evidence workflows **Research**. |
| Australian AI Ethics | Pending consolidation | Abstraction pillar feeds transparency + contestability controls. | Dependent on explainability tooling (**Research**).

Key references underpinning this mapping include the EU AI Act, NIST AI RMF, ISO/IEC standardisation work, and comparative analyses of global AI ethics guidance.[^eu-ai-act][^nist-ai-rmf][^standardizing-ai][^global-ethics]

For clause-level interpretation, consult the consolidated Markdown sources; this mapping should stay synchronized whenever those files change.

### References

[^eu-ai-act]: European Parliament and Council. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence* (EU AI Act), 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689.

[^nist-ai-rmf]: National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (NIST AI 100-1)*, 2023. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf.

[^standardizing-ai]: J. Mökander et al. “Standardising AI: The Case of ISO/IEC JTC 1/SC 42.” *IEEE Technology and Society Magazine*, 40(4):34–41, 2021. https://arxiv.org/pdf/2106.10316.pdf.

[^global-ethics]: Anna Jobin, Marcello Ienca, and Effy Vayena. “The Global Landscape of AI Ethics Guidelines.” *Nature Machine Intelligence*, 1(9):389–399, 2019. https://arxiv.org/pdf/1903.03425.pdf.
