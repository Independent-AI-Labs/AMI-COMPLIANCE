# High-Risk AI Systems Requirement: Post-Market Monitoring and Incident Reporting

## Description

Providers of high-risk AI systems must operate a post-market monitoring system that actively collects, documents and analyses performance information throughout the system’s lifecycle. The monitoring system feeds continuous improvement, enables corrective actions and supports serious-incident reporting.

## Legal Basis

The obligations stem from **Article 72 (Post-market monitoring)** and **Article 73 (Serious incident reporting)** of the EU AI Act.

## Key Elements

### Post-Market Monitoring System

* **Lifecycle scope:** Providers must plan, establish, implement, document and maintain a post-market monitoring system as part of their quality management system (Article 17(1)(h)).
* **Data collection:** The system must systematically gather and analyse operational evidence from deployers, users, logs (Article 12/19), impact assessments (Article 27) and other sources.
* **Feedback loop:** Findings must feed back into risk management (Article 9), technical documentation (Article 11) and any corrective actions required under Article 20.
* **Collaboration:** Providers must cooperate with deployers to secure the data needed for monitoring, while deployers report issues and enable access in line with Article 26.
* **Documented plan:** The monitoring system is captured in a documented plan within the technical documentation. The Commission will issue harmonised templates and data requirements; providers may integrate sector-specific plans where those meet Article 72(3)-(4).

### Serious Incident and Malfunction Reporting

* **Reporting duty:** Providers must notify the market surveillance authority of the Member State where the incident occurred, and the notifying Member State’s competent authority, no later than **15 days** after becoming aware of a serious incident or malfunction that breaches EU AI Act obligations (Article 73(1)-(2)).
* **Escalation timelines:** Fatal incidents must be reported within **10 days**, and widespread serious incidents with significant public-safety impact within **two days**. Providers may send preliminary reports when full details are not yet available, followed by updates (Article 73(2)-(7)).
* **Deployers’ role:** Deployers must inform providers without undue delay and cooperate in investigations (Articles 26 and 73(3)).
* **Documentation:** Incident reports and follow-up actions remain part of the quality management system. Detailed content requirements will follow Commission templates issued under Article 73(9).

## Traces to Other Standards

* **NIST AI RMF:** Supports MANAGE 4 (post-deployment monitoring, incident response, recovery) and MEASURE 3 (tracking emergent risks) with continuous feedback into controls.
* **ISO/IEC 42001 (AI Management System):** Aligns with Clauses 8 (operation), 9 (performance evaluation) and 10 (improvement), plus Annex A controls on incident management and change control.
* **ISO/IEC 27001:** Reinforces Clauses 8.1 (operational control), 9.1-9.3 (monitoring, internal audit, management review) and 10.2 (corrective action), ensuring security incidents and nonconformities are documented.
* **NIST RMF:** Parallels the Monitor step (M-1 to M-5) and integrates with Authorize (R-2, R-3) when monitoring results change risk posture.
