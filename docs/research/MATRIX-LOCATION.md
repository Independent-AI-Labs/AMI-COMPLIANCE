# Matrix Configuration Location

**Note**: Matrix homeserver configuration has been moved to the **streams** module.

## Rationale

Matrix is fundamentally a **real-time messaging and event streaming protocol**, which aligns with the streams module's purpose:
- Event streaming and message queuing
- WebSocket-based real-time communication
- Custom protocol implementation
- Data streaming pipelines

See `streams/REQUIREMENTS.md` section "Data Streaming" (lines 129-145) for requirements.

## Configuration Location

**Matrix Synapse homeserver configuration**: `/streams/config/matrix/`

Files:
- `homeserver.yaml` - Synapse configuration
- `element-config.json` - Element web client configuration
- `README.md` - Setup and integration guide
- `INTEGRATION.md` - Nodes launcher integration

## Docker Compose Services

**File**: `/docker-compose.services.yml`

Services:
- `matrix-postgres` - PostgreSQL database for Synapse
- `matrix-synapse` - Matrix Synapse homeserver
- `matrix-element` - Element web client

Profiles:
- `matrix` - Start Matrix stack only
- `streams-full` - Matrix + data backends
- `isms` - Alias for `matrix`

## Service Manifest

**File**: `/scripts/services.yaml`

Matrix services registered under module: `streams`

Tags:
- `streams:matrix` - Matrix services
- `streams:messaging` - Messaging capabilities
- `streams:events` - Event streaming
- `streams:ui` - Element web UI

## Usage

```bash
# Start Matrix via docker-compose
docker-compose -f docker-compose.services.yml --profile matrix up -d

# Or via nodes launcher (when implemented)
python nodes/scripts/launch_services.py start --profile matrix

# Or use isms profile for compliance integration
python nodes/scripts/launch_services.py start --profile isms
```

## ISMS Integration

The compliance module integrates with Matrix for:
- Incident response coordination (dedicated rooms per incident)
- Human oversight approvals (evolution protocol gates)
- Evidence collection (compliance discussions → audit evidence)
- Security team communication

**ISMS Integration Plan**: `/compliance/docs/research/ISMS-MATRIX-INTEGRATION-PLAN.md`

This integration plan remains in the compliance module as it documents how the **compliance backend** integrates with the Matrix **streaming infrastructure** provided by the streams module.

## Compliance Backend Integration

The compliance backend will integrate with Matrix via:

**File**: `compliance/backend/matrix/bridge.py` (to be implemented)

This bridge will use the Matrix homeserver running in the streams module to:
1. Create incident response rooms
2. Post human oversight alerts
3. Extract evidence from room messages
4. Coordinate security team communication

**See**:
- `/streams/config/matrix/README.md` - Complete Matrix documentation
- `/compliance/docs/research/ISMS-MATRIX-INTEGRATION-PLAN.md` - ISMS integration plan
- `/compliance/docs/research/COMPLIANCE_BACKEND_SPEC.md` - Backend architecture

## Migration Summary

**What Moved**:
- ✅ Matrix Synapse homeserver configuration
- ✅ Element web client configuration
- ✅ Matrix setup and integration documentation
- ✅ Docker compose service definitions
- ✅ Service manifest entries (now under `module: streams`)

**What Stayed**:
- ✅ ISMS-Matrix Integration Plan (compliance perspective)
- ✅ Compliance Backend Specification (Matrix bridge design)
- ✅ Compliance backend implementation (when created)

**Result**: Clean separation between **infrastructure** (streams) and **usage** (compliance).
