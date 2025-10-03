# Compliance Backend & MCP Server Specification

**Version**: 2.0 (OpenAMI Architecture Aligned)
**Last Updated**: 2025-10-02
**Status**: 📋 Specification (Updated for 4-Layer Architecture)

## Purpose

Define the architecture, data contracts, and integration points for the `compliance` module backend and its pluggable Compliance MCP server. The goal is to align implementation with:
- The **OpenAMI 4-Layer Architecture** (Foundation → Operational → Intelligence → Governance)
- **Layer 0 Axioms** and **Compliance Manifest ($\mathcal{CM}$)** primitives
- **SPN-based compliance enforcement** and **CST-based provenance**
- The **8-Step Evolution Protocol** with compliance checkpoints
- Established `base/backend` patterns (Pydantic data models, service layer abstractions, FastMCP servers)
- Compliance insights documented in `/docs/openami/`, `compliance/docs/consolidated/`, and `learning/`

## OpenAMI Architecture Context

The compliance backend implements **Layer 4: Governance** of the OpenAMI architecture:

### Four-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 4: GOVERNANCE (Compliance Module)                     │
│ - Compliance Manifest ($\mathcal{CM}$)                      │
│ - Layer 0 Axioms enforcement                                │
│ - Human oversight + regulatory reporting                    │
│ - Never-Jettison Guarantee verification                     │
└─────────────────────────────────────────────────────────────┘
         ↕ Compliance checks, evidence collection
┌─────────────────────────────────────────────────────────────┐
│ Layer 3: INTELLIGENCE (Self-Evolution Engine)               │
│ - 8-Step Evolution Protocol (Analyze → Activate)            │
│ - ML/AI model selection, fine-tuning                        │
│ - Proof generation (Lean/Coq integration)                   │
└─────────────────────────────────────────────────────────────┘
         ↕ SPNs enforce compliance at every step
