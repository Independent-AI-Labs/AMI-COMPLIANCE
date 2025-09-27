# High-Risk AI Systems Requirement: Accuracy, Robustness and Cybersecurity

## Description

High-risk AI systems must be designed and developed in such a way that they achieve an appropriate level of accuracy, robustness, and cybersecurity, and that they perform consistently in those respects throughout their lifecycle.

## Legal Basis

The requirement for accuracy, robustness and cybersecurity is laid down in **Article 15 of the EU AI Act**.

## Key Elements

### Accuracy

*   High-risk AI systems must achieve an appropriate level of accuracy in relation to their intended purpose.
*   The levels of accuracy and the relevant accuracy metrics shall be declared in the accompanying instructions of use.

### Robustness

*   High-risk AI systems must be as resilient as possible regarding errors, faults or inconsistencies that may occur within the system or the environment in which the system operates.
*   Robustness may be achieved through technical redundancy solutions, which may include backup or fail-safe plans.
*   High-risk AI systems that continue to learn after being placed on the market or put into service shall be developed in such a way as to eliminate or reduce as far as possible the risk of possibly biased outputs influencing input for future operations (feedback loops).

### Cybersecurity

*   High-risk AI systems must be resilient against attempts by unauthorized third parties to alter their use, outputs or performance by exploiting system vulnerabilities.
*   Technical solutions to address AI specific vulnerabilities shall include, where appropriate, measures to prevent, detect, respond to, resolve and control for attacks trying to manipulate the training data set (data poisoning), or pre-trained components used in training (model poisoning), inputs designed to cause the AI model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws.

## Traces to Other Standards

*   **NIST AI RMF:** The requirements for accuracy, robustness, and cybersecurity are aligned with the **Measure** and **Manage** functions of the NIST AI RMF.
    *   **Measure:** The `Measure` function includes evaluating AI systems for trustworthy characteristics, including accuracy, reliability, and resilience (MEASURE 2.5, 2.7).
    *   **Manage:** The `Manage` function includes implementing risk treatment measures, which can include technical solutions to improve accuracy, robustness, and cybersecurity.

*   **ISO/IEC 42001 (AI Management System):** These requirements are directly related to several controls in Annex A of ISO/IEC 42001:
    *   **A.6.2.4: AI system verification and validation**
    *   **A.9.3: Objectives for responsible use of AI system** (which includes reliability and security as objectives)

*   **ISO/IEC 27001 (Information Security Management System):** The cybersecurity requirements of the EU AI Act are a specific application of the information security controls in ISO/IEC 27001. The entire ISO/IEC 27001 standard is relevant, but the following clauses and controls from Annex A are particularly important:
    *   **Clause 6.1.2: Information security risk assessment**
    *   **Clause 8: Operation**
    *   **Annex A.8: Technological controls**

*   **NIST RMF:** The accuracy, robustness, and cybersecurity requirements are key inputs to the **Select**, **Implement**, and **Assess** steps of the NIST RMF. These requirements inform the selection and implementation of controls, and the assessment of their effectiveness.

*   **ETSI TR 103 635:** This technical report from ETSI provides a survey of AI threats and potential mitigation measures, which is highly relevant to the cybersecurity requirements of the EU AI Act.

