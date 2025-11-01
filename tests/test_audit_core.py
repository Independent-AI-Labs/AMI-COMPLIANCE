"""Tests for core audit trail components."""

import asyncio
from datetime import datetime, timedelta

import pytest
from compliance.backend.audit.core import (
    AuditChain,
    AuditContext,
    AuditFilter,
    AuditFinding,
    AuditRecord,
    AuditSeverity,
    AuditStore,
    AuditTargetType,
    AuditViolation,
)


class TestAuditRecord:
    """Tests for AuditRecord model."""

    def test_create_record(self) -> None:
        """Test creating an audit record."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test_source",
        )

        assert record.actor == "test_user"
        assert record.action == "test_action"
        assert record.target == "test_target"
        assert record.target_type == AuditTargetType.FILE
        assert record.source == "test_source"
        assert record.record_hash  # Hash should be calculated
        assert record.record_id  # ID should be generated

    def test_hash_calculation(self) -> None:
        """Test that hash is calculated correctly."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test_source",
        )

        # Recalculate hash
        calculated_hash = record.calculate_hash()
        assert calculated_hash == record.record_hash

    def test_verify_record(self) -> None:
        """Test record verification."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test_source",
        )

        assert record.verify() is True

    def test_mine_block(self) -> None:
        """Test proof-of-work mining."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test_source",
        )

        difficulty = 2
        record.mine_block(difficulty)

        # Check that hash starts with required zeros
        assert record.record_hash.startswith("0" * difficulty)
        assert record.nonce > 0  # Should have incremented nonce

    def test_sign_and_verify(self) -> None:
        """Test signing and verifying record."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test_source",
        )

        # Sign record
        record.sign("test_private_key", "test_signer")

        assert len(record.signatures) == 1
        assert record.signatures[0].signer == "test_signer"
        assert record.verify_signatures() is True


class TestAuditChain:
    """Tests for AuditChain."""

    @pytest.fixture
    def chain(self) -> AuditChain:
        """Create a test chain."""
        return AuditChain(difficulty=1)

    @pytest.mark.asyncio
    async def test_create_chain(self, chain: AuditChain) -> None:
        """Test creating a chain."""
        assert len(chain.chain) == 1  # Should have genesis record
        assert chain.chain[0].action == "genesis"

    @pytest.mark.asyncio
    async def test_add_record(self, chain: AuditChain) -> None:
        """Test adding a record to chain."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test_source",
        )

        added_record = await chain.add_record(record)

        assert len(chain.chain) == 2
        assert added_record.previous_hash == chain.chain[0].record_hash
        assert added_record.record_hash.startswith("0" * chain.difficulty)

    @pytest.mark.asyncio
    async def test_verify_chain(self, chain: AuditChain) -> None:
        """Test verifying chain integrity."""
        # Add some records
        for i in range(5):
            record = AuditRecord(
                actor=f"user_{i}",
                action=f"action_{i}",
                target=f"target_{i}",
                target_type=AuditTargetType.FILE,
                source="test",
            )
            await chain.add_record(record)

        assert chain.verify_chain() is True

    @pytest.mark.asyncio
    async def test_get_chain_slice(self, chain: AuditChain) -> None:
        """Test getting a time slice of the chain."""
        start_time = datetime.utcnow()

        # Add records
        for i in range(3):
            record = AuditRecord(
                actor=f"user_{i}",
                action=f"action_{i}",
                target=f"target_{i}",
                target_type=AuditTargetType.FILE,
                source="test",
            )
            await chain.add_record(record)
            await asyncio.sleep(0.01)  # Small delay

        end_time = datetime.utcnow()

        # Get slice
        records = chain.get_chain_slice(start_time, end_time)
        assert len(records) == 3  # Should get all 3 records (not genesis)

    @pytest.mark.asyncio
    async def test_find_records(self, chain: AuditChain) -> None:
        """Test finding records with filters."""
        # Add records with different actors
        for i in range(5):
            record = AuditRecord(
                actor="user_1" if i < 3 else "user_2",
                action=f"action_{i}",
                target=f"target_{i}",
                target_type=AuditTargetType.FILE,
                source="test",
            )
            await chain.add_record(record)

        # Find records by actor
        audit_filter = AuditFilter(actor="user_1", limit=10)
        records = chain.find_records(audit_filter)

        assert len(records) == 3
        assert all(r.actor == "user_1" for r in records)

    @pytest.mark.asyncio
    async def test_export_chain(self, chain: AuditChain) -> None:
        """Test exporting chain."""
        # Add a record
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test",
        )
        await chain.add_record(record)

        # Export as JSON
        json_export = chain.export_chain(export_format="json")
        assert json_export
        assert "genesis" in json_export

        # Export as YAML
        yaml_export = chain.export_chain(export_format="yaml")
        assert yaml_export
        assert "genesis" in yaml_export