┌─────────────────────────────────────────────────────────────┐
│ Layer 2: OPERATIONAL (SDS - Secure Distributed System)      │
│ - SPNs (Secure Process Nodes) with compliance checks        │
│ - CSTs (Cryptographic State Tokens) for provenance          │
│ - OAMI Protocol for secure inter-component communication    │
└─────────────────────────────────────────────────────────────┘
         ↕ Built on foundational guarantees
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: FOUNDATION                                          │
│ - Layer 0 Axioms (immutable safety constraints)             │
│ - Genesis Kernel (core execution principles)                │
│ - Formal proof checker (Lean/Coq)                           │
└─────────────────────────────────────────────────────────────┘
```

### Never-Jettison Guarantee

The compliance backend ensures that **AI_v1000 must still prove compliance with ORIGINAL Layer 0 axioms**, preventing value drift across self-evolution generations. This is verified through:
- Immutable hash anchoring of Layer 0 Axioms in Compliance Manifest
- CST-based provenance chains linking every evolution to original axioms
- Formal verification proofs maintained across versions

## Target Capabilities

### Core OpenAMI Compliance Primitives

1. **Compliance Manifest ($\mathcal{CM}$) Management**
   - Maintains the authoritative Compliance Manifest with immutable and updateable sections
   - **Immutable Sections**: Layer 0 Axioms, Genesis Kernel, Proof Checker configuration
   - **Updateable Sections**: Evolutionary directives, compliance constraints (with proof of safety)
   - Multi-party signature verification and immutable hash anchoring
   - Version management ensuring Never-Jettison Guarantee

2. **Layer 0 Axioms Enforcement**
   - Stores formalized safety axioms (encoded in Lean/Coq)
   - Provides axiom validation API for SPNs before operation execution
   - Tracks axiom violations and triggers incident response (EU AI Act Article 73)
   - Maintains immutable axiom provenance across system evolution

3. **SPN (Secure Process Node) Compliance Integration**
   - Wraps existing modules as SPNs with pre/post compliance checks
   - Enforces compliance constraints at Layer 2 (Operational) boundary
   - Blocks operations that would violate Layer 0 Axioms
   - Generates compliance evidence for every SPN execution

4. **CST (Cryptographic State Token) Provenance**
   - Creates signed state snapshots linking operations to Compliance Manifest version
   - Maintains cryptographic proof chains for audit trail (EU AI Act Article 12)
   - Enables rollback to compliant states on axiom violations
   - Provides evidence for "Never-Jettison" guarantee verification

5. **8-Step Evolution Protocol Compliance**
   - Integrates compliance checkpoints at each evolution step:
     1. **Analyze**: Verify proposed changes don't conflict with Layer 0 Axioms
     2. **Design**: Check architectural changes maintain compliance manifest
     3. **Compile**: Validate generated code against safety constraints
     4. **Test**: Run compliance test suite on evolved components
     5. **Prove**: Generate Lean/Coq proofs of safety properties
     6. **Verify**: External verification of proofs and evidence
     7. **Log**: Record evolution in CST chain with compliance attestation
     8. **Activate**: Final axiom check before deployment
   - Blocks evolution pipeline on compliance failure at any step

### Traditional Compliance Capabilities

6. **Unified Compliance State API**
   - Collects attestations, control coverage, and risk findings mapped to EU AI Act, ISO/IEC 42001, ISO/IEC 27001, and NIST AI RMF requirements (see `compliance/docs/consolidated`).
   - Stores evaluations and evidence pointers in structured Pydantic models for persistence via the Base DataOps layer.
   - Integrates with OpenAMI architecture evidence (SPNs, CSTs, formal proofs)

7. **Pluggable MCP Server**
   - Ships as `compliance/backend/mcp/compliance_server.py`, extending `base.backend.mcp.fastmcp_server_base.FastMCPServerBase`.
   - Provides tools for retrieving control status, submitting evidence, triggering gap analyses, and exporting audit packets.
   - Exposes Compliance Manifest API, Layer 0 Axiom validation, and SPN compliance checking.
   - Designed so new tools can be registered by dropping modules under `compliance/backend/mcp/tools/`.

8. **Control & Evidence Registry**
   - Maintains canonical control definitions linked to consolidated documentation and Blueprint references.
   - Supports evidence attachment (file pointers, Git references, orchestration logs, CST chains, formal proofs).
   - Lifecycle metadata (owner, review cadence, expiry) with automated compliance status updates.

9. **Risk & Incident Workflow**
   - Provides services to log risk assessments, Article 73 incident notifications, and Clause 10.2 corrective actions.
   - Integrates with Base audit logging (`base/backend/dataops/security/audit_trail.py`) for immutable traceability.
   - Automated serious incident detection based on Layer 0 Axiom violations.
   - Calculates reporting deadlines (15/10/2 days) based on incident severity (EU AI Act Article 73).

## Proposed Directory Layout

```
compliance/backend/
  __init__.py
  config/
    compliance_settings.py        # Settings model mirroring base config style

  # OpenAMI Architecture Models (NEW)
  models/
    __init__.py
    # Layer 1: Foundation primitives
    layer0_axioms.py              # Layer 0 Axioms schema (Lean/Coq integration)
    genesis_kernel.py             # Genesis Kernel principles
    compliance_manifest.py        # Compliance Manifest ($\mathcal{CM}$) schema

    # Layer 2: Operational primitives
    spn.py                        # SPN compliance check models
    cst.py                        # CST provenance token models

    # Traditional compliance models
    controls.py                   # Pydantic models for controls/requirements
    evidence.py                   # Evidence entries (Git, CST, proofs, logs)
    risk.py                       # Risk assessment, incident, corrective action

    # 8-Step Evolution Protocol
    evolution.py                  # Evolution step compliance checkpoints

  repositories/
    __init__.py
    compliance_store.py           # DataOps-backed persistence helpers
    manifest_store.py             # Compliance Manifest versioning (NEW)
    axiom_store.py                # Layer 0 Axioms storage (NEW)
    cst_store.py                  # CST chain persistence (NEW)

  services/
    __init__.py
    # Core OpenAMI services (NEW)
    manifest_service.py           # Compliance Manifest CRUD + version management
    axiom_service.py              # Layer 0 Axioms validation + enforcement
    spn_service.py                # SPN compliance wrapper generation
    cst_service.py                # CST creation + verification
    evolution_service.py          # 8-step protocol compliance orchestration
    proof_service.py              # Lean/Coq proof verification integration

    # Traditional compliance services
    control_service.py            # CRUD + status aggregation for controls
    risk_service.py               # Risk lifecycle + Article 73 helpers
    evidence_service.py           # Evidence attachment & validation

  mcp/
    __init__.py
    compliance_server.py          # FastMCP server implementation
    tools/
      __init__.py
      # OpenAMI tools (NEW)
      get_compliance_manifest.py  # Retrieve current $\mathcal{CM}$ version
      validate_axiom.py           # Check operation against Layer 0 Axioms
      verify_never_jettison.py    # Verify Never-Jettison Guarantee
      get_cst_chain.py            # Retrieve CST provenance chain
      check_evolution_step.py     # Validate evolution protocol compliance

      # Traditional tools
      get_control.py              # Expose control metadata/status
      list_gaps.py                # Return outstanding gaps
      submit_evidence.py          # Register evidence items
      export_audit_packet.py      # Download structured compliance report

  # Formal verification integration (NEW)
  verification/
    __init__.py
    lean_integration.py           # Lean theorem prover integration
    coq_integration.py            # Coq proof assistant integration
    proof_checker.py              # Unified proof verification interface
```

## Data Model Guidelines

### General Principles

- Use `pydantic.BaseModel` subclasses with `ConfigDict(extra="forbid")` for strict validation (matching `base/backend/dataops` style).
- All models must be JSON-serializable for storage via UnifiedCRUD.
- Reference consolidated documentation with `doc_path: str` attributes (e.g., `"consolidated/ISO_42001/support/support.md"`).
- Include cryptographic integrity fields (`hash`, `signature`) for audit trail compliance (EU AI Act Article 12).

### OpenAMI Architecture Models

#### 1. Compliance Manifest ($\mathcal{CM}$)

```python
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from datetime import datetime

