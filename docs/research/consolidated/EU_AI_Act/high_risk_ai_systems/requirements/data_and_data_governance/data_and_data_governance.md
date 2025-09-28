# High-Risk AI Systems Requirement: Data and Data Governance

## Description

High-risk AI systems that rely on training AI models with data must use training, validation and testing data sets that meet rigorous quality standards. Strong data governance limits bias, promotes safety and underpins trustworthy performance.

## Legal Basis

The data governance requirements are laid down in **Article 10 of the EU AI Act**.

## Key Elements

### Data Governance and Management Practices

Training, validation and testing data sets shall be subject to appropriate governance covering:

* **Relevant design choices** and assumptions that influence data selection.
* **Data collection processes** and provenance, including third-party sources.
* **Preparation operations** such as labelling, cleaning, filtering, enrichment and aggregation.
* **Assessment of availability, quantity and suitability** of datasets.
* **Bias examination** and documentation of potential negative impacts on health, safety or fundamental rights.
* **Mitigation measures** to detect, prevent and reduce identified biases.
* **Identification of data gaps or shortcomings** and follow-on remediation plans.

### Quality Criteria for Data Sets

Datasets must be:

* **Relevant, sufficiently representative, as error-free and complete as possible** given the intended purpose.
* Equipped with **appropriate statistical properties** for the affected persons or groups.
* Tailored to the **geographical, contextual, behavioural or functional setting** of use, at either the individual dataset level or across combined datasets.

### Processing Special Categories of Personal Data

Providers may only process special categories of personal data for bias detection and correction when all of the following conditions are satisfied:

1. **Strict necessity:** The objective cannot be achieved with other data, including synthetic or anonymised data.
2. **Technical limitations on re-use:** Special-category data is protected with state-of-the-art privacy and security measures, including pseudonymisation.
3. **Access control:** Processing is subject to strict safeguards that ensure only authorised persons with confidentiality obligations can access the data.
4. **No onward transfer:** The data is not transmitted or otherwise made accessible to other parties.
5. **Deletion duties:** The data is deleted once the bias is corrected or the retention period expires, whichever occurs first.
6. **Accountability records:** Records of processing explain why the use of special-category data was strictly necessary and why alternatives were insufficient.

### Applicability to Non-ML Techniques

For high-risk AI systems that do not involve training of AI models, the governance requirements of paragraphs 2-5 apply to **testing datasets** only.

## Traces to Other Standards

* **NIST AI RMF:** Supports the **Map** function (context, stakeholder impacts) and **Measure** function (bias evaluation, TEVV traceability).
* **ISO/IEC 42001 (AI Management System):** Mirrors Annex A controls on data acquisition, quality, provenance and preparation (A.7.2-A.7.6) and links to Clause 6 on risk and impact assessments.
* **ISO/IEC 27001 (Information Security Management System):** Complements information classification (Annex A 5.12), transfer (5.14), deletion (8.10) and masking (8.11) controls; relies on Clause 7.5 documentation and Clause 8 operational control.
* **ISO/IEC 27701:** Provides privacy safeguards for special-category data handling, reinforcing minimisation, purpose limitation and accountability.
* **NIST RMF:** Aligns with Prepare (P-12, P-13) and Categorize steps that classify information types and sensitivity to guide control selection.