class TestAuditStore:
    """Tests for AuditStore."""

    @pytest.fixture
    def store(self) -> AuditStore:
        """Create a test store."""
        return AuditStore()

    @pytest.mark.asyncio
    async def test_store_record(self, store: AuditStore) -> None:
        """Test storing a record."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test",
        )

        await store.store_record(record)

        # Retrieve it
        retrieved = await store.get_record(record.record_id)
        assert retrieved is not None
        assert retrieved.record_id == record.record_id

    @pytest.mark.asyncio
    async def test_query_records(self, store: AuditStore) -> None:
        """Test querying records."""
        # Store multiple records
        for i in range(5):
            record = AuditRecord(
                actor=f"user_{i}",
                action="test_action",
                target=f"target_{i}",
                target_type=AuditTargetType.FILE,
                source="test",
            )
            await store.store_record(record)

        # Query all
        audit_filter = AuditFilter(limit=10)
        records = await store.query_records(audit_filter)

        assert len(records) == 5

    @pytest.mark.asyncio
    async def test_get_provenance_chain(self, store: AuditStore) -> None:
        """Test getting provenance chain for a target."""
        target = "test_file.py"

        # Store records for the same target
        for i in range(3):
            record = AuditRecord(
                actor=f"user_{i}",
                action=f"action_{i}",
                target=target,
                target_type=AuditTargetType.FILE,
                source="test",
            )
            await store.store_record(record)

        # Get provenance
        provenance = await store.get_provenance_chain(target)

        assert len(provenance) == 3
        assert all(r.target == target for r in provenance)
        # Should be in chronological order
        assert provenance[0].timestamp <= provenance[-1].timestamp

    @pytest.mark.asyncio
    async def test_verify_integrity(self, store: AuditStore) -> None:
        """Test verifying store integrity."""
        # Store some records
        for i in range(3):
            record = AuditRecord(
                actor=f"user_{i}",
                action="test_action",
                target=f"target_{i}",
                target_type=AuditTargetType.FILE,
                source="test",
            )
            await store.store_record(record)

        # Verify integrity
        assert await store.verify_integrity() is True


class TestAuditContext:
    """Tests for AuditContext."""

    @pytest.mark.asyncio
    async def test_basic_context(self) -> None:
        """Test basic context usage."""
        async with AuditContext(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
        ) as ctx:
            ctx.add_context("key", "value")
            ctx.add_metadata("meta_key", "meta_value")

        # Record should be created
        record = ctx.get_record()
        assert record is not None
        assert record.actor == "test_user"
        assert record.context["key"] == "value"
        assert record.metadata["meta_key"] == "meta_value"

    @pytest.mark.asyncio
    async def test_context_with_findings(self) -> None:
        """Test context with findings."""
        async with AuditContext(
            actor="test_user",
            action="quality_check",
            target="test_file.py",
            target_type=AuditTargetType.FILE,
        ) as ctx:
            finding = AuditFinding(
                finding_type="quality_issue",
                severity=AuditSeverity.WARNING,
                description="Test finding",
            )
            ctx.add_finding(finding)

        record = ctx.get_record()
        assert record is not None
        assert len(record.findings) == 1
        assert record.severity == AuditSeverity.WARNING

    @pytest.mark.asyncio
    async def test_context_with_violations(self) -> None:
        """Test context with violations."""
        async with AuditContext(
            actor="test_user",
            action="code_scan",
            target="test_file.py",
            target_type=AuditTargetType.FILE,
        ) as ctx:
            violation = AuditViolation(
                rule="no-unused-vars",
                severity=AuditSeverity.ERROR,
                message="Unused variable detected",
                file_path="test_file.py",
                line_number=42,
            )
            ctx.add_violation(violation)

        record = ctx.get_record()
        assert record is not None
        assert len(record.violations) == 1
        assert record.severity == AuditSeverity.ERROR

    @pytest.mark.asyncio
    async def test_context_with_exception(self) -> None:
        """Test context when exception occurs."""
        try:
            async with AuditContext(
                actor="test_user",
                action="failing_action",
                target="test_target",
                target_type=AuditTargetType.FILE,
            ) as ctx:
                msg = "Test error"
                raise ValueError(msg)
        except ValueError:
            pass

        record = ctx.get_record()
        assert record is not None
        assert record.severity == AuditSeverity.ERROR
        assert "error_type" in record.metadata
        assert record.metadata["error_type"] == "ValueError"

    @pytest.mark.asyncio
    async def test_manual_commit(self) -> None:
        """Test manual commit without auto_commit."""
        ctx = AuditContext(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            auto_commit=False,
        )

        ctx.add_context("key", "value")

        # Should not be committed yet
        assert ctx.get_record() is None

        # Manual commit
        record = await ctx.commit()

        assert record is not None
        assert ctx.get_record() is not None


class TestAuditFilter:
    """Tests for AuditFilter."""

    def test_filter_matches(self) -> None:
        """Test filter matching logic."""
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test",
            severity=AuditSeverity.INFO,
        )

        # Should match
        audit_filter = AuditFilter(actor="test_user")
        assert audit_filter.matches(record) is True

        # Should not match
        audit_filter = AuditFilter(actor="other_user")
        assert audit_filter.matches(record) is False

    def test_filter_time_range(self) -> None:
        """Test filtering by time range."""
        now = datetime.utcnow()
        record = AuditRecord(
            actor="test_user",
            action="test_action",
            target="test_target",
            target_type=AuditTargetType.FILE,
            source="test",
            timestamp=now,
        )

        # Should match - within range
        audit_filter = AuditFilter(
            since=now - timedelta(hours=1),
            until=now + timedelta(hours=1),
        )
        assert audit_filter.matches(record) is True

        # Should not match - before range
        audit_filter = AuditFilter(since=now + timedelta(hours=1))
        assert audit_filter.matches(record) is False

        # Should not match - after range
        audit_filter = AuditFilter(until=now - timedelta(hours=1))
        assert audit_filter.matches(record) is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