class Layer0Axioms(BaseModel):
    """Immutable safety constraints (EU AI Act Article 9 fundamentals)"""
    axiom_id: str
    formal_spec: str              # Lean/Coq theorem statement
    natural_language: str         # Human-readable description
    regulatory_source: str        # e.g., "EU_AI_Act_Article_9_4_a"
    proof_required: bool = True

    class Config:
        frozen = True  # Immutable

class GenesisKernel(BaseModel):
    """Core execution principles from Gemini DSE-AI"""
    principle_id: str
    description: str
    justification_triad_required: bool  # Hypothesis, Trigger, Verification

    class Config:
        frozen = True  # Immutable

class EvolutionaryDirective(BaseModel):
    """Updateable goals for self-evolution"""
    directive_id: str
    goal: str
    priority: int
    constraints: List[str]        # References to compliance_constraints
    added_at: datetime
    proof_of_safety: str          # Reference to Lean/Coq proof

class ComplianceConstraint(BaseModel):
    """Updateable ethical/legal rules"""
    constraint_id: str
    rule: str
    regulatory_basis: str         # e.g., "ISO_42001_Clause_8_3"
    enforcement_level: str        # "BLOCK" | "WARN" | "LOG"
    added_at: datetime
    proof_of_non_conflict: str    # Proof it doesn't conflict with Layer 0

class Signature(BaseModel):
    """Multi-party signature for Compliance Manifest"""
    signer: str                   # Role: "Security Lead", "Legal", "CTO"
    public_key: str
    signature: str
    timestamp: datetime

class ComplianceManifest(BaseModel):
    """
    Authoritative compliance specification for the system.
    Implements Never-Jettison Guarantee through immutable_hash.
    """
    # IMMUTABLE SECTIONS (Never modified)
    layer0_axioms: List[Layer0Axioms]
    genesis_kernel: List[GenesisKernel]
    layer0_verifier_config: Dict[str, Any]  # Lean/Coq checker setup

    # UPDATEABLE SECTIONS (With proof of safety)
    evolutionary_directives: List[EvolutionaryDirective]
    compliance_constraints: List[ComplianceConstraint]

    # METADATA
    version: str                  # Semantic version
    created_at: datetime
    signatures: List[Signature]   # Multi-party approval
    immutable_hash: str           # SHA-256 of layer0_axioms + genesis_kernel
    previous_version: str | None  # For version chain

    def verify_never_jettison(self, original_manifest: "ComplianceManifest") -> bool:
        """Verify this version maintains original immutable sections"""
        return self.immutable_hash == original_manifest.immutable_hash
```

#### 2. SPN (Secure Process Node) Models

```python
class SPNComplianceCheck(BaseModel):
    """Compliance validation result for SPN operation"""
    check_id: str
    spn_name: str
    operation: str                # Function being executed
    timestamp: datetime

    # Compliance validation
    axioms_checked: List[str]     # Layer 0 Axiom IDs
    passed: bool
    violations: List[str] = []    # Axiom IDs that failed

    # Evidence
    input_state_hash: str
    output_state_hash: str
    cst_id: str | None            # Link to CST if created
    proof_reference: str | None   # Lean/Coq proof if required

    # Incident tracking
    incident_triggered: bool = False
    incident_severity: str | None  # "SERIOUS" | "CRITICAL" per Article 73

class SPNWrapper(BaseModel):
    """Configuration for wrapping module as SPN with compliance"""
    spn_id: str
    module_path: str              # e.g., "base.backend.dataops.crud"
    wrapped_functions: List[str]

    # Compliance configuration
    pre_check_axioms: List[str]   # Axioms to verify before execution
    post_check_axioms: List[str]  # Axioms to verify after execution
    requires_proof: bool = False  # Whether formal proof is needed
    evidence_collection: bool = True

    # CST configuration
    create_cst_on_success: bool = True
    cst_includes_output: bool = False  # Privacy consideration
```

#### 3. CST (Cryptographic State Token) Models

```python
class CSTProvenance(BaseModel):
    """Provenance chain entry linking operation to Compliance Manifest"""
    parent_cst_id: str | None     # Previous CST in chain (None for genesis)
    compliance_manifest_version: str
    compliance_manifest_hash: str  # Proves which axioms applied
    operation_type: str           # "DATA_ACCESS", "MODEL_UPDATE", "EVOLUTION_STEP"
    spn_id: str
    timestamp: datetime

class CST(BaseModel):
    """
    Cryptographic State Token - signed snapshot for audit trail.
    Implements EU AI Act Article 12 logging requirements.
    """
    cst_id: str                   # UUID
    timestamp: datetime

    # State snapshot
    state_hash: str               # SHA-256 of relevant state
    state_description: str        # Human-readable summary

    # Provenance
    provenance: CSTProvenance

    # Compliance attestation
    compliance_check_id: str      # Link to SPNComplianceCheck
    axioms_satisfied: List[str]   # Layer 0 Axiom IDs

    # Cryptographic integrity
    signature: str                # Signed by system private key
    previous_cst_hash: str | None # Blockchain-style chain

    def verify_chain(self, previous_cst: "CST") -> bool:
        """Verify CST chain integrity"""
        import hashlib
        expected_hash = hashlib.sha256(
            f"{previous_cst.cst_id}{previous_cst.signature}".encode()
        ).hexdigest()
        return self.previous_cst_hash == expected_hash
