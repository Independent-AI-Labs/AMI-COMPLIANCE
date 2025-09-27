# Governance Alignment

Open AMI governance guidance extends the consolidated compliance research into actionable operating models, echoing recommended practices from AI ethics and risk management scholarship.[^winfield][^nist-ai-rmf]

## Oversight Structure

- **Compliance Working Group** — maintains manifests, reviews evidence (see `CURRENT_IMPLEMENTATION_STATUS.md`).
- **Engineering Owners** — implement manifest directives in code modules; tie changes to OAMI tasks.
- **Audit Stakeholders** — consume SDS logs and manifest reports for certification.

## Key Processes

1. **Manifest Review Cadence** — quarterly, or after regulatory updates.
2. **Incident Workflow** — SDS signals trigger Article 73 report templates and ISO/IEC 27001 Clause 16 handling.
3. **Evidence Intake** — compliance MCP collects artifacts, storing metadata for ISO/IEC 42001 Clause 8 documentation.
4. **Change Management** — architecture decisions referencing Open AMI pillars documented in `docs/Architecture-Map.md`.

## Tooling Dependencies

- Compliance backend services (loader, evidence, risk) — **Planned**.
- Base audit trail exporter to compliance MCP — **Planned**.
- Simulation-based rehearsals (OASIM) — **Research**.

Maintain this file alongside `EXECUTIVE_ACTION_PLAN.md` to keep strategic plans aligned with Open AMI theory.

### References

[^winfield]: Alan F. T. Winfield. “Ethical governance is essential to building trust in robotics and artificial intelligence systems.” *Philosophical Transactions of the Royal Society A*, 377(2134), 2019. https://royalsocietypublishing.org/doi/pdf/10.1098/rsta.2019.0162.

[^nist-ai-rmf]: National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (NIST AI 100-1)*, 2023. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf.
