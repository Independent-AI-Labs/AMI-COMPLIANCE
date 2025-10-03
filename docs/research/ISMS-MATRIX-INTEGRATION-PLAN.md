# ISMS-Matrix Integration Plan

**Version**: 1.0
**Created**: 2025-10-02
**Status**: 📋 Proposal
**Owner**: Compliance Working Group + Security Team

---

## Executive Summary

This plan proposes integrating the **Matrix protocol** as the secure communications backbone for the **Information Security Management System (ISMS)**, providing:

- **Secure, auditable communications** for security incidents, compliance activities, and human oversight
- **End-to-end encrypted** coordination channels for compliance team, security team, and auditors
- **Compliance evidence collection** from security-critical communications
- **Integration with OpenAMI architecture** (SPNs, CSTs, compliance workflows)
- **ISO/IEC 27001 Clause 7.4 (Communication) and 16.1 (Incident Management)** full compliance
- **EU AI Act Article 26 (Human Oversight)** communication channel requirements

### Key Benefits

| Benefit | Impact | ISO 27001 Clause |
|---------|--------|------------------|
| Encrypted incident response coordination | HIGH | 16.1, A.5.24, A.5.26 |
| Auditable compliance communications | HIGH | 7.4, 9.1 |
| Human oversight coordination | CRITICAL | Article 26 (EU AI Act) |
| Evidence collection from comms | MEDIUM | 9.1, 10.1 |
| Secure external auditor collaboration | HIGH | 9.2, 9.3 |
| Real-time security alerts | HIGH | 16.1, A.5.24 |

### Budget Impact

- **Initial Setup**: €15k (Q4 2025)
- **Annual Operations**: €8k/year (hosting + maintenance)
- **Integration Development**: Included in compliance backend budget (already allocated)

**ROI**: 3-6 months through reduced incident response time and automated evidence collection.

---

## Table of Contents

