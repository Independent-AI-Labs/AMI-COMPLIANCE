# OASIM Simulation Subsystem

OASIM provides simulation-driven validation, grounding, and embodiment support for Open AMI, drawing on immersive simulation platforms for embodied AI research.[^habitat]

## Goals

- Test compliance behaviours in controlled environments before production deployment.
- Supply synthetic but traceable evidence artefacts for manifest directives (e.g., robustness, human oversight drills).[^concrete]

## Architecture

1. **Simulation Service** — runs physics or environment models; produces telemetry tagged with Compliance IDs (**Research**).
2. **Interpretation Service** — renders and analyses simulation outputs for human review; supports multi-modal evidence (**Research**).
3. **Protocol Gateway** — bridges OAMI protocol calls to the simulator interfaces (target location `compliance/backend/simulation_gateway.py`).

## Standards Alignment

- Supports ISO/IEC 42001 Clause 8 (operational planning and control) through rehearsal scenarios.
- Reinforces EU AI Act Annex IV documentation expectations by generating structured evaluation logs.[^eu-ai-act]

## Integration Points

- Connects to `nodes/` for provisioning compute assets.
- Feeds compliance backend evidence registry with scenario results.
- Potential integration with NVIDIA Omniverse / USD toolchains (flagged as **Research**).

## Roadmap

- **Prototype**: scripted simulation harness using existing `streams/` ingestion paths.
- **MVP**: incorporate into compliance MCP for manual trigger + evidence capture.
- **Advanced**: automated regression suite with pass/fail hooks for manifest directives.

### References

[^habitat]: Manolis Savva et al. “Habitat: A Platform for Embodied AI Research.” *Proceedings of ICCV*, 2019. https://arxiv.org/pdf/1904.01201.pdf.

[^concrete]: Dario Amodei et al. “Concrete Problems in AI Safety.” *arXiv preprint* arXiv:1606.06565, 2016. https://arxiv.org/pdf/1606.06565.pdf.

[^eu-ai-act]: European Parliament and Council. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence* (EU AI Act), 2024. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689.
