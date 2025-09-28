# Machine Learning Lifecycle Alignment

Open AMI applies the four pillars across each learning paradigm, incorporating safeguards highlighted in contemporary trustworthy-ML literature.[^datasheets][^concrete] Use this as guidance for future compliance services and tests.

## Lifecycle Overview

- Embeds compliance checkpoints into data intake, model training, validation, deployment, and monitoring.
- Complements the consolidated risk-management guidance (`consolidated/ISO_42001/`) and post-market monitoring requirements (`consolidated/EU_AI_Act/high_risk_ai_systems/requirements/post_market_monitoring/`).

## Supervised Learning

- Requires labelled data provenance and bias scans before training (map to Compliance Manifest constraints).[^datasheets][^model-cards]
- Supports policy-driven feature approval via the planned evidence registry (`compliance/backend/evidence_service.py`).

## Unsupervised Learning

- Emphasises dataset integrity and drift detection — tie to SDS anomaly detection (see `../systems/secure_distributed_system.md`).
- Marked **Research** pending drift tooling in `streams/` module.

## Reinforcement Learning

- Guidance functions enforce safe action spaces; log every policy update through compliance MCP hooks.[^concrete]
- Future integration: RL sandbox under `simulation/` nodes to supply evidence for Articles 14 (human oversight).

## Continuous and Online Learning

- Requires adaptive controls and versioned manifests to satisfy EU AI Act lifecycle obligations.[^continual]
- Implementation: scheduled manifest review jobs in compliance backend (**Planned**).

## Federated Learning

- Inherits SDS guarantees for secure aggregation and privacy.[^federated]
- Reference consolidated privacy requirements (`consolidated/EU_AI_Act/.../data_governance/`).
- Needs secure channel support from base networking stack (**Research**).

## Model Composition and Interoperability

- Feeds into OAMI protocol for knowledge sharing (see `../systems/oami_protocol.md`).
- Compliance implication: maintain component registry with approval status (**Future Implementation** in compliance backend).

### References

[^datasheets]: Timnit Gebru et al. “Datasheets for Datasets.” *Communications of the ACM*, 64(12):86–92, 2021. https://arxiv.org/pdf/1803.09010.pdf.

[^model-cards]: Margaret Mitchell et al. “Model Cards for Model Reporting.” *Proceedings of the 2019 Conference on Fairness, Accountability, and Transparency*, 2019. https://arxiv.org/pdf/1810.03993.pdf.

[^concrete]: Dario Amodei et al. “Concrete Problems in AI Safety.” *arXiv preprint* arXiv:1606.06565, 2016. https://arxiv.org/pdf/1606.06565.pdf.

[^continual]: German I. Parisi et al. “Continual Lifelong Learning with Neural Networks: A Review.” *Neural Networks*, 113:54–71, 2019. https://arxiv.org/pdf/1802.07569.pdf.

[^federated]: Peter Kairouz et al. “Advances and Open Problems in Federated Learning.” *Foundations and Trends in Machine Learning*, 14(1–2):1–210, 2021. https://arxiv.org/pdf/1912.04977.pdf.