```

#### 4. 8-Step Evolution Protocol Models

```python
from enum import Enum

class EvolutionStep(str, Enum):
    ANALYZE = "analyze"
    DESIGN = "design"
    COMPILE = "compile"
    TEST = "test"
    PROVE = "prove"
    VERIFY = "verify"
    LOG = "log"
    ACTIVATE = "activate"

class EvolutionStepCheckpoint(BaseModel):
    """Compliance checkpoint for each evolution step"""
    step: EvolutionStep
    timestamp: datetime

    # Compliance validation
    compliance_check_id: str
    passed: bool
    blocking_issues: List[str] = []

    # Evidence
    artifacts: List[str]          # Paths to generated code, proofs, test results
    cst_id: str | None

    # Step-specific data
    step_metadata: Dict[str, Any]

class EvolutionPipeline(BaseModel):
    """Complete evolution pipeline with compliance tracking"""
    pipeline_id: str
    started_at: datetime
    completed_at: datetime | None

    # What's being evolved
    target_component: str
    evolution_goal: str
    directive_id: str             # Link to EvolutionaryDirective

    # Compliance context
    compliance_manifest_version: str

    # Step tracking
    checkpoints: List[EvolutionStepCheckpoint]
    current_step: EvolutionStep | None
    pipeline_status: str          # "IN_PROGRESS" | "BLOCKED" | "COMPLETED" | "FAILED"

    # Final attestation
    never_jettison_verified: bool = False
    final_cst_id: str | None
    deployment_approved: bool = False
```

### Traditional Compliance Models

#### 5. Control Models

```python
class Control(BaseModel):
    """Regulatory control/requirement"""
    control_id: str               # e.g., "ISO27001-6.1.3"
    title: str
    source_standard: str          # "EU_AI_Act" | "ISO_42001" | "ISO_27001" | "NIST_AI_RMF"
    requirement_summary: str
    doc_path: str                 # Link to consolidated docs

    # Implementation
    implementation_status: str    # "NOT_STARTED" | "IN_PROGRESS" | "OPERATIONAL" | "EVIDENCE_REQUIRED"

    # OpenAMI integration (NEW)
    layer0_axiom_refs: List[str] = []      # Which axioms enforce this
    spn_enforcement_points: List[str] = [] # Which SPNs check this

    # Evidence
    evidence_refs: List[str] = [] # Evidence IDs (CSTs, proofs, files)

    # Lifecycle
    owner: str
    review_cadence_days: int
    last_reviewed: datetime | None
    next_review: datetime | None

class EvidenceRef(BaseModel):
    """Reference to compliance evidence"""
    evidence_id: str
    source_type: str              # "GIT_COMMIT" | "CST" | "PROOF" | "FILE" | "RUN_LOG"
    location: str                 # URI, CST ID, Git SHA, etc.
    hash_or_version: str
    submitted_by: str
    submitted_at: datetime
    validation_state: str         # "PENDING" | "VALIDATED" | "REJECTED"
    controls_satisfied: List[str] # Control IDs this evidence supports
```

#### 6. Risk & Incident Models

```python
class Risk(BaseModel):
    """Risk assessment per EU AI Act Article 9, ISO 42001 Clause 8"""
    risk_id: str
    description: str
    category: str                 # "BIAS", "PRIVACY", "SAFETY", "SECURITY", "TRANSPARENCY"

    # Assessment
    likelihood: str               # "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"
    impact: str                   # "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"
    residual_risk: str            # After controls applied

    # Treatment
    treatment_plan: str
    status: str                   # "IDENTIFIED" | "TREATING" | "ACCEPTED" | "MITIGATED"

    # OpenAMI integration (NEW)
    related_axioms: List[str] = []         # Layer 0 Axioms addressing this risk
    mitigation_controls: List[str] = []    # Control IDs

class Incident(BaseModel):
    """
    Serious incident per EU AI Act Article 73.
    Triggered automatically on Layer 0 Axiom violations.
    """
    incident_id: str
    timestamp: datetime
    severity: str                 # "SERIOUS" | "CRITICAL"

    # Violation details
    violated_axioms: List[str]    # Layer 0 Axiom IDs
    spn_id: str                   # Where violation occurred
    compliance_check_id: str

    # Provenance
    cst_chain: List[str]          # CST IDs leading to violation

    # Regulatory reporting (Article 73)
    reporting_deadline: datetime  # 15/10/2 days based on severity
    notified_authorities: List[str] = []
    notification_timestamps: Dict[str, datetime] = {}

    # Resolution
    root_cause: str | None
    corrective_actions: List[str] = []  # Corrective action IDs
    resolved_at: datetime | None
    resolution_cst_id: str | None # CST proving resolution