1. [Matrix Protocol Overview](#matrix-protocol-overview)
2. [ISMS-Matrix Architecture](#isms-matrix-architecture)
3. [ISO 27001 Compliance Mapping](#iso-27001-compliance-mapping)
4. [OpenAMI Integration](#openami-integration)
5. [Technical Specifications](#technical-specifications)
6. [Implementation Roadmap](#implementation-roadmap)
7. [Security Considerations](#security-considerations)
8. [Operations & Governance](#operations--governance)
9. [Success Criteria](#success-criteria)

---

## Matrix Protocol Overview

### What is Matrix?

**Matrix** is an open standard for secure, decentralized, real-time communication:

- **End-to-end encryption** (E2EE) using Olm/Megolm protocols
- **Federation**: Self-hosted servers, no vendor lock-in
- **Audit trail**: All messages cryptographically signed and persisted
- **Open source**: Fully auditable codebase
- **Bridges**: Integration with email, Slack, Discord, etc.

### Why Matrix for ISMS?

| ISMS Requirement | Matrix Capability |
|------------------|-------------------|
| Secure communications (ISO 27001 7.4) | E2E encryption, forward secrecy |
| Incident coordination (ISO 27001 16.1) | Real-time messaging, rooms per incident |
| Audit trail (ISO 27001 12.4) | Immutable message logs, signatures |
| External collaboration (ISO 27001 5.3) | Federation, guest access controls |
| Evidence retention (EU AI Act 12) | 10-year message retention configurable |
| Human oversight (EU AI Act 26) | Real-time alerts to human overseers |

### Comparison to Alternatives

| Feature | Matrix | Slack | MS Teams | Email |
|---------|--------|-------|----------|-------|
| E2E Encryption | ✅ Built-in | ❌ Enterprise only | ⚠️ Limited | ❌ No |
| Self-hosted | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| Open source | ✅ Yes | ❌ No | ❌ No | ✅ Partial |
| Audit trail | ✅ Immutable | ⚠️ Limited | ⚠️ Limited | ⚠️ Mutable |
| Federation | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| Compliance-ready | ✅ ISO 27001 | ⚠️ Commercial | ⚠️ Commercial | ⚠️ Complex |
| Cost | €€ Low | €€€€ High | €€€ Medium | € Very Low |

**Decision**: Matrix provides the best balance of security, auditability, and cost for ISMS communications.

---

## ISMS-Matrix Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 4: GOVERNANCE (Compliance Module)                        │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ ISMS Communications (Matrix Integration)                  │ │
│  │                                                            │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │ │
│  │  │ Incident     │  │ Human        │  │ Compliance   │   │ │
│  │  │ Response     │  │ Oversight    │  │ Coordination │   │ │
│  │  │ Rooms        │  │ Alerts       │  │ Rooms        │   │ │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │ │
│  │         │                  │                  │           │ │
│  │         └──────────────────┼──────────────────┘           │ │
│  │                            │                              │ │
│  │                    ┌───────▼────────┐                     │ │
│  │                    │ Matrix Bridge  │                     │ │
│  │                    │ (MCP Server)   │                     │ │
│  │                    └───────┬────────┘                     │ │
│  └────────────────────────────┼──────────────────────────────┘ │
│                                │                                │
│  ┌─────────────────────────────▼──────────────────────────────┐│
│  │ Compliance Backend Services                                ││
│  │ • Evidence Service (extracts from Matrix rooms)            ││
│  │ • Incident Service (creates rooms, alerts via Matrix)      ││
│  │ • Axiom Service (posts violation alerts to Matrix)         ││
│  └────────────────────────────┬───────────────────────────────┘│
└────────────────────────────────┼────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│ Matrix Homeserver (Synapse)                                    │
│                                                                 │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐               │
│  │ Security   │  │ Compliance │  │ External   │               │
│  │ Team Rooms │  │ Team Rooms │  │ Auditor    │               │
│  └────────────┘  └────────────┘  └────────────┘               │
│                                                                 │
│  ┌────────────────────────────────────────────────────────┐   │
│  │ Incident-Specific Rooms (Auto-created)                 │   │
│  │ • incident-2025-10-02-axiom-violation                  │   │
│  │ • incident-2025-10-03-data-breach-suspected            │   │
│  └────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Communication Flows

#### 1. Incident Response Flow

```
Layer 0 Axiom Violation Detected
         │
         ▼
Incident Service creates incident record
         │
         ▼
Matrix Bridge creates dedicated room
         │
         ├──> Invites security team
         ├──> Invites human overseer
         ├──> Posts incident details (encrypted)
         └──> Links to CST chain
         │
         ▼
Team coordinates response in Matrix room
         │
         ├──> Discusses root cause
         ├──> Assigns remediation tasks
         └──> Documents resolution
         │
         ▼
Evidence Service extracts room transcript
         │
         ▼
Transcript attached as evidence to incident record
         │
         ▼
Incident closed, room archived with 10-year retention
```

#### 2. Human Oversight Alert Flow

```
Evolution Step "Activate" triggered
         │
         ▼
Evolution Service requires human approval
         │
         ▼
Matrix Bridge posts to Human Oversight room
         │
         ├──> Evolution details
         ├──> Compliance check results
         ├──> Never-Jettison verification
         └──> Approval buttons (Element client)
         │
         ▼
Human Overseer reviews in Matrix client
         │
         ├──> Asks clarifying questions
         ├──> Reviews linked CST chains
         └──> Makes approval decision
         │
         ▼
Approval/rejection captured as evidence
         │
         ▼
Evolution pipeline proceeds or blocks
```

#### 3. Compliance Evidence Collection Flow

```
Compliance team discusses control implementation
         │
         ▼
Evidence Service monitors #compliance-iso27001 room
         │
         ▼
Detects message: "Deployed access control update [commit abc123]"
         │
         ▼
Extracts evidence:
         ├──> Message content + timestamp
         ├──> Sender (compliance team member)
         ├──> Linked artifacts (Git commit)
         └──> Room context
         │
         ▼
Creates EvidenceRef with source_type=MATRIX_MESSAGE
         │
         ▼
Links to control ISO27001-9.2.1 (Access control policy)
         │
         ▼
Available for audit packet export
```

---

## ISO 27001 Compliance Mapping

### Complete ISO 27001 Coverage via Matrix

| Clause | Requirement | Matrix Implementation | Evidence Generated |
|--------|-------------|----------------------|-------------------|
| **5.3** | Segregation of duties | Separate rooms: security-team, compliance-team, audit-team | Room membership logs |
| **7.4** | Communication | Secure channels for ISMS communications | Message logs (E2E encrypted) |
| **12.4** | Logging and monitoring | Immutable message logs with signatures | Synapse audit logs |
| **16.1.1** | Incident management planning | Dedicated incident rooms with templates | Room creation logs |
| **16.1.2** | Incident assessment | Incident discussion threads in rooms | Message transcripts |
| **16.1.4** | Incident response assessment | Post-mortem discussions captured | Room archives |
| **16.1.5** | Incident response communication | Real-time coordination via Matrix | Message delivery receipts |
| **A.5.24** | Information security incident response | Automated room creation on incidents | Incident room metadata |
| **A.5.26** | Response to info security incidents | Coordinated response in dedicated rooms | Response timeline from messages |
| **A.8.16** | Monitoring activities | Security alerts posted to monitoring room | Alert message logs |

### Annex A Controls Enhanced by Matrix

#### A.5.24: Security Incident Management Planning

**Current Gap**: Manual incident coordination via email/Slack
**Matrix Solution**:
- Auto-create incident room on Article 73 incident detection
- Standard incident response template posted automatically
- Key stakeholders invited based on severity
- Incident timeline reconstructed from room messages

**Evidence Generated**:
- Room creation timestamp
- Initial incident report (bot message)
- Team coordination transcript
- Resolution documentation
- Time-to-resolution metrics

#### A.5.26: Response to Information Security Incidents

**Current Gap**: No unified communication channel for incident response
**Matrix Solution**:
- Dedicated encrypted room per incident
- Integration with CST chain (link to violation provenance)
- Real-time updates to human overseers
- External auditor guest access for critical incidents

**Evidence Generated**:
- Complete response timeline
- Decision rationale
- Corrective action assignments
- Stakeholder notifications

#### A.8.16: Monitoring Activities

**Current Gap**: Monitoring alerts not integrated with response workflows
**Matrix Solution**:
- `#security-monitoring` room receives real-time alerts
- SPNs post axiom violation warnings
- CST chain anomaly detection alerts
- System health dashboards embedded in room

**Evidence Generated**:
- Alert history
- Alert acknowledgment by security team
- Follow-up actions discussed

---

## OpenAMI Integration

### Matrix as an OpenAMI SPN

Matrix communication itself becomes a **Secure Process Node (SPN)** with compliance enforcement:

```python
class MatrixSPN(SPNWrapper):
    """
    Matrix messaging wrapped as SPN with compliance checks.
    """
    spn_id = "matrix-communications"
    module_path = "compliance.backend.matrix.client"

    # Compliance configuration
    pre_check_axioms = [
        "data_privacy",           # Check message doesn't leak PII
        "access_control",         # Verify sender has room access
        "transparency"            # Log who sent what to whom
    ]

    post_check_axioms = [
        "audit_trail_created",    # Message logged immutably
        "encryption_verified"     # E2E encryption confirmed
    ]

    # CST configuration
    create_cst_on_success = True  # Every message creates CST
    cst_includes_output = False   # Don't include message content (E2E encrypted)

    async def send_message(self, room_id: str, message: str) -> MessageResult:
        """Send message with compliance checks."""
        # Pre-check: Validate message doesn't violate axioms
        compliance_check = await self.axiom_service.validate({
            "operation": "send_matrix_message",
            "room_id": room_id,
            "has_pii": self._detect_pii(message)
        })

        if not compliance_check.passed:
            raise AxiomViolationError(compliance_check.violations)

        # Send message via Matrix client
        result = await self.matrix_client.send_message(room_id, message)

        # Post-check: Verify encryption + create CST
        cst = await self.cst_service.create({
            "operation": "matrix_message_sent",
            "room_id": room_id,
            "event_id": result.event_id,
            "encrypted": result.encrypted,
            "timestamp": result.timestamp
        })

        return MessageResult(
            event_id=result.event_id,
            cst_id=cst.cst_id,
            compliance_check_id=compliance_check.check_id
        )
```

### Integration with Compliance Backend

#### 1. Matrix Bridge MCP Server

New MCP server: `compliance.backend.mcp.matrix_bridge.py`

**Tools Provided**:

```python
# Create incident response room
mcp_client.call_tool("matrix.create_incident_room", {
    "incident_id": "incident-2025-10-02-001",
    "severity": "CRITICAL",
    "stakeholders": ["security-lead", "human-overseer", "compliance-manager"]
})

# Post alert to human oversight room
mcp_client.call_tool("matrix.post_oversight_alert", {
    "pipeline_id": "evolution-2025-10-02",
    "step": "activate",
    "requires_approval": True,
    "compliance_manifest_version": "2.5.0",
    "cst_chain": ["cst-001", "cst-002", "cst-003"]
})

# Extract evidence from room
evidence = mcp_client.call_tool("matrix.extract_room_evidence", {
    "room_id": "!abc123:openami.org",
    "start_timestamp": "2025-10-01T00:00:00Z",
    "end_timestamp": "2025-10-02T00:00:00Z"
})

# Search for compliance discussions
results = mcp_client.call_tool("matrix.search_compliance_discussions", {
    "query": "ISO27001-6.1.3 implementation",
    "rooms": ["#compliance-iso27001"]
})
```

#### 2. Integration with Incident Service

```python
class IncidentService:
    """Enhanced with Matrix integration."""

    async def create_incident(self, incident: Incident) -> Incident:
        """Create incident with Matrix room."""
        # Traditional incident creation
        incident = await self.incident_store.create(incident)

        # Create Matrix room for coordination
        room = await self.matrix_bridge.create_incident_room(
            incident_id=incident.incident_id,
            severity=incident.severity,
            violated_axioms=incident.violated_axioms
        )

        # Link room to incident
        incident.matrix_room_id = room.room_id
        incident.matrix_room_url = room.url

        # Invite stakeholders based on severity
        if incident.severity == "CRITICAL":
            await self.matrix_bridge.invite_users(room.room_id, [
                "security-lead",
                "human-overseer",
                "cto",
                "legal-counsel"
            ])
        else:
            await self.matrix_bridge.invite_users(room.room_id, [
                "security-lead",
                "compliance-manager"
            ])

        # Post initial incident report
        await self.matrix_bridge.post_message(room.room_id,
            self._format_incident_report(incident)
        )

        return incident
```

#### 3. Integration with Evolution Protocol

```python
class EvolutionService:
    """Enhanced with Matrix human oversight."""

    async def request_activation_approval(
        self,
        pipeline: EvolutionPipeline
    ) -> bool:
        """Request human approval via Matrix."""

        # Post to human oversight room
        approval_request = await self.matrix_bridge.post_oversight_alert(
            pipeline_id=pipeline.pipeline_id,
            evolution_goal=pipeline.evolution_goal,
            compliance_manifest_version=pipeline.compliance_manifest_version,
            never_jettison_verified=pipeline.never_jettison_verified,
            checkpoints=pipeline.checkpoints
        )

        # Wait for approval (with timeout)
        approval = await self.matrix_bridge.wait_for_approval(
            message_id=approval_request.event_id,
            timeout_seconds=3600  # 1 hour
        )

        if not approval.approved:
            # Log rejection as evidence
            await self.evidence_service.create({
                "source_type": "MATRIX_MESSAGE",
                "location": f"matrix://{approval_request.room_id}/{approval.event_id}",
                "description": f"Evolution rejected: {approval.rejection_reason}",
                "submitted_by": approval.approver,
                "submitted_at": approval.timestamp
            })
            return False

        # Log approval as evidence
        await self.evidence_service.create({
            "source_type": "MATRIX_MESSAGE",
            "location": f"matrix://{approval_request.room_id}/{approval.event_id}",
            "description": f"Evolution approved by {approval.approver}",
            "submitted_by": approval.approver,
            "submitted_at": approval.timestamp
        })

        return True
```

### CST Integration

Every Matrix message creates a CST for provenance:

```python
class MatrixCSTIntegration:
    """Create CSTs for Matrix messages."""

    async def on_message_sent(self, event: MessageEvent) -> CST:
        """Create CST when message sent."""
        cst = await self.cst_service.create({
            "operation_type": "MATRIX_MESSAGE",
            "spn_id": "matrix-communications",
            "state_description": f"Message sent to {event.room_id}",
            "compliance_check_id": event.compliance_check_id,
            "provenance": {
                "parent_cst_id": None,  # Root CST for this message
                "compliance_manifest_version": self.get_current_cm_version(),
                "operation_type": "MATRIX_MESSAGE",
                "spn_id": "matrix-communications",
                "metadata": {
                    "room_id": event.room_id,
                    "event_id": event.event_id,
                    "sender": event.sender,
                    "encrypted": event.encrypted
                }
            }
        })

        return cst
```

---

## Technical Specifications

### Matrix Homeserver Deployment

#### Infrastructure Requirements

```yaml
# Docker Compose deployment
services:
  synapse:
    image: matrixdotorg/synapse:v1.95.0
    container_name: openami-matrix-synapse
    environment:
      - SYNAPSE_SERVER_NAME=matrix.openami.org
      - SYNAPSE_REPORT_STATS=no
    volumes:
      - ./synapse-data:/data
      - ./synapse-config:/config
    ports:
      - "8008:8008"
      - "8448:8448"  # Federation
    networks:
      - openami-compliance

  postgres:
    image: postgres:15
    container_name: openami-matrix-db
    environment:
      - POSTGRES_USER=synapse
      - POSTGRES_PASSWORD=${SYNAPSE_DB_PASSWORD}
      - POSTGRES_DB=synapse
    volumes:
      - ./postgres-data:/var/lib/postgresql/data
    networks:
      - openami-compliance

  element:
    image: vectorim/element-web:v1.11.0
    container_name: openami-matrix-element
    volumes:
      - ./element-config.json:/app/config.json
    ports:
      - "8080:80"
    networks:
      - openami-compliance

networks:
  openami-compliance:
    driver: bridge
```

#### Synapse Configuration

Key security settings in `homeserver.yaml`:

```yaml
# Server identity
server_name: "matrix.openami.org"
public_baseurl: "https://matrix.openami.org"

# Database
database:
  name: psycopg2
  args:
    user: synapse
    password: ${SYNAPSE_DB_PASSWORD}
    database: synapse
    host: postgres
    port: 5432
    cp_min: 5
    cp_max: 10

# Encryption (E2E)
encryption_enabled_by_default_for_room_type: all
require_encryption_for_room_type: all

# Retention policy (ISO 27001, EU AI Act Article 12)
retention:
  enabled: true
  default_policy:
    min_lifetime: 1d
    max_lifetime: 3650d  # 10 years

# Federation (disabled initially for security)
federation_domain_whitelist: []

# Registration (disabled - manual user provisioning only)
enable_registration: false
enable_registration_without_verification: false

# Rate limiting
rc_message:
  per_second: 10
  burst_count: 20

# Media
max_upload_size: 50M
media_retention:
  local_media_lifetime: 3650d  # 10 years
  remote_media_lifetime: 90d

# Logging
log_config: "/config/log.config"
```

### Matrix-Compliance Bridge Architecture

#### Bridge Components

```python
# compliance/backend/matrix/bridge.py

from matrix_client import AsyncClient
from typing import List, Dict, Any

class MatrixComplianceBridge:
    """
    Bridge between Matrix homeserver and compliance backend.
    Handles room management, message posting, evidence extraction.
    """

    def __init__(
        self,
        homeserver_url: str,
        bot_access_token: str,
        axiom_service: AxiomService,
        cst_service: CSTService,
        evidence_service: EvidenceService
    ):
        self.client = AsyncClient(homeserver_url, "@compliance-bot:matrix.openami.org")
        self.client.access_token = bot_access_token
        self.axiom_service = axiom_service
        self.cst_service = cst_service
        self.evidence_service = evidence_service

    async def create_incident_room(
        self,
        incident_id: str,
        severity: str,
        violated_axioms: List[str]
    ) -> RoomCreationResult:
        """Create dedicated room for incident response."""

        room_alias = f"#incident-{incident_id}:matrix.openami.org"

        # Create E2E encrypted room
        room = await self.client.room_create(
            alias=room_alias,
            name=f"Incident: {incident_id}",
            topic=f"Severity: {severity} | Axioms: {', '.join(violated_axioms)}",
            preset="private_chat",
            initial_state=[
                {
                    "type": "m.room.encryption",
                    "state_key": "",
                    "content": {"algorithm": "m.megolm.v1.aes-sha2"}
                },
                {
                    "type": "m.room.retention",
                    "state_key": "",
                    "content": {
                        "max_lifetime": 315360000000  # 10 years in ms
                    }
                }
            ]
        )

        # Post initial incident report
        await self.client.room_send(
            room.room_id,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "body": self._format_incident_report(incident_id, severity, violated_axioms),
                "format": "org.matrix.custom.html",
                "formatted_body": self._format_incident_report_html(incident_id, severity, violated_axioms)
            }
        )

        return RoomCreationResult(
            room_id=room.room_id,
            room_alias=room_alias,
            url=f"https://matrix.openami.org/#/room/{room.room_id}"
        )

    async def extract_room_evidence(
        self,
        room_id: str,
        start_timestamp: datetime,
        end_timestamp: datetime
    ) -> List[EvidenceRef]:
        """Extract messages from room as compliance evidence."""

        # Fetch room messages
        messages = await self.client.room_messages(
            room_id=room_id,
            start=self._datetime_to_matrix_ts(start_timestamp),
            end=self._datetime_to_matrix_ts(end_timestamp),
            direction="f",  # Forward
            limit=1000
        )

        evidence_refs = []

        for event in messages.chunk:
            if event.type != "m.room.message":
                continue

            # Create evidence reference
            evidence_ref = await self.evidence_service.create({
                "source_type": "MATRIX_MESSAGE",
                "location": f"matrix://{room_id}/{event.event_id}",
                "description": event.content.get("body", ""),
                "submitted_by": event.sender,
                "submitted_at": datetime.fromtimestamp(event.origin_server_ts / 1000),
                "hash_or_version": event.event_id,
                "metadata": {
                    "room_id": room_id,
                    "event_id": event.event_id,
                    "encrypted": event.encrypted
                }
            })

            evidence_refs.append(evidence_ref)

        return evidence_refs
```

#### MCP Server Integration

```python
# compliance/backend/mcp/matrix_bridge_server.py

from base.backend.mcp.fastmcp_server_base import FastMCPServerBase
from mcp import Tool

class MatrixBridgeMCPServer(FastMCPServerBase):
    """MCP server exposing Matrix bridge functionality."""

    def __init__(self, bridge: MatrixComplianceBridge):
        super().__init__(name="matrix-bridge")
        self.bridge = bridge

    def get_tools(self) -> List[Tool]:
        return [
            Tool(
                name="matrix.create_incident_room",
                description="Create dedicated Matrix room for incident response",
                input_schema={
                    "type": "object",
                    "properties": {
                        "incident_id": {"type": "string"},
                        "severity": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH", "CRITICAL"]},
                        "violated_axioms": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["incident_id", "severity"]
                }
            ),
            Tool(
                name="matrix.post_oversight_alert",
                description="Post alert to human oversight room requiring approval",
                input_schema={
                    "type": "object",
                    "properties": {
                        "pipeline_id": {"type": "string"},
                        "step": {"type": "string"},
                        "requires_approval": {"type": "boolean"},
                        "metadata": {"type": "object"}
                    },
                    "required": ["pipeline_id", "step"]
                }
            ),
            Tool(
                name="matrix.extract_room_evidence",
                description="Extract messages from Matrix room as compliance evidence",
                input_schema={
                    "type": "object",
                    "properties": {
                        "room_id": {"type": "string"},
                        "start_timestamp": {"type": "string", "format": "date-time"},
                        "end_timestamp": {"type": "string", "format": "date-time"}
                    },
                    "required": ["room_id"]
                }
            ),
            Tool(
                name="matrix.search_compliance_discussions",
                description="Search Matrix rooms for compliance-related discussions",
                input_schema={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "rooms": {"type": "array", "items": {"type": "string"}},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"}
                    },
                    "required": ["query"]
                }
            )
        ]

    async def handle_tool_call(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        if tool_name == "matrix.create_incident_room":
            return await self.bridge.create_incident_room(**arguments)
        elif tool_name == "matrix.post_oversight_alert":
            return await self.bridge.post_oversight_alert(**arguments)
        elif tool_name == "matrix.extract_room_evidence":
            return await self.bridge.extract_room_evidence(**arguments)
        elif tool_name == "matrix.search_compliance_discussions":
            return await self.bridge.search_compliance_discussions(**arguments)
        else:
            raise ValueError(f"Unknown tool: {tool_name}")
```

### Data Models

```python
# compliance/backend/models/matrix.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict, Any, Optional

class MatrixRoom(BaseModel):
    """Matrix room metadata."""
    room_id: str
    room_alias: str
    name: str
    topic: str
    encrypted: bool = True
    retention_days: int = 3650  # 10 years
    created_at: datetime
    created_by: str

    # Compliance metadata
    purpose: str  # "INCIDENT_RESPONSE" | "HUMAN_OVERSIGHT" | "COMPLIANCE_COORDINATION"
    linked_entity_type: str | None  # "INCIDENT" | "EVOLUTION_PIPELINE" | "CONTROL"
    linked_entity_id: str | None

    # Access control
    members: List[str]
    invited_users: List[str]

class MatrixMessage(BaseModel):
    """Matrix message with compliance metadata."""
    event_id: str
    room_id: str
    sender: str
    timestamp: datetime
    content: str
    encrypted: bool

    # Compliance integration
    cst_id: str | None  # CST created for this message
    compliance_check_id: str | None
    evidence_ref_id: str | None  # If extracted as evidence

class MatrixEvidence(BaseModel):
    """Evidence extracted from Matrix communications."""
    evidence_id: str
    room_id: str
    event_ids: List[str]  # Message(s) comprising the evidence
    extracted_at: datetime
    extracted_by: str

    # Content
    summary: str
    full_transcript: str | None  # Encrypted if room was encrypted

    # Linkage
    controls_satisfied: List[str]  # Control IDs this evidence supports
    incidents_related: List[str]  # Incident IDs discussed

class OversightApproval(BaseModel):
    """Human oversight approval via Matrix."""
    approval_id: str
    pipeline_id: str
    step: str

    # Request
    requested_at: datetime
    requested_by: str  # Usually "compliance-bot"
    request_message_id: str

    # Response
    approved: bool
    approver: str  # Human overseer user ID
    approval_timestamp: datetime | None
    rejection_reason: str | None
    response_message_id: str

    # Evidence
    cst_id: str  # CST proving approval/rejection
    evidence_ref_id: str
```

---

## Implementation Roadmap

### Timeline: Q4 2025 - Q1 2026

**Budget**: €23k (€15k setup + €8k annual operations included in compliance backend budget)

### Phase 1: Infrastructure Setup (Q4 2025, Week 12)

**Goal**: Deploy Matrix homeserver and basic configuration

**Tasks**:
1. **Week 12, Day 1-2: Infrastructure Provisioning**
   - Provision VM/container infrastructure (€5k/year hosting)
   - Set up Docker Compose environment
   - Configure PostgreSQL database for Synapse
   - Deploy Synapse homeserver
   - Deploy Element web client

2. **Week 12, Day 3-4: Security Hardening**
   - Enable E2E encryption by default
   - Configure retention policies (10 years)
   - Disable federation (initially, enable later after security review)
   - Set up rate limiting
   - Configure TLS certificates (Let's Encrypt)

3. **Week 12, Day 5: User Provisioning**
   - Create compliance bot user account
   - Create initial rooms:
     - `#security-team:matrix.openami.org`
     - `#compliance-team:matrix.openami.org`
     - `#human-oversight:matrix.openami.org`
     - `#incident-response:matrix.openami.org`
   - Provision initial users (security lead, compliance manager, human overseer)
   - Test E2E encryption

**Deliverables**:
- ✅ Operational Matrix homeserver
- ✅ Element web client accessible
- ✅ Compliance bot account
- ✅ Initial rooms configured
- ✅ Security hardening complete

**Budget**: €15k (infrastructure setup + first year hosting prepaid)

### Phase 2: Bridge Development (Q1 2026, Weeks 13-14)

**Goal**: Build Matrix-Compliance Bridge with basic functionality

**Tasks**:
1. **Week 13: Core Bridge Implementation**
   - Implement `MatrixComplianceBridge` class
   - Room creation functionality
   - Message posting functionality
   - Evidence extraction functionality
   - User invitation management

2. **Week 14: MCP Server Integration**
   - Implement `MatrixBridgeMCPServer`
   - Expose MCP tools:
     - `matrix.create_incident_room`
     - `matrix.post_message`
     - `matrix.extract_room_evidence`
   - Integration testing with compliance backend
   - Documentation

**Deliverables**:
- ✅ `compliance/backend/matrix/bridge.py` implemented
- ✅ `compliance/backend/mcp/matrix_bridge_server.py` operational
- ✅ Basic MCP tools working
- ✅ Integration tests passing

**Budget**: Included in compliance backend development (already allocated)

### Phase 3: Incident Response Integration (Q1 2026, Weeks 15-16)

**Goal**: Integrate Matrix with incident management workflow

**Tasks**:
1. **Week 15: Incident Service Integration**
   - Update `IncidentService` to create Matrix rooms
   - Auto-invite stakeholders based on severity
   - Post initial incident report to room
   - Test incident lifecycle with Matrix coordination

2. **Week 16: Evidence Collection**
   - Implement automated evidence extraction from incident rooms
   - Link evidence to incident records
   - Test evidence chain: incident → Matrix room → evidence → audit packet

**Deliverables**:
- ✅ Incidents automatically create Matrix rooms
- ✅ Evidence extracted from incident discussions
- ✅ Integration with Article 73 incident reporting

**Budget**: Included in compliance backend development

### Phase 4: Human Oversight Integration (Q1 2026, Weeks 17-18)

**Goal**: Implement human oversight approval workflow via Matrix

**Tasks**:
1. **Week 17: Oversight Alert System**
   - Implement `post_oversight_alert` functionality
   - Create approval request message templates
   - Build approval/rejection capture mechanism
   - Test with evolution pipeline integration

2. **Week 18: Approval Workflow**
   - Update `EvolutionService` to use Matrix for approvals
   - Implement approval timeout handling
   - Create evidence trail for approvals/rejections
   - Test complete evolution cycle with human oversight

**Deliverables**:
- ✅ Human oversight alerts posted to Matrix
- ✅ Approval/rejection captured as evidence
- ✅ Evolution pipeline gated by Matrix approvals
- ✅ EU AI Act Article 26 compliance achieved

**Budget**: Included in compliance backend development

### Phase 5: Evidence Automation (Q1 2026, Weeks 19-20)

**Goal**: Automate evidence collection from compliance discussions

**Tasks**:
1. **Week 19: Search & Extraction**
   - Implement `search_compliance_discussions` tool
   - Build evidence extraction from keyword searches
   - Create evidence linking to controls
   - Test evidence workflow: discussion → extraction → control linkage

2. **Week 20: Audit Integration**
   - Include Matrix evidence in `export_audit_packet`
   - Generate Matrix evidence bundle (room transcripts)
   - Test audit packet with Matrix evidence
   - Documentation for auditors

**Deliverables**:
- ✅ Automated evidence extraction from Matrix
- ✅ Matrix evidence in audit packets
- ✅ Auditor documentation complete

**Budget**: Included in compliance backend development

### Phase 6: Operations & Training (Q1 2026, Week 21)

**Goal**: Operationalize Matrix ISMS and train users

**Tasks**:
1. **Week 21, Day 1-2: Documentation**
   - User guide for security team
   - User guide for compliance team
   - Human oversight approval process
   - Incident response via Matrix runbook

2. **Week 21, Day 3-4: Training**
   - Train security team on Matrix client (Element)
   - Train compliance team on evidence collection
   - Train human overseers on approval workflow
   - Conduct incident response drill using Matrix

3. **Week 21, Day 5: Go-Live**
   - Enable Matrix for production use
   - Monitor initial usage
   - Collect feedback
   - Iterate on UX issues

**Deliverables**:
- ✅ Complete user documentation
- ✅ Team training completed
- ✅ Matrix ISMS operational
- ✅ Monitoring dashboards deployed

**Budget**: €3k (training materials + incident response drill)

### Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Incident response time | <30 minutes | Time from incident creation to first team message |
| Human oversight approval time | <1 hour | Time from request to approval/rejection |
| Evidence collection automation | 80%+ | % of evidence auto-extracted vs manual |
| User adoption | 100% security team | Active users in Matrix rooms |
| Message retention compliance | 100% | All rooms configured with 10-year retention |
| Encryption coverage | 100% | All rooms E2E encrypted |
| ISO 27001 Clause 16.1 compliance | 100% | Incident management via Matrix |

---

## Security Considerations

### Threat Model

| Threat | Impact | Mitigation |
|--------|--------|------------|
| Unauthorized access to incident rooms | CRITICAL | E2E encryption + strict room access controls |
| Message tampering | HIGH | Cryptographic signatures on all messages |
| Compliance bot compromise | CRITICAL | Separate bot account, limited permissions |
| Insider threat (malicious team member) | HIGH | Immutable message logs, audit trail |
| DoS attack on homeserver | MEDIUM | Rate limiting, infrastructure redundancy |
| Data breach (stolen server) | HIGH | E2E encryption (server has encrypted blobs only) |
| Evidence deletion | CRITICAL | Immutable Synapse database + backups |

### Security Controls

#### 1. End-to-End Encryption

**Requirement**: All compliance-sensitive rooms must use E2E encryption (Olm/Megolm)

**Implementation**:
```yaml
# Synapse config
encryption_enabled_by_default_for_room_type: all
require_encryption_for_room_type: all
```

**Verification**:
- Room state includes `m.room.encryption` event
- Messages have `m.room.encrypted` type
- CST records `encrypted: true` field

#### 2. Access Control

**Principle**: Need-to-know access only

**Implementation**:
- Private rooms (invite-only)
- Role-based invitations (security team, compliance team, auditors)
- Guest access disabled by default
- Federation disabled (no cross-server communication initially)

**Verification**:
- Room membership audited via Matrix admin API
- Unauthorized join attempts logged and blocked

#### 3. Audit Logging

**Requirement**: All Matrix activities logged immutably

**Implementation**:
```python
# Every Matrix message creates CST
cst = await cst_service.create({
    "operation_type": "MATRIX_MESSAGE",
    "spn_id": "matrix-communications",
    "state_hash": hash(event_id + sender + timestamp),
    "compliance_check_id": compliance_check.check_id,
    "provenance": {
        "operation_type": "MATRIX_MESSAGE",
        "spn_id": "matrix-communications",
        "metadata": {
            "room_id": room_id,
            "event_id": event_id,
            "sender": sender,
            "encrypted": True
        }
    }
})
```

**Retention**:
- Matrix Synapse logs: 10 years
- CST chain: 10 years
- Database backups: 10 years (encrypted)

#### 4. Compliance Bot Security

**Threat**: Compromised bot could leak sensitive data

**Mitigations**:
- Bot runs with least privilege (can only post/read in designated rooms)
- Bot token stored in HashiCorp Vault
- Bot actions logged via CST chain
- Bot cannot approve evolution steps (human-only action)

#### 5. Incident Room Isolation

**Design**: Each incident gets dedicated room that is archived after resolution

**Benefits**:
- Prevents cross-incident information leakage
- Clear evidence boundaries
- Easier audit trail reconstruction

**Implementation**:
```python
async def create_incident_room(self, incident_id: str):
    room = await self.client.room_create(
        alias=f"#incident-{incident_id}:matrix.openami.org",
        preset="private_chat",  # Invite-only
        initial_state=[{
            "type": "m.room.encryption",
            "content": {"algorithm": "m.megolm.v1.aes-sha2"}
        }]
    )
    return room
```

### Compliance with Standards

#### ISO/IEC 27001:2022

| Control | Requirement | Matrix Implementation |
|---------|-------------|----------------------|
| A.5.13 | Labelling of information | Room topics indicate sensitivity |
| A.5.14 | Information transfer | E2E encryption for all transfers |
| A.5.24 | Information security incident management | Incident-specific rooms |
| A.8.10 | Information deletion | Configurable retention policies |
| A.8.16 | Monitoring activities | Alert rooms + message logs |

#### EU AI Act Article 12 (Logging)

**Requirement**: Automatic recording of events during operation of high-risk AI

**Matrix Compliance**:
- All human oversight decisions logged (approval/rejection messages)
- Incident response actions logged (room transcripts)
- 10-year retention period configured
- Immutable logs (Synapse database + CST chain)

#### GDPR Considerations

**Personal Data in Matrix**:
- User IDs (email addresses) - personal data
- Message content may contain personal data

**GDPR Compliance**:
- **Lawful basis**: Legitimate interest (ISMS operation, regulatory compliance)
- **Data minimization**: Only security/compliance team members in rooms
- **Storage limitation**: 10-year retention justified by EU AI Act Article 12
- **Right to erasure**: Cannot delete from immutable logs, but can pseudonymize
- **Encryption**: E2E encryption protects personal data

---

## Operations & Governance

### Operational Procedures

#### 1. Incident Response via Matrix (Runbook)

**Trigger**: Layer 0 Axiom violation detected OR manual incident creation

**Procedure**:
1. **Automatic**: Incident Service creates Matrix room
2. **Automatic**: Compliance bot posts initial incident report
3. **Automatic**: Stakeholders invited based on severity:
   - CRITICAL: Security Lead, Human Overseer, CTO, Legal
   - HIGH: Security Lead, Compliance Manager
   - MEDIUM/LOW: Security Lead only
4. **Human**: Security team joins room, begins investigation
5. **Human**: Root cause analysis documented in room
6. **Human**: Remediation tasks assigned via Matrix messages
7. **Human**: Resolution documented, room marked resolved
8. **Automatic**: Evidence Service extracts room transcript
9. **Automatic**: Evidence linked to incident record
10. **Manual**: Incident closed by Security Lead
11. **Automatic**: Room archived (10-year retention)

#### 2. Human Oversight Approval (Runbook)

**Trigger**: Evolution step "Activate" requires approval

**Procedure**:
1. **Automatic**: Evolution Service posts approval request to `#human-oversight` room
2. **Automatic**: Approval request includes:
   - Evolution goal
   - Compliance Manifest version
   - Never-Jettison verification result
   - CST chain links
   - All compliance checkpoint results
3. **Human**: Human Overseer reviews request in Element client
4. **Human**: Overseer asks clarifying questions (via Matrix messages)
5. **Human**: Overseer reviews linked CST chains (via web UI)
6. **Human**: Overseer makes decision (approve/reject)
7. **Human**: Overseer clicks approval button OR posts rejection reason
8. **Automatic**: Evidence Service captures approval message
9. **Automatic**: Evolution Service proceeds or blocks based on decision
10. **Automatic**: CST created linking approval to evolution pipeline

#### 3. Evidence Collection from Discussions (Runbook)

**Trigger**: Compliance team mentions control ID in Matrix room

**Procedure**:
1. **Human**: Compliance team discusses control implementation in `#compliance-iso27001` room
2. **Human**: Team member posts: "Deployed MFA for admin access per ISO27001-9.4.3 [commit abc123]"
3. **Automatic**: Evidence Service detects control ID mention via webhook
4. **Automatic**: Evidence Service extracts message as evidence
5. **Automatic**: Evidence linked to control ISO27001-9.4.3
6. **Automatic**: Evidence includes:
   - Message content
   - Timestamp
   - Submitter (compliance team member)
   - Linked artifacts (Git commit abc123)
7. **Manual**: Evidence validated by Compliance Manager
8. **Automatic**: Evidence available in audit packet

### Governance Structure

#### Room Ownership

| Room | Owner | Purpose | Retention |
|------|-------|---------|-----------|
| `#security-team` | Security Lead | General security discussions | 10 years |
| `#compliance-team` | Compliance Manager | Compliance coordination | 10 years |
| `#human-oversight` | Human Overseer | Evolution approvals, high-severity incidents | 10 years |
| `#incident-*` | Security Lead | Per-incident response | 10 years |
| `#audit-*` | Compliance Manager | External auditor collaboration | 10 years |

#### Access Control Policy

**Principles**:
- **Need-to-know**: Only invite users who need access for their role
- **Least privilege**: Bot has minimal permissions
- **Separation of duties**: Security team ≠ Compliance team (different rooms)

**User Roles**:
- **Security Lead**: Admin access to security rooms, incident rooms
- **Compliance Manager**: Admin access to compliance rooms
- **Human Overseer**: Read/write access to oversight room
- **Compliance Bot**: Post messages, create rooms (no admin)
- **External Auditor**: Read-only guest access to audit rooms (time-limited)

### Monitoring & Metrics

#### Operational Metrics

**Real-time Dashboard** (integrated with compliance backend):

```python
# compliance/backend/matrix/metrics.py

class MatrixMetrics:
    """Collect operational metrics from Matrix."""

    async def get_dashboard_metrics(self) -> Dict[str, Any]:
        return {
            "active_incident_rooms": await self.count_active_incident_rooms(),
            "pending_oversight_approvals": await self.count_pending_approvals(),
            "messages_last_24h": await self.count_messages_last_24h(),
            "evidence_extracted_this_week": await self.count_evidence_this_week(),
            "average_incident_response_time_minutes": await self.calculate_avg_response_time(),
            "average_oversight_approval_time_minutes": await self.calculate_avg_approval_time(),
            "encryption_coverage_percent": await self.calculate_encryption_coverage(),
            "rooms_with_retention_policy_percent": await self.calculate_retention_coverage()
        }
```

**Alerts** (posted to `#security-monitoring` room):
- New incident room created (severity: HIGH/CRITICAL)
- Pending oversight approval >30 minutes
- Encryption disabled on any room (should never happen)
- Retention policy not configured (should never happen)
- Unusual message volume (potential DoS or incident)

---

## Success Criteria

### Phase Completion Criteria

#### Phase 1: Infrastructure Setup ✅
- [ ] Matrix homeserver operational (99.9% uptime)
- [ ] E2E encryption enabled on all rooms
- [ ] 10-year retention configured
- [ ] Element web client accessible
- [ ] Compliance bot account created
- [ ] Initial rooms configured
- [ ] Security hardening complete (TLS, rate limiting)

#### Phase 2: Bridge Development ✅
- [ ] `MatrixComplianceBridge` implemented
- [ ] MCP server operational
- [ ] Basic MCP tools working
- [ ] Integration tests passing (90%+ coverage)
- [ ] Documentation complete

#### Phase 3: Incident Response Integration ✅
- [ ] Incidents auto-create Matrix rooms
- [ ] Stakeholders auto-invited based on severity
- [ ] Evidence auto-extracted from incident rooms
- [ ] Integration with Article 73 reporting
- [ ] Incident response time <30 minutes

#### Phase 4: Human Oversight Integration ✅
- [ ] Oversight alerts posted to Matrix
- [ ] Approvals captured as evidence
- [ ] Evolution pipeline gated by Matrix approvals
- [ ] Approval time <1 hour
- [ ] EU AI Act Article 26 compliance achieved

#### Phase 5: Evidence Automation ✅
- [ ] Automated evidence extraction from discussions
- [ ] 80%+ evidence auto-collected
- [ ] Matrix evidence in audit packets
- [ ] Auditor documentation complete

#### Phase 6: Operations & Training ✅
- [ ] User documentation complete
- [ ] Team training completed (100% participation)
- [ ] Incident response drill successful
- [ ] Matrix ISMS operational
- [ ] User satisfaction >4.0/5.0

### Overall Success Criteria

**Technical**:
- ✅ 100% encryption coverage
- ✅ 100% retention policy compliance
- ✅ <30 minute incident response time
- ✅ <1 hour oversight approval time
- ✅ 99.9% homeserver uptime

**Compliance**:
- ✅ ISO 27001 Clause 7.4 (Communication) - 100% compliant
- ✅ ISO 27001 Clause 16.1 (Incident Management) - 100% compliant
- ✅ EU AI Act Article 26 (Human Oversight) - communication channel provided
- ✅ EU AI Act Article 12 (Logging) - 10-year retention configured
- ✅ External audit dry-run successful

**Operational**:
- ✅ 100% security team adoption
- ✅ 100% compliance team adoption
- ✅ 80%+ evidence auto-collected
- ✅ Zero unauthorized access incidents
- ✅ User satisfaction >4.0/5.0

---

## Budget Summary

| Category | Q4 2025 | Q1 2026 | Q2 2026 | Total |
|----------|---------|---------|---------|-------|
| Infrastructure Setup | €15k | €0k | €0k | €15k |
| Annual Hosting (prepaid) | €0k | €5k | €0k | €5k |
| Training & Documentation | €0k | €3k | €0k | €3k |
| **Total** | **€15k** | **€8k** | **€0k** | **€23k** |

**Included in compliance backend budget** (no additional allocation needed):
- Bridge development (Weeks 13-14)
- Incident integration (Weeks 15-16)
- Oversight integration (Weeks 17-18)
- Evidence automation (Weeks 19-20)

**Total ISMS-Matrix Budget**: €23k over 9 months

**Annual recurring cost**: €8k (hosting + maintenance)

---

## Appendices

### Appendix A: Matrix Room Templates

#### Incident Room Template

```markdown
# Incident: {incident_id}

**Severity**: {severity}
**Created**: {timestamp}
**Violated Axioms**: {axiom_list}

## Incident Details

- **SPN**: {spn_id}
- **Compliance Check**: {compliance_check_id}
- **CST Chain**: {cst_chain_links}

## Response Checklist

- [ ] Root cause identified
- [ ] Immediate containment actions taken
- [ ] Stakeholders notified
- [ ] Remediation plan created
- [ ] Regulatory reporting initiated (if required)
- [ ] Corrective actions implemented
- [ ] Incident review completed

## Links

- Incident Record: {incident_url}
- CST Chain: {cst_chain_url}
- Compliance Check: {compliance_check_url}
```

#### Human Oversight Approval Template

```markdown
# Evolution Approval Request

**Pipeline ID**: {pipeline_id}
**Step**: Activate
**Requested**: {timestamp}

## Evolution Details

**Goal**: {evolution_goal}
**Target Component**: {target_component}
**Compliance Manifest Version**: {cm_version}

## Compliance Status

✅ Never-Jettison Verified: {never_jettison_result}
✅ All checkpoints passed: {all_checkpoints_passed}

## Checkpoints

- ✅ Analyze: Passed
- ✅ Design: Passed
- ✅ Compile: Passed
- ✅ Test: Passed
- ✅ Prove: Passed
- ✅ Verify: Passed
- ✅ Log: Passed

## CST Chain

{cst_chain_links}

## Action Required

**Human Overseer**: Please review and approve/reject this evolution.

**To Approve**: React with ✅ and post "APPROVED"
**To Reject**: React with ❌ and post "REJECTED: {reason}"
```

### Appendix B: Configuration Examples

See technical specifications section above for complete configuration examples.

---

**Document Maintenance**:
- **Created**: 2025-10-02
- **Next Review**: After Phase 1 completion (Q4 2025 Week 12)
- **Owner**: Compliance Working Group + Security Team

---

**Related Documents**:
- [COMPLIANCE_BACKEND_SPEC.md](COMPLIANCE_BACKEND_SPEC.md) - Compliance backend architecture
- [EXECUTIVE_ACTION_PLAN.md](EXECUTIVE_ACTION_PLAN.md) - Overall compliance roadmap
- [CURRENT_IMPLEMENTATION_STATUS.md](CURRENT_IMPLEMENTATION_STATUS.md) - Implementation status
- [OPENAMI-COMPLIANCE-MAPPING.md](OPENAMI-COMPLIANCE-MAPPING.md) - Regulatory mappings
