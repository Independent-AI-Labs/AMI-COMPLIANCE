"""Blockchain-style immutable audit chain with cryptographic verification."""

import json
from datetime import datetime
from typing import Any

import yaml
from loguru import logger

from .models import AuditFilter, AuditRecord, AuditTargetType


class AuditChain:
    """Blockchain-style immutable chain of audit records."""

    def __init__(self, difficulty: int = 2) -> None:
        """
        Initialize audit chain.

        Args:
            difficulty: Mining difficulty for proof-of-work (number of leading zeros)
        """
        self.chain: list[AuditRecord] = []
        self.difficulty = difficulty

        # Create genesis record
        genesis = AuditRecord(
            actor="system",
            action="genesis",
            target="audit_chain",
            target_type=AuditTargetType.GIT,
            source="system",
            reason="Initialize audit chain",
            previous_hash="0",
        )
        genesis.mine_block(self.difficulty)
        self.chain.append(genesis)

        logger.info(f"Audit chain initialized with genesis record: {genesis.record_hash[:16]}...")

    def get_latest_record(self) -> AuditRecord:
        """
        Get the latest record in chain.

        Returns:
            Most recent audit record
        """
        return self.chain[-1]

    async def add_record(self, record: AuditRecord) -> AuditRecord:
        """
        Add new record to chain with proof-of-work.

        Args:
            record: Audit record to add (will be modified to link to chain)

        Returns:
            The added record with updated hash and nonce
        """
        # Link to previous record
        latest = self.get_latest_record()
        object.__setattr__(record, "previous_hash", latest.record_hash)
        # Recalculate hash after updating previous_hash
        object.__setattr__(record, "record_hash", record.calculate_hash())

        # Mine the record (proof-of-work)
        record.mine_block(self.difficulty)

        # Verify before adding
        if not record.verify():
            msg = "Record verification failed before adding to chain"
            raise ValueError(msg)

        # Add to chain
        self.chain.append(record)

        logger.info(f"Added audit record: {record.record_hash[:16]}... (action={record.action}, target={record.target}, actor={record.actor})")

        return record

    def verify_chain(self) -> bool:
        """
        Verify entire chain integrity.

        Returns:
            True if chain is cryptographically valid

        Raises:
            ValueError: If chain verification fails
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Verify current record hash
            if not current.verify():
                logger.error(f"Record {i} ({current.record_id}) failed hash verification")
                return False

            # Verify link to previous record
            if current.previous_hash != previous.record_hash:
                logger.error(
                    f"Record {i} ({current.record_id}) has invalid previous_hash. Expected {previous.record_hash[:16]}..., got {current.previous_hash[:16]}..."
                )
                return False

            # Verify proof-of-work
            if not current.record_hash.startswith("0" * self.difficulty):
                logger.error(f"Record {i} ({current.record_id}) has insufficient proof-of-work")
                return False

        logger.info(f"Audit chain verified successfully ({len(self.chain)} records)")
        return True

    def get_chain_slice(self, start: datetime, end: datetime) -> list[AuditRecord]:
        """
        Get slice of chain within time range.

        Args:
            start: Start timestamp (inclusive)
            end: End timestamp (inclusive)

        Returns:
            List of records within time range
        """
        return [
            record
            for record in self.chain[1:]  # Skip genesis
            if start <= record.timestamp <= end
        ]

    def find_records(self, audit_filter: AuditFilter) -> list[AuditRecord]:
        """
        Find records matching filter criteria.

        Args:
            audit_filter: Filter criteria

        Returns:
            List of matching records (limited by filter.limit)
        """
        matches = []
        checked = 0

        # Search from newest to oldest (skip genesis)
        for record in reversed(self.chain[1:]):
            checked += 1

            # Skip records outside time range first (optimization)
            if audit_filter.since and record.timestamp < audit_filter.since:
                continue
            if audit_filter.until and record.timestamp > audit_filter.until:
                continue

            # Check other filters
            if audit_filter.matches(record):
                matches.append(record)

            # Stop if we hit the limit
            if len(matches) >= audit_filter.limit:
                break

        # Apply offset
        matches = matches[audit_filter.offset :]

        logger.debug(f"Found {len(matches)} matching records (checked {checked}, limit={audit_filter.limit})")

        return matches

    def export_chain(self, export_format: str = "json") -> str:
        """
        Export entire chain in specified format.

        Args:
            export_format: Export format (json, yaml, csv)

        Returns:
            Serialized chain

        Raises:
            ValueError: If format is not supported
        """
        if export_format == "json":
            return json.dumps(
                [record.model_dump(mode="json") for record in self.chain],
                indent=2,
                default=str,
            )
        if export_format == "yaml":
            return yaml.dump(
                [record.model_dump(mode="json") for record in self.chain],
                default_flow_style=False,
            )
        msg = f"Unsupported export format: {export_format}"
        raise ValueError(msg)

    def verify_signatures(self) -> dict[str, bool]:
        """
        Verify all signatures in chain.

        Returns:
            Dictionary mapping record_id to signature validity
        """
        results = {}

        for record in self.chain:
            if record.signatures:
                results[record.record_id] = record.verify_signatures()
            else:
                results[record.record_id] = True  # No signatures = valid

        return results

    def get_statistics(self) -> dict[str, Any]:
        """
        Get chain statistics.

        Returns:
            Dictionary with chain metrics
        """
        if len(self.chain) <= 1:
            return {
                "total_records": 0,
                "earliest_timestamp": None,
                "latest_timestamp": None,
                "unique_actors": 0,
                "unique_actions": 0,
            }

        records = self.chain[1:]  # Exclude genesis

        return {
            "total_records": len(records),
            "earliest_timestamp": min(r.timestamp for r in records).isoformat(),
            "latest_timestamp": max(r.timestamp for r in records).isoformat(),
            "unique_actors": len({r.actor for r in records}),
            "unique_actions": len({r.action for r in records}),
            "severity_counts": {severity: sum(1 for r in records if r.severity == severity) for severity in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")},
        }
