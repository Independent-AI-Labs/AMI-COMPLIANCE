# High-Risk AI Systems Requirement: Human Oversight

## Description

High-risk AI systems must be designed and developed so that natural persons can oversee their operation effectively throughout the whole period of use. Appropriate human-machine interface tools and organisational procedures allow humans to prevent or minimise risks to health, safety and fundamental rights that may arise even when other safeguards are in place.

## Legal Basis

Human oversight duties are defined in **Article 14 of the EU AI Act**.

## Key Elements

### Oversight Measures

Oversight measures must be commensurate with the system’s risk profile, level of autonomy and context of use, and may include:

* **Built-in controls** specified and implemented by the provider (e.g. explainability aids, confidence indicators, safe-stop functions).
* **Organisational measures** identified by the provider for the deployer to implement (e.g. dual-control procedures, escalation paths, operating checklists).

### Capabilities Required for Oversight Personnel

Individuals assigned to human oversight must be enabled, through training and system design, to:

* Understand the system’s capacities, limitations and potential failure modes and monitor for anomalies or unexpected performance.
* Recognise and compensate for automation bias, especially when the AI system supplies recommendations for human decision-making.
* Correctly interpret the AI system’s output using the interpretation tools provided.
* Disregard, override or reverse the AI system’s output when appropriate, including deciding not to use the system in specific situations.
* Intervene or interrupt operation via a ‘stop’ button or equivalent control that brings the system to a safe state.

### Specific Rule for Remote Biometric Identification

For high-risk AI systems that perform remote biometric identification of natural persons (Annex III, point 1(a)):

* No decision or action may be taken solely on the AI identification unless **at least two competent natural persons** independently verify and confirm the result.
* **Member States may waive** the double-verification requirement for systems used in law enforcement, migration, border control or asylum where national or Union law considers the requirement disproportionate. Any such waiver must still ensure safeguards consistent with Article 14.

### Link to Logging and Post-Market Monitoring

Oversight personnel must ensure logs required under Articles 12 and 19 are properly captured, retained and shared with providers to support post-market monitoring (Article 72) and serious-incident reporting (Article 73).

## Traces to Other Standards

* **NIST AI RMF:** Aligns with GOVERN 3.2 (role definition) and MANAGE 2.4 (mechanisms to disengage AI systems) and supports ongoing risk tracking in MANAGE 4.
* **ISO/IEC 42001 (AI Management System):** Reflects Annex A controls on human oversight, training and responsible use objectives (A.9.3, A.9.4) as well as Clause 7.2 competence requirements.
* **ISO/IEC 27001 (Information Security Management System):** Ties into Clause 7.2 training, Clause 8 operational planning and Annex A controls on privileged access and monitoring.
* **NIST RMF:** Embedded within the Implement and Monitor steps, ensuring that authorising officials retain situational awareness and can trigger corrective actions when controls fail.

