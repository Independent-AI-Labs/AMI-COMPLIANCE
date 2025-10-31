# Audit Trail System Specification

**Version**: 1.0.0
**Status**: 📋 Specification Complete → 🛠️ Implementation Ready
**Module**: Compliance (Layer 4: Governance)
**Date**: 2025-10-31

---

## Executive Summary

The Audit Trail System provides comprehensive, cryptographically-verifiable auditing for ANY file, module, or service within the AMI-ORCHESTRATOR repository. It replaces the limited `base/backend/dataops/security/audit_trail.py` decorator with a generic, pluggable architecture that supports:

- **Git history auditing**: Commits, authors, blame, change patterns
- **File auditing**: Content hashing, metadata, permissions, quality
- **Log auditing**: Structured parsing, error aggregation, pattern detection
- **Service auditing**: Health checks, uptime, resource usage
- **Module auditing**: Dependencies, test coverage, code metrics
- **Quality auditing**: Integration with ami-agent for code quality violations

All audit records are stored in a blockchain-style immutable chain with cryptographic signatures, supporting complete traceability, forensic analysis, and regulatory compliance.

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Core Components](#core-components)
3. [Audit Sources](#audit-sources)
4. [Analyzers](#analyzers)
5. [Collectors](#collectors)
6. [Reporting](#reporting)
7. [CLI Interface](#cli-interface)
8. [MCP Integration](#mcp-integration)
9. [Data Models](#data-models)
10. [Storage](#storage)
11. [Implementation Plan](#implementation-plan)
12. [Examples](#examples)

---

## Architecture Overview

### Design Principles

1. **Generic & Reusable**: Audit ANY entity (file, module, service, log) with consistent interface
2. **Pluggable**: Add new audit sources and analyzers without changing core
3. **Immutable**: Blockchain-style audit chain with cryptographic verification
4. **Traceable**: Every audit record includes who, what, when, where, how, why
5. **Integration-Ready**: Works with ami-agent, DataOps, MCP, services, git

### Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLI Layer                                │
│  ami-audit {repo|module|file|git|logs|services|quality}         │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Collection Layer                             │
│  ┌──────────────┬──────────────┬──────────────┐                │
│  │BatchCollector│StreamCollector│ScheduledCol │                │
│  └──────────────┴──────────────┴──────────────┘                │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                      Source Layer                               │
│  ┌────────┬────────┬────────┬─────────┬────────┬────────┐      │
│  │  Git   │  File  │  Log   │ Service │ Module │Quality │      │
│  │ Source │ Source │ Source │  Source │ Source │Source  │      │
│  └────────┴────────┴────────┴─────────┴────────┴────────┘      │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                     Analyzer Layer                              │
│  ┌────────┬────────┬─────────┬───────────┬────────┐            │
│  │  Git   │Quality │Security │Compliance │ Drift  │            │
│  │Analyzer│Analyzer│Analyzer │ Analyzer  │Analyzer│            │
│  └────────┴────────┴─────────┴───────────┴────────┘            │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                       Core Layer                                │
│  ┌──────────────┬──────────────┬──────────────┐                │
│  │ AuditRecord  │  AuditChain  │  AuditStore  │                │
│  └──────────────┴──────────────┴──────────────┘                │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                     Storage Layer                               │
│  Dgraph (provenance graph) + Postgres (records) + Redis (cache)│
└─────────────────────────────────────────────────────────────────┘
```

### Component Organization

```
compliance/
├── backend/
│   └── audit/
│       ├── core/                 # Core audit primitives
│       ├── sources/              # Pluggable audit sources
│       ├── analyzers/            # Pluggable analyzers
│       ├── collectors/           # Collection strategies
│       └── reporting/            # Output formatting
└── scripts/
    ├── ami-audit                 # CLI wrapper (executable)
    └── audit_cli.py              # CLI implementation
```

---

## Core Components

### 1. AuditRecord

**Purpose**: Immutable audit record representing a single auditable event.

**Location**: `compliance/backend/audit/core/audit_record.py`

**Schema**:
```python
class AuditRecord(BaseModel):
    """Immutable audit record."""

    # Identity
    record_id: str = Field(default_factory=lambda: str(uuid.uuid7()))
    record_hash: str = ""  # SHA-256 hash of record content

    # Provenance (WHO/WHAT/WHEN/WHERE/HOW/WHY)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    actor: str  # Who performed the action (user, service, system)
    action: str  # What action was performed
    target: str  # What was targeted (file path, module name, service name)
    target_type: AuditTargetType  # FILE, MODULE, SERVICE, LOG, GIT
    source: str  # How audit was collected (git_source, quality_source, etc.)
    reason: str | None = None  # Why action was taken

    # Context
    context: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)

    # Chain linkage
    previous_hash: str = "0"  # Hash of previous record in chain
    nonce: int = 0  # Proof-of-work nonce

    # Signatures
    signatures: list[AuditSignature] = Field(default_factory=list)

    # Analysis results
    findings: list[AuditFinding] = Field(default_factory=list)
    violations: list[AuditViolation] = Field(default_factory=list)

    # Classification
    severity: AuditSeverity = AuditSeverity.INFO
    classification: DataClassification = DataClassification.INTERNAL

    # Status
    status: AuditStatus = AuditStatus.RECORDED
```

**Key Methods**:
- `calculate_hash() -> str`: Calculate SHA-256 hash of record
- `mine_block(difficulty: int) -> None`: Proof-of-work mining
- `verify() -> bool`: Verify record integrity
- `sign(private_key: str, signer: str) -> None`: Add cryptographic signature
- `verify_signatures() -> bool`: Verify all signatures

### 2. AuditChain

**Purpose**: Blockchain-style immutable chain of audit records with verification.

**Location**: `compliance/backend/audit/core/audit_chain.py`

**Key Features**:
- Append-only audit chain
- Cryptographic hash linking
- Multi-party signature support
- Byzantine fault tolerance ready (4/5 consensus)
- Complete chain verification
- Forensic analysis support

**Key Methods**:
```python
class AuditChain:
    async def add_record(self, record: AuditRecord) -> AuditRecord
    def verify_chain(self) -> bool
    def get_chain_slice(self, start: datetime, end: datetime) -> list[AuditRecord]
    def find_records(self, filters: AuditFilter) -> list[AuditRecord]
    def export_chain(self, format: str) -> str
    def verify_signatures(self) -> dict[str, bool]
```

### 3. AuditStore

**Purpose**: Persistent storage for audit records with efficient querying.

**Location**: `compliance/backend/audit/core/audit_store.py`

**Storage Backends**:
- **Dgraph**: Provenance graph (who → what → when relationships)
- **Postgres**: Structured audit records (queryable)
- **Redis**: Hot cache for recent audits

**Key Methods**:
```python
class AuditStore:
    async def store_record(self, record: AuditRecord) -> None
    async def get_record(self, record_id: str) -> AuditRecord | None
    async def query_records(self, filter: AuditFilter) -> list[AuditRecord]
    async def get_provenance_chain(self, target: str) -> list[AuditRecord]
    async def verify_integrity(self) -> bool
```

### 4. AuditContext

**Purpose**: Context manager for scoped audit collection.

**Location**: `compliance/backend/audit/core/audit_context.py`

**Usage**:
```python
async with AuditContext(
    actor="ami-agent",
    action="quality_check",
    target="base/backend/dataops/",
) as audit:
    # Operations are automatically audited
    violations = await run_quality_check()
    audit.add_findings(violations)
    # Context exit commits audit record
```

---

## Audit Sources

### Base Interface

**Location**: `compliance/backend/audit/sources/base.py`

```python
class AuditSource(ABC):
    """Abstract audit source interface."""

    @abstractmethod
    async def collect(self, target: str, options: AuditOptions) -> list[AuditRecord]:
        """Collect audit records from source."""

    @abstractmethod
    def supports(self, target_type: AuditTargetType) -> bool:
        """Check if source supports target type."""

    @abstractmethod
    def get_metadata(self) -> dict[str, Any]:
        """Get source metadata."""
```

### 1. GitSource

**Location**: `compliance/backend/audit/sources/git_source.py`

**Capabilities**:
- Commit history extraction
- Author contributions analysis
- File change tracking
- Blame annotations
- Branch/tag analysis

**Example Usage**:
```python
git_source = GitSource(repo_path="/path/to/repo")
records = await git_source.collect(
    target="base/backend/dataops/",
    options=AuditOptions(
        since=datetime(2024, 1, 1),
        authors=["ami"],
        include_blame=True
    )
)
```

### 2. FileSource

**Location**: `compliance/backend/audit/sources/file_source.py`

**Capabilities**:
- Content hashing (SHA-256)
- File metadata (size, permissions, timestamps)
- Ownership tracking
- Symlink resolution
- Binary vs. text detection

**Example Usage**:
```python
file_source = FileSource()
records = await file_source.collect(
    target="base/**/*.py",
    options=AuditOptions(pattern=True, include_hash=True)
)
```

### 3. LogSource

**Location**: `compliance/backend/audit/sources/log_source.py`

**Capabilities**:
- Structured log parsing (JSON, logfmt)
- Error aggregation
- Pattern detection
- Log level filtering
- Multi-file correlation

**Example Usage**:
```python
log_source = LogSource()
records = await log_source.collect(
    target="logs/ami-agent/",
    options=AuditOptions(level=LogLevel.ERROR, since="7 days ago")
)
```

### 4. ServiceSource

**Location**: `compliance/backend/audit/sources/service_source.py`

**Capabilities**:
- Service health checks
- Process status monitoring
- Resource usage tracking (CPU, memory, disk)
- Docker container inspection
- Uptime calculation

**Integration**: Reads from `nodes/config/setup-service.yaml`

**Example Usage**:
```python
service_source = ServiceSource()
records = await service_source.collect(
    target="data-stack",
    options=AuditOptions(include_health=True, include_logs=True)
)
```

### 5. ModuleSource

**Location**: `compliance/backend/audit/sources/module_source.py`

**Capabilities**:
- Dependency analysis (pyproject.toml, uv.lock)
- Test coverage extraction
- Code metrics (LOC, complexity)
- Module structure analysis
- Import graph analysis

**Integration**: Reads module structure from repository

**Example Usage**:
```python
module_source = ModuleSource()
records = await module_source.collect(
    target="base",
    options=AuditOptions(include_dependencies=True, include_tests=True)
)
```

### 6. QualitySource

**Location**: `compliance/backend/audit/sources/quality_source.py`

**Capabilities**:
- Code quality violations (via ami-agent)
- Banned words detection
- Ruff/mypy violations
- Security vulnerabilities (bandit)
- Complexity analysis

**Integration**: Calls ami-agent for quality checks

**Example Usage**:
```python
quality_source = QualitySource()
records = await quality_source.collect(
    target="base/",
    options=AuditOptions(
        check_banned_words=True,
        run_ruff=True,
        run_mypy=True
    )
)
```

---

## Analyzers

### Base Interface

**Location**: `compliance/backend/audit/analyzers/base.py`

```python
class AuditAnalyzer(ABC):
    """Abstract audit analyzer interface."""

    @abstractmethod
    async def analyze(self, records: list[AuditRecord]) -> list[AuditFinding]:
        """Analyze audit records and produce findings."""

    @abstractmethod
    def supports(self, source_type: str) -> bool:
        """Check if analyzer supports source type."""
```

### 1. GitAnalyzer

**Location**: `compliance/backend/audit/analyzers/git_analyzer.py`

**Analysis**:
- Commit frequency patterns
- Author contribution distribution
- Change hotspots (frequently modified files)
- Commit message quality
- Large file commits

### 2. QualityAnalyzer

**Location**: `compliance/backend/audit/analyzers/quality_analyzer.py`

**Analysis**:
- Code quality trends
- Violation density (violations per LOC)
- Quality debt estimation
- Refactoring recommendations
- Test coverage gaps

### 3. SecurityAnalyzer

**Location**: `compliance/backend/audit/analyzers/security_analyzer.py`

**Analysis**:
- Secrets detection (API keys, passwords)
- Vulnerability scanning
- Dependency vulnerabilities
- Permission issues
- Insecure patterns

### 4. ComplianceAnalyzer

**Location**: `compliance/backend/audit/analyzers/compliance_analyzer.py`

**Analysis**:
- Regulatory gap detection
- Control coverage analysis
- Evidence completeness
- Audit trail gaps
- Policy violations

### 5. DriftAnalyzer

**Location**: `compliance/backend/audit/analyzers/drift_analyzer.py`

**Analysis**:
- Baseline comparison
- Change velocity tracking
- Unexpected modifications
- Configuration drift
- Dependency drift

---

## Collectors

### 1. BatchCollector

**Location**: `compliance/backend/audit/collectors/batch_collector.py`

**Purpose**: One-time batch audit collection.

**Usage**:
```python
collector = BatchCollector()
results = await collector.collect(
    sources=[git_source, file_source, quality_source],
    analyzers=[git_analyzer, quality_analyzer],
    target="base/backend/dataops/"
)
```

### 2. StreamCollector

**Location**: `compliance/backend/audit/collectors/stream_collector.py`

**Purpose**: Real-time audit trail streaming.

**Usage**:
```python
collector = StreamCollector()
async for record in collector.stream(
    sources=[log_source, service_source],
    target="logs/ami-agent/"
):
    print(f"New audit record: {record.action}")
```

### 3. ScheduledCollector

**Location**: `compliance/backend/audit/collectors/scheduled_collector.py`

**Purpose**: Cron-based periodic audit collection.

**Usage**:
```python
collector = ScheduledCollector()
await collector.schedule(
    schedule="0 */6 * * *",  # Every 6 hours
    sources=[quality_source],
    target="**/*.py"
)
```

---

## Reporting

### 1. Formatters

**Location**: `compliance/backend/audit/reporting/formatters.py`

**Supported Formats**:
- **JSON**: Machine-readable, API-friendly
- **YAML**: Human-readable, config-friendly
- **Markdown**: Documentation, reports
- **HTML**: Web dashboards
- **CSV**: Spreadsheet analysis
- **Terminal**: ANSI-colored CLI output

### 2. Exporters

**Location**: `compliance/backend/audit/reporting/exporters.py`

**Export Targets**:
- **DataOps**: Store in Dgraph/Postgres
- **SIEM**: Export to security information systems
- **Compliance Systems**: Export for regulatory reporting
- **Git**: Commit audit reports to repository
- **Slack/Email**: Notification integrations

### 3. Dashboards

**Location**: `compliance/backend/audit/reporting/dashboards.py`

**Features**:
- Terminal-based real-time dashboards
- Rich text rendering (tables, progress bars, sparklines)
- Live updating metrics
- Interactive filtering

---

## CLI Interface

### Wrapper Script

**Location**: `compliance/scripts/ami-audit`

```bash
#!/usr/bin/env bash
# ami-audit: Wrapper for compliance/scripts/audit_cli.py
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

# Use compliance module venv
exec "$MODULE_DIR/.venv/bin/python" "$SCRIPT_DIR/audit_cli.py" "$@"
```

### CLI Commands

**Location**: `compliance/scripts/audit_cli.py`

#### Repository Audit
```bash
# Audit entire repository
ami-audit repo

# Audit with specific sources
ami-audit repo --sources=git,file,quality

# Audit with baseline comparison
ami-audit repo --baseline=.audit/baseline-2024-01-01.json
```

#### Module Audit
```bash
# Audit specific module
ami-audit module base

# Include tests
ami-audit module base --include-tests

# Include dependencies analysis
ami-audit module compliance --include-dependencies
```

#### File Audit
```bash
# Audit single file
ami-audit file base/backend/dataops/security/audit_trail.py

# Audit pattern
ami-audit file "base/**/*.py" --pattern

# Include git history
ami-audit file path/to/file.py --include-git
```

#### Git History Audit
```bash
# Audit all commits since date
ami-audit git --since="2024-01-01"

# Audit by author
ami-audit git --author="ami"

# Audit specific file history
ami-audit git --file=path/to/file.py

# Include blame annotations
ami-audit git --file=path/to/file.py --blame
```

#### Log Audit
```bash
# Audit log directory
ami-audit logs --dir=logs/ami-agent

# Filter by level
ami-audit logs --dir=logs/ --level=ERROR

# Filter by service
ami-audit logs --service=data-stack

# Time range
ami-audit logs --since="1 hour ago" --until="now"
```

#### Service Audit
```bash
# Audit all services
ami-audit services

# Audit specific service
ami-audit service data-stack

# Include health checks
ami-audit service data-stack --health

# Include logs
ami-audit service data-stack --logs --since="24 hours ago"
```

#### Quality Audit
```bash
# Quality audit with ami-agent
ami-audit quality base/

# Check for violations
ami-audit quality base/ --violations

# Include banned words
ami-audit quality compliance/ --banned-words

# Auto-fix issues
ami-audit quality base/ --fix
```

#### Diff/Comparison
```bash
# Compare two time periods
ami-audit diff --from="2024-01-01" --to="2024-10-31"

# Compare against baseline
ami-audit diff --baseline=.audit/baseline.json

# Show drift
ami-audit diff --baseline=.audit/baseline.json --show-drift
```

#### Reporting
```bash
# Generate markdown report
ami-audit report --format=markdown --output=AUDIT-REPORT.md

# Generate JSON export
ami-audit report --format=json --output=audit-data.json

# Export to compliance system
ami-audit report --export=compliance-system

# Generate HTML dashboard
ami-audit report --format=html --output=audit-dashboard.html
```

#### Verification
```bash
# Verify audit chain integrity
ami-audit verify --chain

# Verify signatures
ami-audit verify --signatures

# Verify specific record
ami-audit verify --record=abc123...
```

#### Query
```bash
# Query by action
ami-audit query --action=dataops_delete

# Query by user
ami-audit query --user=system

# Query by module
ami-audit query --module=base

# Query by time range
ami-audit query --since="7 days ago" --until="now"

# Complex query
ami-audit query --action=quality_violation --severity=HIGH --since="30 days ago"
```

#### Watch Mode
```bash
# Watch module for changes
ami-audit watch --module=base

# Watch service
ami-audit watch --service=data-stack

# Watch logs
ami-audit watch --logs=logs/ami-agent/
```

---

## MCP Integration

### Audit MCP Server

**Location**: `compliance/backend/mcp/audit/audit_server.py`

**Tools**:

#### 1. audit_file
```python
@mcp.tool()
async def audit_file(file_path: str, include_git: bool = False) -> dict:
    """Audit a specific file."""
```

#### 2. audit_module
```python
@mcp.tool()
async def audit_module(
    module_name: str,
    include_tests: bool = False,
    include_dependencies: bool = False
) -> dict:
    """Audit a module."""
```

#### 3. audit_git
```python
@mcp.tool()
async def audit_git(
    target: str,
    since: str | None = None,
    author: str | None = None
) -> dict:
    """Audit git history."""
```

#### 4. audit_logs
```python
@mcp.tool()
async def audit_logs(
    log_dir: str,
    level: str | None = None,
    since: str | None = None
) -> dict:
    """Audit log files."""
```

#### 5. audit_services
```python
@mcp.tool()
async def audit_services(service_name: str | None = None) -> dict:
    """Audit services."""
```

#### 6. verify_audit_chain
```python
@mcp.tool()
async def verify_audit_chain() -> dict:
    """Verify audit chain integrity."""
```

#### 7. query_audit_trail
```python
@mcp.tool()
async def query_audit_trail(
    action: str | None = None,
    user: str | None = None,
    since: str | None = None,
    limit: int = 100
) -> dict:
    """Query audit trail."""
```

---

## Data Models

### Enumerations

```python
class AuditTargetType(str, Enum):
    FILE = "file"
    MODULE = "module"
    SERVICE = "service"
    LOG = "log"
    GIT = "git"
    QUALITY = "quality"

class AuditSeverity(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class AuditStatus(str, Enum):
    RECORDED = "recorded"
    ANALYZED = "analyzed"
    VERIFIED = "verified"
    EXPORTED = "exported"
```

### Supporting Models

```python
class AuditSignature(BaseModel):
    signer: str
    signature: str
    algorithm: str = "Ed25519"
    timestamp: datetime

class AuditFinding(BaseModel):
    finding_id: str
    finding_type: str
    severity: AuditSeverity
    description: str
    location: str | None = None
    recommendation: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

class AuditViolation(BaseModel):
    violation_id: str
    rule: str
    severity: AuditSeverity
    message: str
    file_path: str | None = None
    line_number: int | None = None
    column_number: int | None = None

class AuditFilter(BaseModel):
    target_type: AuditTargetType | None = None
    action: str | None = None
    actor: str | None = None
    severity: AuditSeverity | None = None
    since: datetime | None = None
    until: datetime | None = None
    limit: int = 100
```

---

## Storage

### Dgraph Schema

```graphql
type AuditRecord {
    record_id: string @index(exact)
    record_hash: string @index(exact)
    timestamp: datetime @index(hour)
    actor: string @index(exact)
    action: string @index(exact)
    target: string @index(term)
    target_type: string @index(exact)
    source: string @index(exact)
    previous_hash: string @index(exact)
    severity: string @index(exact)
    status: string @index(exact)

    # Relationships
    previous_record: uid @reverse
    findings: [uid] @reverse
    violations: [uid] @reverse
    signatures: [uid] @reverse
}

type AuditFinding {
    finding_id: string @index(exact)
    finding_type: string @index(exact)
    severity: string @index(exact)
    description: string
}

type AuditViolation {
    violation_id: string @index(exact)
    rule: string @index(exact)
    severity: string @index(exact)
    message: string
    file_path: string @index(term)
}

type AuditSignature {
    signer: string @index(exact)
    signature: string
    algorithm: string
    timestamp: datetime @index(hour)
}
```

### Postgres Schema

```sql
CREATE TABLE audit_records (
    record_id UUID PRIMARY KEY,
    record_hash VARCHAR(64) NOT NULL UNIQUE,
    timestamp TIMESTAMP NOT NULL,
    actor VARCHAR(255) NOT NULL,
    action VARCHAR(255) NOT NULL,
    target TEXT NOT NULL,
    target_type VARCHAR(50) NOT NULL,
    source VARCHAR(255) NOT NULL,
    reason TEXT,
    context JSONB,
    metadata JSONB,
    previous_hash VARCHAR(64) NOT NULL,
    nonce INTEGER NOT NULL,
    severity VARCHAR(50) NOT NULL,
    classification VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_audit_timestamp ON audit_records(timestamp DESC);
CREATE INDEX idx_audit_actor ON audit_records(actor);
CREATE INDEX idx_audit_action ON audit_records(action);
CREATE INDEX idx_audit_target_type ON audit_records(target_type);
CREATE INDEX idx_audit_severity ON audit_records(severity);

CREATE TABLE audit_findings (
    finding_id UUID PRIMARY KEY,
    record_id UUID REFERENCES audit_records(record_id),
    finding_type VARCHAR(255) NOT NULL,
    severity VARCHAR(50) NOT NULL,
    description TEXT,
    location TEXT,
    recommendation TEXT,
    metadata JSONB
);

CREATE TABLE audit_violations (
    violation_id UUID PRIMARY KEY,
    record_id UUID REFERENCES audit_records(record_id),
    rule VARCHAR(255) NOT NULL,
    severity VARCHAR(50) NOT NULL,
    message TEXT,
    file_path TEXT,
    line_number INTEGER,
    column_number INTEGER
);

CREATE TABLE audit_signatures (
    signature_id UUID PRIMARY KEY,
    record_id UUID REFERENCES audit_records(record_id),
    signer VARCHAR(255) NOT NULL,
    signature TEXT NOT NULL,
    algorithm VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);
```

---

## Implementation Plan

### Phase 1: Core Foundation (Week 1)
- [ ] Create directory structure
- [ ] Implement AuditRecord model
- [ ] Implement AuditChain
- [ ] Implement AuditStore (Postgres + Dgraph)
- [ ] Write core tests

### Phase 2: Audit Sources (Week 2)
- [ ] Implement base AuditSource interface
- [ ] Implement GitSource
- [ ] Implement FileSource
- [ ] Implement LogSource
- [ ] Implement ServiceSource
- [ ] Implement ModuleSource
- [ ] Implement QualitySource
- [ ] Write source tests

### Phase 3: Analyzers (Week 3)
- [ ] Implement base AuditAnalyzer interface
- [ ] Implement GitAnalyzer
- [ ] Implement QualityAnalyzer
- [ ] Implement SecurityAnalyzer
- [ ] Implement ComplianceAnalyzer
- [ ] Implement DriftAnalyzer
- [ ] Write analyzer tests

### Phase 4: Collectors & Reporting (Week 4)
- [ ] Implement BatchCollector
- [ ] Implement StreamCollector
- [ ] Implement ScheduledCollector
- [ ] Implement Formatters (JSON, YAML, Markdown, HTML)
- [ ] Implement Exporters
- [ ] Implement Dashboards
- [ ] Write collector/reporting tests

### Phase 5: CLI (Week 5)
- [ ] Create ami-audit wrapper script
- [ ] Implement audit_cli.py with all subcommands
- [ ] Add CLI tests
- [ ] Write CLI documentation

### Phase 6: MCP Integration (Week 6)
- [ ] Implement audit MCP server
- [ ] Implement MCP tools
- [ ] Add MCP integration tests
- [ ] Update MCP documentation

### Phase 7: Integration & Documentation (Week 7)
- [ ] Integrate with ami-agent
- [ ] Migrate existing audit_trail.py users
- [ ] Write comprehensive documentation
- [ ] Update compliance README.md
- [ ] Create example workflows

---

## Examples

### Example 1: Audit Module Quality

```bash
# Audit base module for quality issues
ami-audit quality base/ --violations --output=base-quality-report.md

# Review violations
cat base-quality-report.md

# Fix automatically
ami-audit quality base/ --fix

# Verify fixes
ami-audit quality base/ --violations
```

### Example 2: Track Git History

```bash
# Audit all commits in last 30 days
ami-audit git --since="30 days ago" --output=git-history.json

# Analyze author contributions
ami-audit git --since="2024-01-01" --format=markdown > AUTHORS.md

# Track specific file history
ami-audit git --file=compliance/README.md --blame
```

### Example 3: Monitor Service Health

```bash
# Check data-stack health
ami-audit service data-stack --health

# Continuous monitoring
ami-audit watch --service=data-stack

# Audit service logs
ami-audit service data-stack --logs --since="1 hour ago" --level=ERROR
```

### Example 4: Compliance Audit

```bash
# Full repository audit
ami-audit repo --sources=git,file,quality,service

# Generate compliance report
ami-audit report --format=html --output=compliance-audit.html

# Export to compliance system
ami-audit report --export=compliance-system

# Verify audit chain
ami-audit verify --chain --signatures
```

### Example 5: Query Audit Trail

```python
from compliance.backend.audit import AuditStore, AuditFilter

# Query recent quality violations
store = AuditStore()
records = await store.query_records(
    AuditFilter(
        action="quality_violation",
        severity=AuditSeverity.HIGH,
        since=datetime.now() - timedelta(days=30)
    )
)

# Analyze patterns
for record in records:
    print(f"{record.timestamp}: {record.target} - {record.findings}")
```

---

## Migration from audit_trail.py

### Old Usage (base/backend/dataops/security/audit_trail.py)

```python
from base.backend.dataops.security.audit_trail import audit_log

@audit_log(module="dataops", action="delete")
async def delete_data(id: str):
    # Operation
    pass
```

### New Usage (compliance/backend/audit)

```python
from compliance.backend.audit import AuditContext

async def delete_data(id: str):
    async with AuditContext(
        actor="system",
        action="dataops_delete",
        target=f"record:{id}",
        target_type=AuditTargetType.SERVICE
    ) as audit:
        # Operation
        result = await perform_delete(id)

        # Add metadata
        audit.context["record_id"] = id
        audit.context["result"] = result

        # Context exit commits audit record
```

---

## Security Considerations

1. **Cryptographic Verification**: All audit records signed with Ed25519
2. **Immutability**: Blockchain-style chain prevents tampering
3. **Access Control**: Audit operations require authentication
4. **Data Classification**: Sensitive data redacted based on classification
5. **Multi-Party Signatures**: Support for BFT consensus (4/5 verifiers)

---

## Compliance Mapping

| Feature | EU AI Act | ISO 42001 | ISO 27001 | NIST AI RMF |
|---------|-----------|-----------|-----------|-------------|
| Audit Trail | Article 12 | 8.3 | A.12.4.1 | GOVERN 1.2 |
| Provenance | Article 13 | 8.4 | A.12.4.2 | MAP 1.1 |
| Verification | Article 14 | 9.1 | A.12.4.3 | MEASURE 1.1 |
| Retention | Article 12 | 10.2 | A.12.3.1 | GOVERN 1.4 |

---

**Last Updated**: 2025-10-31
**Next Review**: After Phase 1 completion
**Owner**: Compliance Working Group
