# Compliance Module

**Version**: 2.0 (OpenAMI Architecture Integrated)
**Status**: 📋 Specification Phase → 🛠️ Implementation Starting Q4 2025
**Owner**: Compliance Working Group

---

## Overview

The **Compliance Module** implements **Layer 4: Governance** of the OpenAMI architecture, providing:

- **Compliance Manifest ($\mathcal{CM}$)** management with Layer 0 Axioms enforcement
- **Secure Process Nodes (SPNs)** with pre/post compliance checks
- **Cryptographic State Tokens (CSTs)** for provenance and audit trails
- **8-Step Evolution Protocol** compliance gates
- **Never-Jettison Guarantee** verification ensuring AI_v1000 maintains original safety constraints
- Traditional regulatory compliance tracking (EU AI Act, ISO 42001, ISO 27001, NIST AI RMF)

This module ensures that the self-evolving AI system remains **compliant across generations**, preventing value drift while enabling continuous improvement.

---

## Table of Contents

1. [Architecture Context](#architecture-context)
2. [Key Capabilities](#key-capabilities)
3. [Directory Structure](#directory-structure)
4. [Documentation Index](#documentation-index)
5. [Getting Started](#getting-started)
6. [MCP Server Usage](#mcp-server-usage)
7. [Development Roadmap](#development-roadmap)
8. [Contributing](#contributing)

---

## Architecture Context

### OpenAMI Four-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 4: GOVERNANCE (This Module)                          │
│ ✓ Compliance Manifest ($\mathcal{CM}$)                     │
│ ✓ Layer 0 Axioms enforcement                               │
│ ✓ Human oversight + regulatory reporting                   │
│ ✓ Never-Jettison Guarantee                                 │
└─────────────────────────────────────────────────────────────┘
         ↕ Compliance checks, evidence collection
┌─────────────────────────────────────────────────────────────┐
│ Layer 3: INTELLIGENCE                                       │
│ • 8-Step Evolution Protocol (gated by compliance)           │
│ • Self-evolution engine                                     │
└─────────────────────────────────────────────────────────────┘
         ↕ SPNs enforce compliance at every step
┌─────────────────────────────────────────────────────────────┐
│ Layer 2: OPERATIONAL (SDS)                                  │
│ • SPNs with compliance pre/post checks                      │
│ • CSTs for audit trails                                     │
└─────────────────────────────────────────────────────────────┘
         ↕ Built on foundational guarantees
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: FOUNDATION                                         │
│ • Layer 0 Axioms (immutable safety constraints)             │
│ • Genesis Kernel                                            │
│ • Formal proof checker (Lean/Coq)                           │
└─────────────────────────────────────────────────────────────┘
```

**Never-Jettison Guarantee**: Ensures that even AI_v1000 proves compliance with the ORIGINAL Layer 0 axioms from v1.0.0, preventing unintended value drift across self-evolution generations.

---

## Key Capabilities

### Core OpenAMI Primitives

#### 1. Compliance Manifest ($\mathcal{CM}$)

Authoritative specification defining:
- **Immutable sections**: Layer 0 Axioms, Genesis Kernel, proof checker config
- **Updateable sections**: Evolutionary directives, compliance constraints (with proofs)
- **Version management**: Cryptographic hash anchoring, multi-party signatures
- **Never-Jettison verification**: Ensures immutable sections remain unchanged

**Status**: 📋 Specified → Implementation Q4 2025 Weeks 3-4

#### 2. Layer 0 Axioms

Formal safety constraints encoded in Lean/Coq:
- Derived from EU AI Act Article 9 (high-risk AI requirements)
- Enforced at every SPN execution
- Violations trigger automatic Article 73 incident reporting
- Immutable once signed into Compliance Manifest

**Status**: 📋 Specified → Formalization Q4 2025 Weeks 1-2

#### 3. Secure Process Nodes (SPNs)

Wrapper pattern for modules with compliance enforcement:
- Pre-condition: Validate operation against Layer 0 Axioms
- Execution: Run original module function
- Post-condition: Verify output satisfies axioms
- Evidence: Create CST on success, block + incident on violation

**Status**: 📋 Specified → Implementation Q4 2025 Weeks 7-8

#### 4. Cryptographic State Tokens (CSTs)

Blockchain-style provenance chain:
- Signed state snapshots after each SPN operation
- Links to Compliance Manifest version (proves which axioms applied)
- Enables audit trail reconstruction
- 10-year retention (EU AI Act Article 12 requirement)

**Status**: 📋 Specified → Implementation Q4 2025 Week 6

#### 5. 8-Step Evolution Protocol

Compliance gates at each evolution step:
1. **Analyze**: Verify proposed changes don't violate axioms
2. **Design**: Check architecture maintains compliance
3. **Compile**: Scan generated code for safety violations
4. **Test**: Run compliance test suite
5. **Prove**: Generate Lean/Coq proofs of safety
6. **Verify**: External proof validation
7. **Log**: Create CST with evolution evidence
8. **Activate**: Final check + human approval

**Status**: 📋 Specified → Implementation Q4 2025 Weeks 9-11

### Traditional Compliance Features

- Control catalog mapped to EU AI Act, ISO 42001, ISO 27001, NIST AI RMF
- Evidence registry (Git commits, CSTs, proofs, files, logs)
- Risk assessment and incident management (Article 73 automation)
- Gap analysis and remediation tracking
- Audit packet export for regulators

**Status**: 📋 Specified → Implementation Q1 2026 Weeks 13-20

---

## Directory Structure

```
compliance/
├── README.md                          # This file
├── __init__.py
│
├── backend/                           # Backend implementation (Q4 2025 - Q2 2026)
│   ├── __init__.py
│   ├── config/
│   │   └── compliance_settings.py
│   ├── models/                        # Pydantic data models
│   │   ├── compliance_manifest.py     # $\mathcal{CM}$ schema
│   │   ├── layer0_axioms.py          # Layer 0 Axioms
│   │   ├── spn.py                    # SPN models
│   │   ├── cst.py                    # CST models
│   │   ├── evolution.py              # 8-step protocol
│   │   └── controls.py               # Traditional compliance
│   ├── services/                      # Business logic
│   │   ├── manifest_service.py       # $\mathcal{CM}$ management
│   │   ├── axiom_service.py          # Axiom validation
│   │   ├── spn_service.py            # SPN wrapping
│   │   ├── cst_service.py            # CST creation
│   │   └── evolution_service.py      # Evolution orchestration
│   ├── verification/                  # Formal verification
│   │   ├── lean_integration.py       # Lean 4 prover
│   │   ├── coq_integration.py        # Coq assistant
│   │   └── proof_service.py          # Unified interface
│   └── mcp/                           # MCP server
│       ├── compliance_server.py      # FastMCP server
│       └── tools/                    # MCP tools
│           ├── get_compliance_manifest.py
│           ├── validate_axiom.py
│           ├── verify_never_jettison.py
│           └── check_evolution_step.py
│
├── docs/                              # Documentation
│   ├── consolidated/                  # Regulatory mappings (✅ Complete)
│   │   ├── EU_AI_Act/
│   │   ├── ISO_42001/
│   │   ├── ISO_27001/
│   │   ├── NIST_AI_RMF/
│   │   └── blueprint/                # Cross-standard mapping
│   └── research/                      # Implementation docs
│       ├── COMPLIANCE_BACKEND_SPEC.md          # ✅ Updated (OpenAMI v2.0)
│       ├── CURRENT_IMPLEMENTATION_STATUS.md    # ✅ Updated
│       ├── EXECUTIVE_ACTION_PLAN.md            # ✅ Updated
│       ├── OPENAMI-COMPLIANCE-MAPPING.md       # ✅ New comprehensive mapping
│       └── COMPLIANCE_GAP_ANALYSIS.md
│
└── tests/                             # Test suite (Q1-Q2 2026)
    ├── test_compliance_manifest.py
    ├── test_layer0_axioms.py
    ├── test_spn_wrapper.py
    ├── test_cst_chain.py
    └── test_evolution_protocol.py
```

---

## Documentation Index

### Quick Links

| Document | Purpose | Status |
|----------|---------|--------|
| [COMPLIANCE_BACKEND_SPEC.md](docs/research/COMPLIANCE_BACKEND_SPEC.md) | Technical specification for backend implementation | ✅ Updated (v2.0) |
| [CURRENT_IMPLEMENTATION_STATUS.md](docs/research/CURRENT_IMPLEMENTATION_STATUS.md) | Current capabilities and gaps | ✅ Updated |
| [EXECUTIVE_ACTION_PLAN.md](docs/research/EXECUTIVE_ACTION_PLAN.md) | Budget, timeline, resource allocation | ✅ Updated |
| [OPENAMI-COMPLIANCE-MAPPING.md](docs/research/OPENAMI-COMPLIANCE-MAPPING.md) | OpenAMI architecture → regulatory requirements traceability | ✅ Complete |
| [COMPLIANCE_GAP_ANALYSIS.md](docs/research/COMPLIANCE_GAP_ANALYSIS.md) | Gap analysis and remediation plan | 🟡 In Progress |

### OpenAMI Documentation

- [System Architecture](/docs/openami/architecture/system-architecture.md) - Complete 4-layer architecture
- [What is OpenAMI?](/docs/openami/overview/what-is-openami.md) - Introduction
- [Quickstart Guide](/docs/openami/guides/quickstart.md) - Developer onboarding
- [Documentation Index](/docs/openami/DOCUMENTATION-INDEX.md) - Full documentation roadmap

### Regulatory Standards

Complete consolidated documentation available in `compliance/docs/consolidated/`:
- **EU AI Act** (Regulation 2024/1689)
- **ISO/IEC 42001:2023** (AI Management System)
- **ISO/IEC 27001:2022** (Information Security)
- **NIST AI RMF 1.0** (AI Risk Management Framework)

---

## Getting Started

### Prerequisites

**Current Phase**: Specification & Planning (Q4 2025 start)

Implementation prerequisites (will be updated as development progresses):
- Python 3.11+
- Lean 4 theorem prover (for formal verification)
- PostgreSQL 15+ (for compliance data)
- Dgraph (for CST chain traversal)
- Redis (for axiom caching)

### Installation (Future - Q2 2026)

```bash
# Clone repository
git clone https://github.com/Independent-AI-Labs/OpenAMI.git
cd OpenAMI/compliance

# Install dependencies
pip install -e .

# Configure compliance backend
cp default.env .env
# Edit .env with your configuration

# Initialize Compliance Manifest
python -m compliance.backend.scripts.init_manifest

# Start MCP server
python -m compliance.backend.mcp.run_mcp
```

### Current Status (2025-10-02)

**Phase**: Specification & Documentation (✅ Complete)

**Next Steps**:
1. ✅ Complete architecture documentation
2. ✅ Update compliance specs for OpenAMI integration
3. ⭕ Formalize Layer 0 Axioms (Q4 2025 Weeks 1-2)
4. ⭕ Implement Compliance Manifest (Q4 2025 Weeks 3-4)
5. ⭕ Begin backend scaffolding (Q4 2025 Week 5)

---

## MCP Server Usage

### Overview (Specification)

The Compliance MCP Server will expose compliance primitives via the Model Context Protocol, enabling:
- AI assistants to validate operations against Layer 0 Axioms
- Automated compliance checking during development
- Self-service SPN wrapping for existing modules
- Evolution protocol orchestration with compliance gates

### Available Tools (Planned Q4 2025 - Q1 2026)

#### OpenAMI Compliance Tools

```python
# Get current Compliance Manifest
manifest = mcp_client.call_tool("compliance.get_compliance_manifest")

# Validate operation against Layer 0 Axioms
result = mcp_client.call_tool("compliance.validate_axiom", {
    "operation_descriptor": {
        "module": "dataops.crud",
        "function": "delete_dataset",
        "params": {"dataset_id": "sensitive-data-001"}
    }
})

# Verify Never-Jettison Guarantee
verification = mcp_client.call_tool("compliance.verify_never_jettison", {
    "current_version": "2.5.0",
    "original_version": "1.0.0"
})

# Get CST provenance chain
chain = mcp_client.call_tool("compliance.get_cst_chain", {
    "spn_id": "dataops-crud-delete"
})

# Check evolution step compliance
checkpoint = mcp_client.call_tool("compliance.check_evolution_step", {
    "pipeline_id": "evolution-2024-10-02",
    "step": "prove",
    "artifacts": {"proof_file": "safety_proof.lean"}
})

# Wrap module as SPN
spn_config = mcp_client.call_tool("compliance.wrap_spn", {
    "module_path": "base.backend.dataops.crud",
    "functions": ["create", "read", "update", "delete"],
    "axiom_config": {
        "pre_check": ["data_privacy", "access_control"],
        "post_check": ["audit_trail_created"]
    }
})
```

#### Traditional Compliance Tools

```python
# Get control status
control = mcp_client.call_tool("compliance.get_control", {
    "control_id": "ISO27001-6.1.3"
})

# List compliance gaps
gaps = mcp_client.call_tool("compliance.list_gaps", {
    "standard": "EU_AI_Act",
    "status": "OPEN"
})

# Submit evidence
updated_control = mcp_client.call_tool("compliance.submit_evidence", {
    "control_id": "ISO42001-8.3",
    "evidence_ref": {
        "source_type": "CST",
        "location": "cst://abc123...",
        "submitted_by": "compliance-bot"
    }
})

# Export audit packet
audit_packet = mcp_client.call_tool("compliance.export_audit_packet", {
    "standard": "EU_AI_Act",
    "include_openami": true
})
```

---

## Development Roadmap

### Timeline: Q4 2025 - Q2 2026

**Total Budget**: €564k
**Resources**: 1.5 FTE engineering + 0.5 FTE formal verification specialist

### Phase 0: Foundation (Q4 2025, Weeks 1-4)
- ✅ Complete OpenAMI architecture documentation
- ⭕ Formalize Layer 0 Axioms in Lean/Coq
- ⭕ Implement Compliance Manifest schema
- ⭕ Create multi-party signature workflow

### Phase 1: Core OpenAMI Backend (Q4 2025, Weeks 5-8)
- ⭕ Integrate Lean/Coq proof verification
- ⭕ Implement CST creation and chain verification
- ⭕ Build SPN wrapper abstraction
- ⭕ Create axiom enforcement service

### Phase 2: Evolution Protocol & MCP (Q4 2025, Weeks 9-12)
- ⭕ Implement 8-step evolution protocol orchestration
- ⭕ Build MCP server with OpenAMI tools
- ⭕ Create evolution step compliance checker
- ⭕ Deploy SPN wrapper tool

### Phase 3: Traditional Compliance (Q1 2026, Weeks 13-20)
- ⭕ Implement control/evidence/risk models
- ⭕ Build traditional MCP tools
- ⭕ Create Article 73 incident automation
- ⭕ Load blueprint mappings

### Phase 4: Audit & Reporting (Q1-Q2 2026, Weeks 21-26)
- ⭕ Build audit packet generator
- ⭕ Automate evidence collection
- ⭕ Comprehensive testing
- ⭕ External audit dry-run

**Current Status**: Phase 0 - Documentation complete, implementation starting Q4 2025

See [EXECUTIVE_ACTION_PLAN.md](docs/research/EXECUTIVE_ACTION_PLAN.md) for detailed week-by-week breakdown.

---

## Regulatory Compliance Status

**Last Updated**: 2025-10-02

| Framework | Coverage | Readiness | Target Certification |
|-----------|----------|-----------|---------------------|
| EU AI Act | 35% → 100% (architected) | 40% | Q2 2026 |
| ISO/IEC 42001 | 40% → 100% (architected) | 45% | Q2 2026 |
| ISO/IEC 27001 | 45% → 85% (architected) | 50% | Q1 2026 |
| NIST AI RMF | 35% → 100% (architected) | 40% | Q2 2026 |

**Key Achievement**: OpenAMI architecture provides 100% theoretical coverage for EU AI Act, ISO 42001, and NIST AI RMF. Implementation in progress.

See [CURRENT_IMPLEMENTATION_STATUS.md](docs/research/CURRENT_IMPLEMENTATION_STATUS.md) for detailed capability breakdown.

---

## Contributing

### For Developers

1. **Read the specifications**:
   - [COMPLIANCE_BACKEND_SPEC.md](docs/research/COMPLIANCE_BACKEND_SPEC.md) - Technical architecture
   - [OpenAMI System Architecture](/docs/openami/architecture/system-architecture.md) - Core concepts

2. **Follow the implementation roadmap**:
   - Check [EXECUTIVE_ACTION_PLAN.md](docs/research/EXECUTIVE_ACTION_PLAN.md) for current priorities
   - Claim tasks from the roadmap (create GitHub issue)

3. **Development standards**:
   - Python 3.11+ with type hints
   - Pydantic models for all data structures
   - 90%+ test coverage required
   - All compliance checks must be auditable (create CSTs)

4. **Testing requirements**:
   - Unit tests for all services
   - Integration tests for MCP tools
   - Contract tests for OpenAMI primitives (axioms, CSTs, SPNs)
   - Mock Lean/Coq for CI/CD

### For Compliance Experts

1. **Review consolidated documentation**:
   - Check `compliance/docs/consolidated/` for accuracy
   - Validate regulatory mappings in [OPENAMI-COMPLIANCE-MAPPING.md](docs/research/OPENAMI-COMPLIANCE-MAPPING.md)

2. **Contribute to gap analysis**:
   - Review current gaps in COMPLIANCE_GAP_ANALYSIS.md
   - Suggest additional controls or evidence

3. **Participate in Compliance Manifest governance**:
   - Review Layer 0 Axioms formalization
   - Provide multi-party signature for Compliance Manifest updates

---

## Contact & Support

- **Compliance Lead**: compliance@independentailabs.com
- **Engineering Lead**: engineering@independentailabs.com
- **Issues**: [GitHub Issues](https://github.com/Independent-AI-Labs/OpenAMI/issues?label=compliance)
- **Documentation**: [OpenAMI Docs](https://github.com/Independent-AI-Labs/OpenAMI/tree/main/docs/openami)

---

## License

See LICENSE file in repository root.

---

**Last Updated**: 2025-10-02
**Next Review**: After Phase 0 completion (Q4 2025 Week 4)