```

## MCP Server Contract

### OpenAMI Architecture Tools (NEW)

#### Tool: `compliance.get_compliance_manifest`
- **Inputs:** `version` (optional, defaults to latest)
- **Outputs:** Serialized `ComplianceManifest` with Layer 0 Axioms, Genesis Kernel, and version metadata
- **Purpose:** Retrieve current or historical Compliance Manifest for audit trail

#### Tool: `compliance.validate_axiom`
- **Inputs:** `operation_descriptor` (JSON describing operation), `axiom_ids` (optional, defaults to all)
- **Outputs:** Validation result with passed/failed axioms and violation details
- **Flow:**
  1. Load current Compliance Manifest
  2. Retrieve specified axioms (or all Layer 0 Axioms)
  3. Execute formal verification check (Lean/Coq integration)
  4. Return validation result with evidence references
- **Purpose:** Pre-flight check for SPN operations, evolution steps

#### Tool: `compliance.verify_never_jettison`
- **Inputs:** `current_version`, `original_version` (optional, defaults to v1.0.0)
- **Outputs:** Verification result with immutable_hash comparison and provenance chain
- **Flow:**
  1. Load both Compliance Manifest versions
  2. Compare immutable_hash values
  3. Trace version chain from original to current
  4. Return detailed verification report
- **Purpose:** Prove Never-Jettison Guarantee for AI_v1000+ versions

#### Tool: `compliance.get_cst_chain`
- **Inputs:** `cst_id` or `spn_id` or `time_range`
- **Outputs:** Array of CSTs with provenance chains
- **Flow:**
  1. Query CST store by specified filter
  2. Reconstruct chain back to genesis CST
  3. Verify cryptographic integrity of each link
  4. Return chain with compliance attestations
- **Purpose:** Audit trail reconstruction, incident investigation

#### Tool: `compliance.check_evolution_step`
- **Inputs:** `pipeline_id`, `step` (EvolutionStep enum), `artifacts` (JSON)
- **Outputs:** Checkpoint validation result
- **Flow:**
  1. Load evolution pipeline and Compliance Manifest
  2. Execute step-specific compliance checks:
     - **Analyze**: Check proposed changes against Layer 0 Axioms
     - **Design**: Validate architecture maintains compliance
     - **Compile**: Scan generated code for safety violations
     - **Test**: Run compliance test suite
     - **Prove**: Verify Lean/Coq proofs
     - **Verify**: External proof validation
     - **Log**: Create CST with evolution evidence
     - **Activate**: Final axiom validation before deployment
  3. Create EvolutionStepCheckpoint
  4. Update pipeline status
  5. Return checkpoint with blocking issues (if any)
- **Purpose:** Orchestrate 8-step evolution protocol with compliance gates

#### Tool: `compliance.wrap_spn`
- **Inputs:** `module_path`, `functions`, `axiom_config` (JSON)
- **Outputs:** SPN wrapper configuration
- **Flow:**
  1. Validate module exists and functions are wrappable
  2. Create SPNWrapper configuration
  3. Register pre/post compliance checks
  4. Generate wrapper code (decorator/proxy pattern)
  5. Store SPN metadata
  6. Return wrapper configuration
- **Purpose:** Convert existing modules to SPNs with compliance enforcement

### Traditional Compliance Tools

#### Tool: `compliance.get_control`
- **Inputs:** `control_id`
- **Outputs:** Serialized `Control` model with evidence summary, doc references, and OpenAMI integration (axiom refs, SPN enforcement points)

#### Tool: `compliance.list_gaps`
- **Inputs:** Optional filters (`standard`, `status`, `module`)
- **Outputs:** Array of open gaps sourced from `COMPLIANCE_GAP_ANALYSIS.md` and live data, with OpenAMI implementation suggestions

#### Tool: `compliance.submit_evidence`
- **Inputs:** `control_id`, `evidence_ref` (supports CST, PROOF, traditional types)
- **Flow:**
  1. Validate control exists
  2. Validate evidence reference (CST chain integrity, proof verification, etc.)
  3. Persist evidence via `EvidenceService`
  4. Update control implementation status
  5. Log via Base audit chain
  6. Create CST for evidence submission
  7. Return updated control snapshot
- **Purpose:** Link evidence (CSTs, proofs, files) to regulatory controls

#### Tool: `compliance.export_audit_packet`
- **Inputs:** `standard`, `timeframe` (optional), `include_openami` (boolean, default True)
- **Outputs:** Structured report (JSON) bundling:
  - Control statuses and evidence references
  - Outstanding actions and gaps
  - **OpenAMI additions**: Compliance Manifest version, CST chains, Layer 0 Axiom compliance summary, Never-Jettison verification
- **Purpose:** Generate regulator-ready audit package with full provenance

### Transport & Deployment
- Server derives from `FastMCPServerBase` to inherit auth, logging, and lifecycle hooks.
- Provide `run_mcp.py` entrypoint mirroring Base modules, using configuration from `.env`/`compliance/default.env`.
- Document CLI usage in `compliance/README.md` after implementation.

## Integration Requirements

### OpenAMI Architecture Integration

1. **Layer 0 Axioms Integration:**
   - Axioms stored in `compliance/backend/models/layer0_axioms.py` with formal specs (Lean/Coq)
   - Loaded at system startup into memory for fast validation
   - Immutable once Compliance Manifest is signed
   - Integration with formal verification tools via `compliance/backend/verification/`

2. **Compliance Manifest Versioning:**
   - Stored in dedicated `manifest_store.py` with full version history
   - Immutable sections hashed and anchored at creation
   - Never-Jettison verification enforced on every version update
   - Multi-party signature validation before persisting new versions

3. **SPN Integration:**
   - Every existing module can be wrapped as SPN via `spn_service.py`
   - Pre/post compliance checks injected using decorator pattern
   - Automatic CST creation on successful operations
   - Blocking behavior on Layer 0 Axiom violations (raises exception)

4. **CST Chain Persistence:**
   - CSTs stored in `cst_store.py` with blockchain-style linking
   - Chain integrity verified on read operations
   - Indexed by `cst_id`, `spn_id`, `timestamp`, `compliance_manifest_version`
   - Retention policy: 10 years minimum (EU AI Act Article 12 requirement)

5. **8-Step Evolution Protocol Integration:**
   - Evolution pipelines orchestrated by `evolution_service.py`
   - Each step creates checkpoint with compliance validation
   - Pipeline blocked if any step fails compliance checks
   - Final "Activate" step requires human approval + Never-Jettison verification

6. **Formal Verification Integration:**
   - `proof_service.py` provides unified interface to Lean/Coq
   - Proofs stored as evidence alongside CSTs
   - Proof verification required for:
     - Layer 0 Axiom formalization (initial + updates)
     - Compliance Manifest updateable section changes
     - High-risk evolution steps (core algorithm changes)

### Base Module Integration

7. **Audit Logging:** Every mutating action must:
   - Call `base.backend.dataops.security.audit_trail.audit_log` to append to blockchain-based audit chain
   - Create CST via `cst_service.py` with reference to audit log entry
   - Link to current Compliance Manifest version

8. **DataOps Persistence:** Repositories should leverage:
   - `base.backend.dataops.core.dao.DAOFactory` for storage (PostgreSQL for relational, Dgraph for graph queries)
   - All compliance models (including OpenAMI primitives) stored via UnifiedCRUD
   - CST chain stored in high-performance backend (Redis/Dgraph) for fast traversal

9. **Configuration:** Align with Base config pattern using `pydantic-settings`:
   - `COMPLIANCE_STORAGE_BACKEND` - storage backend selection
   - `COMPLIANCE_DEFAULT_STANDARD_SET` - default regulatory frameworks
   - `COMPLIANCE_MANIFEST_PATH` - path to signed Compliance Manifest
   - `LEAN_EXECUTABLE_PATH` - path to Lean theorem prover
   - `COQ_EXECUTABLE_PATH` - path to Coq proof assistant
   - `CST_RETENTION_DAYS` - CST retention period (default: 3650 = 10 years)

10. **Blueprint Mapping:** Keep `compliance/docs/consolidated/blueprint` as the canonical mapping:
    - Backend loads blueprint at startup to seed control catalogs
    - Augmented with OpenAMI mappings (Layer 0 Axioms → Controls)
    - Used to auto-generate compliance dashboards

11. **Testing Pattern:** Mirror Base test layout (`tests/` with pytest + async fixtures):
    - Contract tests for MCP tools
    - Repository/service layer tests
    - **OpenAMI additions**:
      - Layer 0 Axiom validation tests (with mock Lean/Coq)
      - CST chain integrity tests
      - SPN wrapper compliance tests
      - Never-Jettison verification tests
      - 8-step evolution protocol integration tests

## Implementation Roadmap

**Timeline**: Q4 2025 - Q2 2026 (aligned with EXECUTIVE_ACTION_PLAN.md)
**Resources**: 1.5 FTE engineering + 0.5 FTE formal verification specialist

### Phase 0: Foundation (Q4 2025, Weeks 1-4)

**Goal**: Establish OpenAMI architecture foundations before backend implementation

1. **Week 1-2: Layer 0 Axioms Formalization**
   - Encode EU AI Act Article 9 requirements as formal axioms (Lean/Coq)
   - Define Genesis Kernel principles from Gemini DSE-AI
   - Create axiom validation test suite
   - **Deliverable**: `layer0_axioms.lean`, `genesis_kernel.lean`

2. **Week 3-4: Compliance Manifest Schema**
   - Implement Pydantic models for Compliance Manifest
   - Design multi-party signature workflow
   - Create immutable hash anchoring mechanism
   - Implement Never-Jettison verification logic
   - **Deliverable**: `compliance/backend/models/compliance_manifest.py`, initial signed $\mathcal{CM}$ v1.0.0

### Phase 1: Core OpenAMI Backend (Q4 2025, Weeks 5-8)

**Goal**: Implement Layer 1 (Foundation) and Layer 2 (Operational) primitives

3. **Week 5: Proof Verification Integration**
   - Implement Lean integration (`lean_integration.py`)
   - Implement Coq integration (`coq_integration.py`)
   - Create unified `proof_service.py` interface
   - **Deliverable**: Working proof verification pipeline

4. **Week 6: CST Implementation**
   - Implement CST models (`cst.py`)
   - Create `cst_store.py` with blockchain-style storage
   - Implement CST chain verification
   - **Deliverable**: Operational CST creation and verification

5. **Week 7: SPN Abstraction Layer**
   - Design SPN wrapper architecture
   - Implement `spn_service.py` with decorator/proxy pattern
   - Create SPN compliance check models
   - **Deliverable**: Ability to wrap existing modules as SPNs

6. **Week 8: Axiom Enforcement Service**
   - Implement `axiom_service.py` with Layer 0 validation
   - Integrate with proof verification
   - Create incident detection on axiom violations
   - **Deliverable**: Operational axiom enforcement

### Phase 2: Evolution Protocol & MCP Server (Q4 2025, Weeks 9-12)

**Goal**: Implement 8-step evolution protocol and expose via MCP

7. **Week 9: Evolution Protocol Models**
   - Implement evolution models (`evolution.py`)
   - Create `evolution_service.py` orchestrator
   - Define compliance checkpoints for each step
   - **Deliverable**: Evolution pipeline infrastructure

8. **Week 10: MCP Server Scaffolding**
   - Create `compliance_server.py` extending FastMCPServerBase
   - Implement OpenAMI tools:
     - `get_compliance_manifest`
     - `validate_axiom`
     - `verify_never_jettison`
     - `get_cst_chain`
   - **Deliverable**: Operational OpenAMI compliance MCP server

9. **Week 11: Evolution Step Checker**
   - Implement `check_evolution_step` MCP tool
   - Integrate step-specific compliance validation
   - Create blocking mechanism for failed steps
   - **Deliverable**: Complete 8-step protocol enforcement

10. **Week 12: SPN Wrapper Tool**
    - Implement `wrap_spn` MCP tool
    - Auto-generate wrapper code
    - Create SPN catalog and discovery
    - **Deliverable**: Self-service SPN creation

### Phase 3: Traditional Compliance Integration (Q1 2026, Weeks 13-20)

**Goal**: Integrate OpenAMI with traditional compliance workflows

11. **Week 13-14: Control & Evidence Models**
    - Implement traditional compliance models (controls, evidence, risk)
    - Augment with OpenAMI fields (layer0_axiom_refs, spn_enforcement_points)
    - Create `control_service.py`, `evidence_service.py`, `risk_service.py`
    - **Deliverable**: Unified compliance data models

12. **Week 15-16: Traditional MCP Tools**
    - Implement `get_control`, `list_gaps`, `submit_evidence`
    - Update tools to accept CST and PROOF evidence types
    - Integrate with CST chain creation
    - **Deliverable**: Complete MCP tool suite

13. **Week 17-18: Incident Management**
    - Implement Article 73 incident detection (auto-trigger on axiom violations)
    - Create reporting deadline calculator (15/10/2 days)
    - Integrate with `risk_service.py`
    - **Deliverable**: Automated incident response workflow

14. **Week 19-20: Blueprint Integration**
    - Load consolidated docs and blueprint mappings
    - Auto-populate control catalog
    - Create OpenAMI → Regulatory requirement mappings
    - Seed initial evidence from existing implementations
    - **Deliverable**: Complete control catalog with OpenAMI integration

### Phase 4: Audit & Reporting (Q1-Q2 2026, Weeks 21-26)

**Goal**: Enable external audits and regulatory reporting

15. **Week 21-22: Audit Packet Generator**
    - Implement `export_audit_packet` with OpenAMI additions
    - Generate CST chain exports
    - Include Never-Jettison verification reports
    - Create formal proof package
    - **Deliverable**: Regulator-ready audit packages

16. **Week 23-24: Evidence Collection Automation**
    - Auto-generate evidence from SPNs (execution logs → CSTs)
    - Extract evidence from Git commits
    - Link test results to controls
    - **Deliverable**: Continuous evidence collection

17. **Week 25: Testing & Documentation**
    - Comprehensive test suite (unit, integration, contract tests)
    - OpenAMI-specific tests (axiom validation, CST integrity, Never-Jettison)
    - MCP tool contract tests
    - Update `compliance/README.md` with usage guide
    - **Deliverable**: Production-ready compliance backend

18. **Week 26: External Audit Preparation**
    - Generate sample audit packets for all frameworks
    - Prepare evidence bundles
    - Document compliance architecture for auditors
    - Conduct dry-run with mock auditor
    - **Deliverable**: Audit-ready compliance system

### Success Criteria

- ✅ All Layer 0 Axioms formalized and verifiable in Lean/Coq
- ✅ Compliance Manifest v1.0.0 signed and deployed
- ✅ CST chain operational with 10-year retention
- ✅ At least 3 critical modules wrapped as SPNs
- ✅ 8-step evolution protocol enforced for all system changes
- ✅ Never-Jettison Guarantee verifiable programmatically
- ✅ Audit packet export generates complete provenance chains
- ✅ All MCP tools operational and documented
- ✅ 90%+ test coverage including OpenAMI components
- ✅ External audit dry-run completed successfully

## Dependencies & Open Questions

### Resolved via OpenAMI Architecture

✅ **Storage Backend**:
- PostgreSQL for relational compliance data (controls, evidence refs, risks)
- Dgraph for CST chain traversal and provenance queries
- Redis for Layer 0 Axioms in-memory cache (fast validation)

✅ **Evidence Storage**:
- CSTs: Stored in compliance backend with signature verification
- Proofs: Stored as files with hash references in evidence models
- Traditional evidence: Git commits (SHA references), file URIs, orchestration logs

✅ **Access Control**:
- Multi-party signature required for Compliance Manifest updates
- Role-based access for MCP tools:
  - Read operations: Any authenticated user
  - Evidence submission: Evidence Submitter role
  - Compliance Manifest updates: Compliance Manager + Legal + CTO signatures
  - Evolution step approval: Security Lead + Human Overseer

### Open Questions Requiring Decisions

1. **Lean vs Coq Primary Prover**:
   - Both will be supported, but which should be default for Layer 0 Axioms?
   - **Recommendation**: Lean 4 (modern, faster, better tooling)
   - **Decision Required By**: Week 1 (before axiom formalization)

2. **CST Signature Algorithm**:
   - Ed25519 (fast, modern) vs RSA-4096 (traditional, widely supported)
   - **Recommendation**: Ed25519 for performance, RSA-4096 for Compliance Manifest
   - **Decision Required By**: Week 6 (before CST implementation)

3. **SPN Performance Overhead**:
   - Every operation requires compliance check - what's acceptable latency?
   - **Options**:
     - Aggressive caching of axiom validation results
     - Async compliance checks for non-critical operations
     - Batched CST creation
   - **Decision Required By**: Week 7 (before SPN design)

4. **Evolution Protocol Human Approval**:
   - Which steps require human-in-the-loop approval?
   - **Recommendation**: "Activate" step always requires approval; "Prove" step for high-risk changes
   - **Decision Required By**: Week 9 (before evolution protocol implementation)

5. **External Auditor Integration**:
   - Should compliance backend expose APIs directly to external auditors?
   - **Recommendation**: Export audit packet only (no direct API access to avoid attack surface)
   - **Decision Required By**: Week 21 (before audit packet implementation)

6. **Formal Verification Specialist Hiring**:
   - In-house hire vs consulting arrangement?
   - **Recommendation**: In-house 0.5 FTE (critical for long-term maintenance)
   - **Decision Required By**: October 23, 2025 (per EXECUTIVE_ACTION_PLAN.md)

### Dependencies on External Systems

- **Lean Theorem Prover**: Installation and integration (Phase 0, Week 5)
- **Coq Proof Assistant**: Installation and integration (Phase 0, Week 5)
- **Base Module UnifiedCRUD**: Must support CST storage patterns (already operational ✅)
- **Base Module Audit Trail**: Blockchain-based logging operational (already operational ✅)
- **OpenAMI Documentation**: System architecture docs complete (already operational ✅)

### Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Lean/Coq integration complexity | HIGH | Hire formal verification specialist (0.5 FTE) |
| SPN performance overhead | MEDIUM | Implement aggressive caching, async checks |
| Compliance Manifest governance | HIGH | Multi-party signature workflow enforced |
| CST storage scaling | MEDIUM | Use Dgraph for graph traversal, Redis cache |
| Evolution protocol adoption | MEDIUM | Excellent documentation + tooling support |

---

## Document Maintenance

**Version**: 2.0 (OpenAMI Architecture Aligned)
**Last Updated**: 2025-10-02
**Next Review**: After Phase 0 completion (Q4 2025, Week 4)

This specification should be updated as implementation progresses. All documentation updates must stay synchronized with:
- `/docs/openami/architecture/` - OpenAMI architecture documentation
- `compliance/docs/consolidated/` - Regulatory requirement mappings
- `compliance/docs/research/OPENAMI-COMPLIANCE-MAPPING.md` - Traceability matrix
- Actual code shipped under `compliance/backend/`

**Change Log**:
- **2025-10-02 (v2.0)**: Major update for OpenAMI architecture alignment
  - Added Layer 0 Axioms, Compliance Manifest, SPN, CST models
  - Added 8-step evolution protocol integration
  - Added formal verification requirements (Lean/Coq)
  - Updated MCP tools for OpenAMI primitives
  - Aligned implementation roadmap with EXECUTIVE_ACTION_PLAN.md (Q4 2025 - Q2 2026)
  - Added Never-Jettison Guarantee verification
- **[Previous version]**: Initial spec for traditional compliance backend
