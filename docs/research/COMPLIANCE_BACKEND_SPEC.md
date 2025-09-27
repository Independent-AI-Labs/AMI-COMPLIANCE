# Compliance Backend & MCP Server Specification

## Purpose

Define the architecture, data contracts, and integration points for the `compliance` module backend and its pluggable Compliance MCP server. The goal is to align implementation with the established `base/backend` patterns (Pydantic data models, service layer abstractions, FastMCP servers) while exposing the compliance insights documented in `/docs` and `compliance/docs/consolidated/`.

## Target Capabilities

1. **Unified Compliance State API**
   - Collects attestations, control coverage, and risk findings mapped to EU AI Act, ISO/IEC 42001, ISO/IEC 27001, and NIST AI RMF requirements (see `compliance/docs/consolidated`).
   - Stores evaluations and evidence pointers in structured Pydantic models for persistence via the Base DataOps layer.

2. **Pluggable MCP Server**
   - Ships as `compliance/backend/mcp/compliance_server.py`, extending `base.backend.mcp.fastmcp_server_base.FastMCPServerBase`.
   - Provides tools for retrieving control status, submitting evidence, triggering gap analyses, and exporting audit packets.
   - Designed so new tools can be registered by dropping modules under `compliance/backend/mcp/tools/`.

3. **Control & Evidence Registry**
   - Maintains canonical control definitions linked to consolidated documentation and Blueprint references.
   - Supports evidence attachment (file pointers, Git references, orchestration logs) and lifecycle metadata (owner, review cadence, expiry).

4. **Risk & Incident Workflow**
   - Provides services to log risk assessments, Article 73 incident notifications, and Clause 10.2 corrective actions.
   - Integrates with Base audit logging (`base/backend/dataops/security/audit_trail.py`) for immutable traceability.

## Proposed Directory Layout

```
compliance/backend/
  __init__.py
  config/
    compliance_settings.py        # Settings model mirroring base config style
  models/
    __init__.py
    controls.py                   # Pydantic models for controls/requirements
    evidence.py                   # Evidence entries linked to Git paths, storage URIs
    risk.py                       # Risk assessment, incident, corrective action models
  repositories/
    __init__.py
    compliance_store.py           # DataOps-backed persistence helpers
  services/
    __init__.py
    control_service.py            # CRUD + status aggregation for controls
    risk_service.py               # Risk lifecycle + Article 73 helpers
    evidence_service.py           # Evidence attachment & validation
  mcp/
    __init__.py
    compliance_server.py          # FastMCP server implementation
    tools/
      __init__.py
      get_control.py              # Expose control metadata/status
      list_gaps.py                # Return outstanding gaps (links to gap analysis doc)
      submit_evidence.py          # Register evidence items
      export_audit_packet.py      # Download structured compliance report
```

## Data Model Guidelines

- Use `pydantic.BaseModel` subclasses with `ConfigDict(extra="forbid")` for strict validation (matching `base/backend/dataops` style).
- Reference consolidated documentation with `doc_path: str` attributes (e.g., `"consolidated/ISO_42001/support/support.md"`).
- Control models should capture:
  - `control_id` (e.g., `"ISO27001-6.1.3"`)
  - `title`
  - `source_standard` (enum covering EU_AI_ACT, ISO_42001, ISO_27001, NIST_AI_RMF, Blueprint)
  - `requirement_summary`
  - `implementation_status` (enum: `NOT_STARTED`, `IN_PROGRESS`, `OPERATIONAL`, `EVIDENCE_REQUIRED`)
  - `evidence_refs: list[EvidenceRef]`
  - `owner`, `review_cadence_days`

- Risk models align with EU AI Act Article 9 and ISO/IEC 42001 Clause 8 expectations:
  - `risk_id`, `description`, `category`, `likelihood`, `impact`, `residual_risk` (enum), `treatment_plan`, `status`.
  - Store Article 73 reporting metadata where applicable (`incident_level`, `notified_authorities`, `report_deadline`).

