# GDPR Data Subject Rights

## Description

Comprehensive rights granted to individuals regarding their personal data, including access, rectification, erasure, and control over automated processing.

## Legal Basis

**GDPR Chapter III - Rights of the Data Subject (Articles 12-23)**

## Key Elements

### Article 12 - Transparent information and communication

#### General Requirements
- Information provided in concise, transparent, intelligible, easily accessible form
- Clear and plain language
- Information provided free of charge
- Response within one month (extendable by two months for complex requests)
- Identity verification may be required
- Excessive requests may incur fee or be refused

### Article 13 - Information to be provided (data collected from subject)

#### Must provide at time of collection:
- Controller identity and contact details
- DPO contact details (where applicable)
- Processing purposes and lawful basis
- Legitimate interests (if applicable)
- Recipients or categories of recipients
- International transfer details

#### Additional required information:
- Retention period or criteria
- Data subject rights existence
- Consent withdrawal right
- Complaint right to supervisory authority
- Whether provision is statutory/contractual requirement
- Automated decision-making existence and logic

### Article 14 - Information to be provided (data not from subject)

#### Same as Article 13 plus:
- Categories of personal data concerned
- Source of personal data
- Must be provided within one month of obtaining

#### Exceptions:
- Subject already has information
- Provision proves impossible or disproportionate effort
- Legal obligation for obtaining/disclosure
- Professional secrecy requirements

### Article 15 - Right of access

#### Data subject entitled to:
- Confirmation whether data is being processed
- Access to the personal data
- Following information:
  - Processing purposes
  - Categories of data concerned
  - Recipients or categories
  - Retention period
  - Rights to rectification/erasure/restriction/objection
  - Complaint right
  - Source of data if not from subject
  - Automated decision-making details
  - International transfer safeguards

#### Provision requirements:
- Copy of personal data free of charge
- Additional copies may incur reasonable fee
- Electronic request = electronic format response
- Must not adversely affect others' rights

### Article 16 - Right to rectification

- Right to rectification without undue delay
- Right to have incomplete data completed
- Including by supplementary statement

### Article 17 - Right to erasure ('right to be forgotten')

#### Grounds for erasure:
1. Data no longer necessary for purposes
2. Consent withdrawn (and no other lawful basis)
3. Successful objection to processing
4. Unlawful processing
5. Legal obligation to erase
6. Children's data collected for information society services

#### Exceptions:
- Freedom of expression and information
- Legal obligation compliance
- Public health reasons
- Archiving/research/statistical purposes
- Legal claims

#### Public data obligations:
- Must inform other controllers if data made public
- Take reasonable steps including technical measures

### Article 18 - Right to restriction of processing

#### Applicable when:
1. Accuracy contested (restrict during verification)
2. Processing unlawful but subject opposes erasure
3. Controller no longer needs but subject needs for legal claims
4. Objection pending verification of legitimate grounds

#### Restriction effects:
- Storage permitted
- Other processing only with consent or for legal claims/protection
- Must inform before lifting restriction

### Article 19 - Notification obligation

- Must communicate rectification/erasure/restriction to all recipients
- Unless impossible or disproportionate effort
- Must inform data subject about recipients if requested

### Article 20 - Right to data portability

#### Conditions:
- Processing based on consent or contract
- Processing carried out by automated means

#### Rights:
- Receive data in structured, commonly used, machine-readable format
- Right to transmit to another controller without hindrance
- Direct transmission where technically feasible

#### Limitations:
- Must not adversely affect others' rights
- Does not apply to public task/official authority processing

### Article 21 - Right to object

#### General right:
- Object to processing based on public task/legitimate interests
- Including profiling based on these provisions
- Controller must stop unless compelling legitimate grounds

#### Direct marketing:
- Absolute right to object
- Including profiling for direct marketing
- Must be explicitly brought to attention at first communication

#### Research/statistics:
- Right to object unless necessary for public interest task

### Article 22 - Automated individual decision-making

#### General prohibition on solely automated decisions that:
- Produce legal effects
- Similarly significantly affect individual

#### Exceptions:
1. Necessary for contract
2. Authorised by law with suitable safeguards
3. Explicit consent

#### Safeguards required:
- Right to human intervention
- Right to express point of view
- Right to contest decision
- No special category data unless explicit consent or substantial public interest

### Article 23 - Restrictions

Member States may restrict rights when necessary for:
- National/public security
- Defence
- Prevention/investigation of criminal offences
- Other important public interests
- Protection of data subject or others
- Enforcement of civil law claims

## Implementation Requirements for AI Systems

### Transparency in AI Context
1. **Explainable AI Interfaces**
   - User-friendly explanations of AI decisions
   - Visualisation tools for model behaviour
   - Confidence scores and uncertainty communication

2. **Automated Decision Documentation**
   - Clear identification of automated processes
   - Logic explanation in lay terms
   - Significance and consequences explained

### Access Rights for AI Systems
1. **AI Processing Visibility**
   - Which AI models process their data
   - Training data inclusion status
   - Inference data usage

2. **Model Decision Access**
   - Historical AI decisions about individual
   - Features/factors considered
   - Decision pathways taken

### Rectification in AI
1. **Training Data Correction**
   - Procedures to correct training data
   - Model retraining triggers
   - Correction propagation tracking

2. **Inference Correction**
   - Correct input data for decisions
   - Re-run decisions with corrected data
   - Update historical records

### Erasure Challenges
1. **Model Unlearning**
   - Techniques for removing data influence
   - Retraining vs incremental unlearning
   - Verification of effective erasure

2. **Federated Learning Considerations**
   - Erasure in distributed models
   - Update propagation requirements
   - Verification challenges

### Human Intervention Requirements
1. **Override Mechanisms**
   - Human review processes
   - Appeal procedures
   - Escalation paths

2. **Meaningful Intervention**
   - Qualified human reviewers
   - Full decision reconsideration
   - Not just rubber-stamping

## Traces to Other Standards

### EU AI Act
- Article 14 (Human oversight) complements GDPR Article 22
- Article 13 (Transparency) extends GDPR information requirements
- Article 52 (Transparency obligations) for AI-specific scenarios

### ISO/IEC 27701
- 7.3 (Determining information for PII principals) maps to Articles 13-14
- 8.2 (PII principals' rights) implements Chapter III requirements

### ISO/IEC 42001
- Clause 7.3 (Awareness) includes data subject rights
- Annex B controls for transparency and human oversight

### NIST Privacy Framework
- Control-P function addresses data subject participation
- Communicate-P function covers transparency requirements

## Audit Checklist

- [ ] Privacy notices include all required Article 13/14 information
- [ ] Response procedures for all rights established
- [ ] Identity verification process defined
- [ ] One-month response timeline tracked
- [ ] Access request fulfilment process documented
- [ ] Rectification procedures implemented
- [ ] Erasure criteria and exceptions documented
- [ ] Restriction mechanisms available
- [ ] Portability format defined (where applicable)
- [ ] Objection handling process established
- [ ] Automated decision-making identified and documented
- [ ] Human intervention procedures for automated decisions
- [ ] Marketing opt-out mechanisms implemented
- [ ] Rights information prominently displayed
- [ ] Staff trained on rights handling