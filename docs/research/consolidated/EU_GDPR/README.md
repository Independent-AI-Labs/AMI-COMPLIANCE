# EU General Data Protection Regulation (GDPR) - Consolidated Analysis

**Regulation (EU) 2016/679**
**Effective Date:** 25 May 2018
**Last Updated Analysis:** September 2025

## Overview

The General Data Protection Regulation (GDPR) is a comprehensive data protection law that regulates the processing of personal data of individuals within the European Union and European Economic Area. It aims to give individuals control over their personal data and to simplify the regulatory environment for international business.

## Structure of This Analysis

This consolidated analysis breaks down GDPR into its key components:

### 1. Principles (Chapter II)
- `/principles/` - Core data protection principles (Article 5-11)
  - Lawfulness, fairness, and transparency
  - Purpose limitation
  - Data minimisation
  - Accuracy
  - Storage limitation
  - Integrity and confidentiality
  - Accountability

### 2. Rights of Data Subjects (Chapter III)
- `/rights/` - Individual rights (Articles 12-23)
  - Right to information and access
  - Right to rectification and erasure
  - Right to data portability
  - Right to object
  - Rights related to automated decision-making

### 3. Controller and Processor Obligations (Chapter IV)
- `/obligations/` - Organisational requirements (Articles 24-43)
  - Data protection by design and default
  - Data Processing Agreements
  - Records of processing activities
  - Data Protection Impact Assessments
  - Data Protection Officer requirements

### 4. Security Requirements (Chapter IV, Section 2)
- `/security/` - Technical and organisational measures (Articles 32-34)
  - Security of processing
  - Personal data breach notification
  - Communication requirements

### 5. International Transfers (Chapter V)
- `/international_transfers/` - Cross-border data flows (Articles 44-50)
  - Adequacy decisions
  - Appropriate safeguards
  - Standard contractual clauses
  - Binding corporate rules

## Key Compliance Areas for AI Systems

### AI-Specific Considerations Under GDPR

1. **Automated Decision-Making (Article 22)**
   - Prohibition on solely automated decisions with legal/significant effects
   - Right to human intervention
   - Special protections for profiling

2. **Transparency for AI (Articles 13-14)**
   - Obligation to inform about automated decision-making existence
   - Meaningful information about logic involved
   - Significance and envisaged consequences

3. **Data Protection Impact Assessment for AI (Article 35)**
   - Mandatory for high-risk processing
   - Systematic and extensive evaluation
   - Large-scale processing of special categories

4. **Privacy by Design for AI Systems (Article 25)**
   - Technical and organisational measures
   - Data minimisation in AI training
   - Purpose limitation for AI models

## Relationship to Other Standards

### EU AI Act Alignment
- GDPR provides the data protection foundation for AI Act compliance
- Article 10 of AI Act references GDPR for training data governance
- Combined compliance approach recommended

### ISO/IEC 27701 Privacy Extension
- GDPR requirements map to ISO/IEC 27701 controls
- Provides implementation framework for GDPR compliance

### NIST Privacy Framework
- Cross-walks available between GDPR articles and NIST Privacy Framework
- Complementary risk-based approach

## Implementation Priority

For AMI-ORCHESTRATOR, the following GDPR requirements are critical:

1. **Lawful Basis** - Establish and document for all AI processing
2. **Transparency** - Clear information about AI system operation
3. **Data Minimisation** - Limit training data to necessary minimum
4. **Security** - Implement appropriate technical measures
5. **Rights Management** - Enable data subject rights in AI context
6. **Impact Assessments** - Conduct DPIAs for high-risk AI processing

## Navigation

- [Principles →](./principles/)
- [Rights →](./rights/)
- [Obligations →](./obligations/)
- [Security →](./security/)
- [International Transfers →](./international_transfers/)