- Evidence entries include `source_type` (enum: `GIT_COMMIT`, `FILE`, `RUN_LOG`, `TICKET`, `DATASET`), `location`, `hash_or_version`, `submitted_by`, `submitted_at`, `validation_state`.

## MCP Server Contract

### Tool: `compliance.get_control`
- **Inputs:** `control_id`
- **Outputs:** Serialized `Control` model with evidence summary and doc references.

### Tool: `compliance.list_gaps`
- **Inputs:** Optional filters (`standard`, `status`, `module`).
- **Outputs:** Array of open gaps sourced from `COMPLIANCE_GAP_ANALYSIS.md` and live data.

### Tool: `compliance.submit_evidence`
- **Inputs:** `control_id`, `evidence_ref`
- **Flow:**
  1. Validate control exists.
  2. Persist evidence via `EvidenceService`.
  3. Log via Base audit chain.
  4. Return updated control snapshot.

### Tool: `compliance.export_audit_packet`
- **Inputs:** `standard`, optional timeframe.
- **Outputs:** Structured report (JSON) bundling control statuses, evidence references, and outstanding actions; suitable for regulators or certification bodies.

### Transport & Deployment
- Server derives from `FastMCPServerBase` to inherit auth, logging, and lifecycle hooks.
- Provide `run_mcp.py` entrypoint mirroring Base modules, using configuration from `.env`/`compliance/default.env`.
- Document CLI usage in `compliance/README.md` after implementation.

## Integration Requirements

1. **Audit Logging:** Every mutating action must call `base.backend.dataops.security.audit_trail.audit_log` to append to the blockchain-based audit chain.
2. **DataOps Persistence:** Repositories should leverage `base.backend.dataops.core.dao.DAOFactory` to store compliance models in configured storage (starting with PostgreSQL or Dgraph) to avoid custom persistence stacks.
3. **Configuration:** Align with Base config pattern using `pydantic-settings`. Provide `COMPLIANCE_STORAGE_BACKEND` & `COMPLIANCE_DEFAULT_STANDARD_SET` environment variables.
4. **Blueprint Mapping:** Keep `compliance/docs/consolidated/blueprint` as the canonical mapping for cross-standard traceability; the backend should load these files to seed control catalogs.
5. **Testing Pattern:** Mirror Base test layout (`tests/` with pytest + async fixtures). Provide contract tests for MCP tools and repository/service layers.

## Implementation Roadmap (Draft)

1. **Sprint 1 – Scaffolding**
   - Create `compliance/backend` package, config models, and placeholder repositories/services.
   - Implement control & evidence Pydantic models referencing consolidated docs.
2. **Sprint 2 – MCP Server MVP**
   - Build `compliance_server.py` with `get_control` and `list_gaps` tools backed by static data.
   - Integrate Base audit logging and DataOps DAO factories.
3. **Sprint 3 – Evidence Workflow**
   - Implement `submit_evidence` workflow with persistence and validation checks.
   - Add Article 73 incident tracking to risk service.
4. **Sprint 4 – Audit Packet & Automation**
   - Deliver `export_audit_packet` and automate seeding from consolidated docs.
   - Provide CLI entrypoint and documentation, plus comprehensive tests.

## Dependencies & Open Questions

- Confirm target storage backend (PostgreSQL vs Dgraph) for compliance data; default to PostgreSQL for relational integrity unless otherwise directed.
- Determine whether evidence files will be stored in Git, object storage, or external GRC tooling; spec assumes URIs/commits rather than binary blobs.
- Validate access control requirements for compliance MCP endpoints (role-based restrictions likely required for write operations).

---

This specification should be updated as implementation progresses. All documentation updates must stay synchronized with `compliance/docs/consolidated` requirements and the actual code shipped under `compliance/backend/`.
