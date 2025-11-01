"""Context manager for scoped audit collection."""

import asyncio
from datetime import datetime
from typing import Any

from loguru import logger

from .audit_chain import AuditChain
from .audit_store import AuditStore
from .models import AuditFinding, AuditRecord, AuditSeverity, AuditTargetType, AuditViolation


class AuditContext:
    """Context manager for automatic audit trail creation."""

    def __init__(
        self,
        actor: str,
        action: str,
        target: str,
        target_type: str | AuditTargetType = AuditTargetType.FILE,
        source: str = "manual",
        reason: str | None = None,
        chain: AuditChain | None = None,
        store: AuditStore | None = None,
        auto_commit: bool = True,
    ) -> None:
        """
        Initialize audit context.

        Args:
            actor: Who is performing the action
            action: What action is being performed
            target: What is being targeted
            target_type: Type of target
            source: Source of the audit
            reason: Why the action is being performed
            chain: Audit chain to use (creates new if None)
            store: Audit store to use (creates new if None)
            auto_commit: Automatically commit record on context exit
        """
        self.actor = actor
        self.action = action
        self.target = target
        self.target_type = target_type if isinstance(target_type, AuditTargetType) else AuditTargetType(target_type)
        self.source = source
        self.reason = reason
        self.auto_commit = auto_commit

        # Create or use provided infrastructure
        self.chain = chain or AuditChain()
        self.store = store or AuditStore()

        # Runtime data
        self.start_time = datetime.utcnow()
        self.context: dict[str, Any] = {}
        self.metadata: dict[str, Any] = {}
        self.findings: list[AuditFinding] = []
        self.violations: list[AuditViolation] = []
        self.severity = AuditSeverity.INFO
        self.error: BaseException | None = None

        self.record: AuditRecord | None = None

    def __enter__(self) -> "AuditContext":
        """Enter audit context."""
        logger.debug(f"Audit context started: {self.action} on {self.target} by {self.actor}")
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: Any) -> None:
        """Exit audit context and create record if auto_commit enabled."""
        # Record exception if one occurred
        if exc_type is not None:
            self.error = exc_val
            self.severity = AuditSeverity.ERROR
            self.metadata["error_type"] = exc_type.__name__
            self.metadata["error_message"] = str(exc_val)

        # Calculate duration
        duration_ms = (datetime.utcnow() - self.start_time).total_seconds() * 1000
        self.metadata["duration_ms"] = duration_ms

        # Create and commit record if enabled
        if self.auto_commit:
            # Run async commit in sync context
            loop = asyncio.new_event_loop()
            try:
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self.commit())
            finally:
                loop.close()

        logger.debug(f"Audit context ended: {self.action} ({duration_ms:.2f}ms, severity={self.severity.value}, findings={len(self.findings)})")

    async def __aenter__(self) -> "AuditContext":
        """Enter async audit context."""
        return self.__enter__()

    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: Any) -> None:
        """Exit async audit context and create record if auto_commit enabled."""
        # Record exception if one occurred
        if exc_type is not None:
            self.error = exc_val
            self.severity = AuditSeverity.ERROR
            self.metadata["error_type"] = exc_type.__name__
            self.metadata["error_message"] = str(exc_val)

        # Calculate duration
        duration_ms = (datetime.utcnow() - self.start_time).total_seconds() * 1000
        self.metadata["duration_ms"] = duration_ms

        # Create and commit record if enabled
        if self.auto_commit:
            await self.commit()

        logger.debug(f"Audit context ended: {self.action} ({duration_ms:.2f}ms, severity={self.severity.value}, findings={len(self.findings)})")

    def add_context(self, key: str, value: Any) -> None:
        """
        Add context information.

        Args:
            key: Context key
            value: Context value
        """
        self.context[key] = value

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add metadata.

        Args:
            key: Metadata key
            value: Metadata value
        """
        self.metadata[key] = value

    def add_finding(self, finding: AuditFinding) -> None:
        """
        Add audit finding.

        Args:
            finding: Audit finding to add
        """
        self.findings.append(finding)

        # Escalate severity if needed
        if finding.severity.value == "critical":
            self.severity = AuditSeverity.CRITICAL
        elif finding.severity.value == "error" and self.severity.value not in {"critical"}:
            self.severity = AuditSeverity.ERROR
        elif finding.severity.value == "warning" and self.severity.value not in {"critical", "error"}:
            self.severity = AuditSeverity.WARNING

    def add_findings(self, findings: list[AuditFinding]) -> None:
        """
        Add multiple audit findings.

        Args:
            findings: List of findings to add
        """
        for finding in findings:
            self.add_finding(finding)

    def add_violation(self, violation: AuditViolation) -> None:
        """
        Add audit violation.

        Args:
            violation: Audit violation to add
        """
        self.violations.append(violation)

        # Escalate severity if needed
        if violation.severity.value == "critical":
            self.severity = AuditSeverity.CRITICAL
        elif violation.severity.value == "error" and self.severity.value not in {"critical"}:
            self.severity = AuditSeverity.ERROR

    def add_violations(self, violations: list[AuditViolation]) -> None:
        """
        Add multiple violations.

        Args:
            violations: List of violations to add
        """
        for violation in violations:
            self.add_violation(violation)

    async def commit(self) -> AuditRecord:
        """
        Create and commit audit record.

        Returns:
            Created audit record

        Raises:
            ValueError: If record creation fails
        """
        # Create audit record
        self.record = AuditRecord(
            actor=self.actor,
            action=self.action,
            target=self.target,
            target_type=self.target_type,
            source=self.source,
            reason=self.reason,
            context=self.context,
            metadata=self.metadata,
            findings=self.findings,
            violations=self.violations,
            severity=self.severity,
            timestamp=self.start_time,
        )

        # Add to chain
        self.record = await self.chain.add_record(self.record)

        # Store persistently
        await self.store.store_record(self.record)

        logger.info(f"Audit record committed: {self.record.record_id} (action={self.action}, severity={self.severity.value})")

        return self.record

    def get_record(self) -> AuditRecord | None:
        """
        Get the created audit record.

        Returns:
            Audit record if committed, None otherwise
        """
        return self.record
