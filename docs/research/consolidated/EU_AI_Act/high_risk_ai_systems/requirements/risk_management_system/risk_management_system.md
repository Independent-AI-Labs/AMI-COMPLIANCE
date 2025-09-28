# High-Risk AI Systems Requirement: Risk Management System

## Description

Providers of high-risk AI systems must establish, implement, document, and maintain a risk management system. This system is a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating.

## Legal Basis

The requirement for a risk management system is laid down in **Article 9 of the EU AI Act**.

## Key Elements

The risk management system shall comprise the following steps:

1.  **Identification and analysis of known and reasonably foreseeable risks:** This includes risks to health, safety, or fundamental rights that the high-risk AI system can pose when used as intended.

2.  **Estimation and evaluation of risks:** This includes risks that may emerge when the high-risk AI system is used in accordance with its intended purpose, and under conditions of reasonably foreseeable misuse.

3.  **Evaluation of other risks:** This is based on the analysis of data gathered from the post-market monitoring system.

4.  **Adoption of appropriate and targeted risk management measures:** These measures are designed to address the identified risks.

## Risk Management Measures

The risk management measures shall be such that the relevant residual risk associated with each hazard, as well as the overall residual risk of the high-risk AI systems is judged to be acceptable. In identifying the most appropriate risk management measures, the following shall be ensured:

*   **Elimination or reduction of risks:** This should be done as far as technically feasible through adequate design and development of the high-risk AI system.
*   **Implementation of mitigation and control measures:** This is for risks that cannot be eliminated.
*   **Provision of information:** This includes providing information required under Article 13 and, where appropriate, training to deployers.

### Scope and Interdependencies

The regulation expects providers to focus on risks that can reasonably be mitigated or eliminated through system design or by supplying adequate technical information (Article 9(3)). Risk treatments must also account for the combined effect of all Chapter III, Section 2 requirements so that safeguards reinforce each other without introducing new hazards (Article 9(4)).

### Lifecycle Testing and Review

Providers must test high-risk AI systems throughout development, and at the latest before market placement, using predefined metrics and probabilistic thresholds to confirm consistent performance for the intended purpose (Article 9(6)-(8)). Real-world testing is permitted when Article 60 conditions are met. Insights from post-market monitoring must feed back into the risk process so that mitigation stays current.

### Protection of Vulnerable Groups and Integration with Other Frameworks

Risk management activities must consider whether the system could adversely impact minors or other vulnerable groups and incorporate appropriate safeguards (Article 9(9)). Providers subject to other Union risk-management obligations may integrate the EU AI Act steps into their existing frameworks so long as all Article 9 requirements remain satisfied (Article 9(10)).

## Traces to Other Standards

*   **NIST AI RMF:** The EU AI Act's risk management system is highly aligned with the four core functions of the NIST AI RMF:
    *   **Govern:** The requirement to establish, implement, document, and maintain a risk management system is a core aspect of the Govern function.
    *   **Map:** The identification and analysis of known and reasonably foreseeable risks in the EU AI Act directly corresponds to the Map function, which focuses on establishing context and identifying risks.
    *   **Measure:** The estimation and evaluation of risks in the EU AI Act aligns with the Measure function, which employs various methods to analyze, assess, and monitor AI risks.
    *   **Manage:** The adoption of appropriate and targeted risk management measures in the EU AI Act is a direct implementation of the Manage function, which involves prioritizing and responding to risks.

*   **ISO/IEC 42001 (AI Management System):** The risk management system in the EU AI Act is a core component of an AIMS as defined in ISO/IEC 42001. Specifically, it aligns with:
    *   **Clause 6.1: Actions to address risks and opportunities**
    *   **Clause 8.2: AI risk assessment**
    *   **Clause 8.3: AI risk treatment**

*   **ISO/IEC 27001 (Information Security Management System):** The risk management system for an AI system will need to be integrated with the organization's overall ISMS. The cybersecurity aspects of the AI risk management system are directly addressed by the controls in ISO/IEC 27001. The risk assessment process in the EU AI Act should be aligned with the information security risk assessment process in **Clause 6.1.2** of ISO/IEC 27001.

*   **NIST RMF (Risk Management Framework for Information Systems and Organizations):** The EU AI Act's risk management system can be seen as a specific application of the NIST RMF to AI systems. The steps of the EU AI Act's risk management system align with the steps of the NIST RMF as follows:
    *   **Prepare:** The establishment of the risk management system itself is part of the Prepare step.
    *   **Categorize, Select, Implement, Assess:** The identification, analysis, estimation, and evaluation of risks, and the adoption of risk management measures in the EU AI Act correspond to these steps in the NIST RMF.
    *   **Authorize:** The decision that the residual risk is acceptable is an authorization decision.
    *   **Monitor:** The requirement for the risk management system to be a continuous iterative process and to evaluate other risks based on post-market monitoring data is aligned with the Monitor step.

*   **ISO 31000 (Risk management — Guidelines):** This is a general standard on risk management that provides principles and guidelines for managing risk in any type of organization. The risk management system in the EU AI Act is a specific application of the principles in ISO 31000 to the context of AI systems.
