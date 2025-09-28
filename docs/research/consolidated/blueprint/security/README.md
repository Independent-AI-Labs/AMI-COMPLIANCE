# Blueprint: Security

## Introduction

Security is a fundamental prerequisite for trustworthy AI. AI systems, like any other software system, are vulnerable to attack. However, AI systems also introduce new vulnerabilities that need to be addressed. This document provides a synthesized view of the security requirements from the EU AI Act, ISO/IEC 27001, and the NIST RMF.

## Unified Security Process

The following is a unified process for ensuring the security of AI systems that integrates the requirements from the relevant standards.

### 1. Implement a comprehensive Information Security Management System (ISMS)

*   **Objective:** To establish, implement, maintain, and continually improve an ISMS in accordance with ISO/IEC 27001.
*   **Activities:**
    *   Define an information security policy.
    *   Conduct information security risk assessments.
    *   Select and implement information security controls.
    *   Monitor and review the performance of the ISMS.
*   **Traces:**
    *   [ISO/IEC 27001: All Clauses](../../iso_27001/)

### 2. Address AI-Specific Vulnerabilities

*   **Objective:** To protect AI systems against AI-specific attacks.
*   **Activities:**
    *   Implement measures to prevent, detect, and respond to attacks such as data poisoning, model poisoning, and adversarial examples.
*   **Traces:**
    *   [EU AI Act: Accuracy, Robustness and Cybersecurity](../../EU_AI_Act/high_risk_ai_systems/requirements/accuracy_robustness_cybersecurity/)

### 3. Follow a Secure Development Lifecycle

*   **Objective:** To integrate security into the entire lifecycle of the AI system.
*   **Activities:**
    *   Apply the principles of the NIST Risk Management Framework (RMF) to the AI system.
    *   Implement security controls throughout the development, implementation, and operation of the system.
*   **Traces:**
    *   [NIST RMF: All Steps](../../nist_rmf/)

