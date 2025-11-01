"""Core audit data models and enumerations."""

import hashlib
import json
import uuid
from datetime import UTC, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class AuditTargetType(str, Enum):
    """Type of audit target."""

    FILE = "file"
    MODULE = "module"
    SERVICE = "service"
    LOG = "log"
    GIT = "git"
    QUALITY = "quality"


class AuditSeverity(str, Enum):
    """Audit event severity level."""

    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class AuditStatus(str, Enum):
    """Audit record processing status."""

    RECORDED = "recorded"
    ANALYZED = "analyzed"
    VERIFIED = "verified"
    EXPORTED = "exported"


class DataClassification(str, Enum):
    """Data classification levels."""

    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"


class AuditSignature(BaseModel):
    """Cryptographic signature for audit record."""

    signer: str
    signature: str
    algorithm: str = "Ed25519"
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        """Pydantic config."""

        frozen = True


class AuditFinding(BaseModel):
    """Analysis finding from audit analyzers."""

    finding_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    finding_type: str
    severity: AuditSeverity
    description: str
    location: str | None = None
    recommendation: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    class Config:
        """Pydantic config."""

        frozen = True


class AuditViolation(BaseModel):
    """Code quality or security violation."""

    violation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    rule: str
    severity: AuditSeverity
    message: str
    file_path: str | None = None
    line_number: int | None = None
    column_number: int | None = None

    class Config:
        """Pydantic config."""

        frozen = True


class AuditRecord(BaseModel):
    """Immutable audit record representing a single auditable event."""

    # Identity
    record_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    record_hash: str = ""

    # Provenance metadata
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    actor: str  # Who performed the action
    action: str  # What action was performed
    target: str  # What was targeted
    target_type: AuditTargetType
    source: str  # How audit was collected
    reason: str | None = None  # Why action was taken

    # Context
    context: dict[str, Any] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)

    # Chain linkage
    previous_hash: str = "0"
    nonce: int = 0

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

    def __init__(self, **data: Any) -> None:
        """Initialize audit record and calculate hash if not provided."""
        super().__init__(**data)
        if not self.record_hash:
            object.__setattr__(self, "record_hash", self.calculate_hash())

    def calculate_hash(self) -> str:
        """
        Calculate SHA-256 hash of record content.

        Returns:
            Hex digest of record hash
        """
        # Create deterministic JSON representation
        hash_content = {
            "record_id": self.record_id,
            "timestamp": self.timestamp.isoformat(),
            "actor": self.actor,
            "action": self.action,
            "target": self.target,
            "target_type": self.target_type.value,
            "source": self.source,
            "reason": self.reason,
            "context": self.context,
            "metadata": self.metadata,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "severity": self.severity.value,
            "classification": self.classification.value,
            "status": self.status.value,
        }

        # Sort keys for deterministic output
        json_str = json.dumps(hash_content, sort_keys=True, default=str)
        return hashlib.sha256(json_str.encode()).hexdigest()

    def mine_block(self, difficulty: int = 2) -> None:
        """
        Perform proof-of-work mining to add computational cost.

        Args:
            difficulty: Number of leading zeros required in hash
        """
        target = "0" * difficulty
        while not self.record_hash.startswith(target):
            object.__setattr__(self, "nonce", self.nonce + 1)
            object.__setattr__(self, "record_hash", self.calculate_hash())

    def verify(self) -> bool:
        """
        Verify record integrity by recalculating hash.

        Returns:
            True if record hash is valid
        """
        return self.record_hash == self.calculate_hash()

    def sign(self, private_key: str, signer: str) -> None:
        """
        Add cryptographic signature to record.

        Args:
            private_key: Private key for signing (Ed25519)
            signer: Identity of signer

        Note:
            In production, use proper Ed25519 implementation.
            This is a temporary implementation that creates a deterministic signature.
        """
        # Create signature from record hash
        signature_input = f"{self.record_hash}{signer}{private_key}"
        signature = hashlib.sha256(signature_input.encode()).hexdigest()

        sig = AuditSignature(
            signer=signer,
            signature=signature,
            algorithm="Ed25519",
            timestamp=datetime.now(UTC),
        )

        # Create new list with added signature (since frozen)
        object.__setattr__(self, "signatures", [*self.signatures, sig])

    def verify_signatures(self) -> bool:
        """
        Verify all signatures on record.

        Returns:
            True if all signatures are valid

        Note:
            In production, use proper Ed25519 verification.
            This temporary implementation just checks that signature is non-empty and valid hex.
        """
        sha256_hex_length = 64  # SHA-256 produces 64 hex characters

        for sig in self.signatures:
            # Temporary verification - just check format
            if not sig.signature or len(sig.signature) != sha256_hex_length:
                return False
            try:
                int(sig.signature, 16)  # Verify it's valid hex
            except ValueError:
                return False
        return True

    class Config:
        """Pydantic config."""

        # Not frozen to allow chain linkage and mining
        frozen = False
        use_enum_values = False


class AuditFilter(BaseModel):
    """Filter criteria for querying audit records."""

    target_type: AuditTargetType | None = None
    action: str | None = None
    actor: str | None = None
    severity: AuditSeverity | None = None
    since: datetime | None = None
    until: datetime | None = None
    limit: int = 100
    offset: int = 0

    def matches(self, record: AuditRecord) -> bool:
        """
        Check if a record matches this filter.

        Args:
            record: Audit record to check

        Returns:
            True if record matches all filter criteria
        """
        if self.target_type and record.target_type != self.target_type:
            return False

        if self.action and record.action != self.action:
            return False

        if self.actor and record.actor != self.actor:
            return False

        if self.severity and record.severity != self.severity:
            return False

        if self.since and record.timestamp < self.since:
            return False

        return not (self.until and record.timestamp > self.until)


class AuditOptions(BaseModel):
    """Options for audit collection."""

    since: datetime | None = None
    until: datetime | None = None
    pattern: bool = False
    include_git: bool = False
    include_hash: bool = True
    include_blame: bool = False
    include_dependencies: bool = False
    include_tests: bool = False
    include_health: bool = False
    include_logs: bool = False
    check_banned_words: bool = False
    run_ruff: bool = False
    run_mypy: bool = False
    authors: list[str] = Field(default_factory=list)
    level: str | None = None
