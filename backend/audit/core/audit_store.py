"""Persistent storage for audit records with multiple backends."""

from typing import Any

from loguru import logger

from .models import AuditFilter, AuditRecord


class AuditStore:
    """
    Persistent storage for audit records.

    Supports multiple storage backends:
    - Dgraph: Provenance graph (relationships)
    - Postgres: Structured records (queryable)
    - Redis: Hot cache (recent records)
    """

    def __init__(
        self,
        postgres_url: str | None = None,
        dgraph_url: str | None = None,
        redis_url: str | None = None,
        enable_cache: bool = True,
    ) -> None:
        """
        Initialize audit store.

        Args:
            postgres_url: PostgreSQL connection URL
            dgraph_url: Dgraph connection URL
            redis_url: Redis connection URL
            enable_cache: Enable Redis caching
        """
        self.postgres_url = postgres_url
        self.dgraph_url = dgraph_url
        self.redis_url = redis_url
        self.enable_cache = enable_cache

        # In-memory fallback when databases not configured
        self._memory_store: dict[str, AuditRecord] = {}

        logger.info(
            f"Audit store initialized (postgres={'configured' if postgres_url else 'memory'}, "
            f"dgraph={'configured' if dgraph_url else 'memory'}, "
            f"cache={'enabled' if enable_cache else 'disabled'})"
        )

    async def store_record(self, record: AuditRecord) -> None:
        """
        Store audit record in all backends.

        Args:
            record: Audit record to store

        Raises:
            ValueError: If record is invalid
        """
        # Verify record before storing
        if not record.verify():
            msg = f"Cannot store invalid record: {record.record_id}"
            raise ValueError(msg)

        # Store in memory (always available)
        self._memory_store[record.record_id] = record

        # TODO: Store in Postgres when configured
        if self.postgres_url:
            await self._store_postgres(record)

        # TODO: Store in Dgraph when configured
        if self.dgraph_url:
            await self._store_dgraph(record)

        # TODO: Cache in Redis when configured
        if self.enable_cache and self.redis_url:
            await self._cache_redis(record)

        logger.debug(f"Stored audit record: {record.record_id} (action={record.action}, target={record.target})")

    async def get_record(self, record_id: str) -> AuditRecord | None:
        """
        Retrieve audit record by ID.

        Args:
            record_id: Record identifier

        Returns:
            Audit record if found, None otherwise
        """
        # Try cache first
        if self.enable_cache and self.redis_url:
            cached = await self._get_redis(record_id)
            if cached:
                return cached

        # Try memory store
        if record_id in self._memory_store:
            return self._memory_store[record_id]

        # Try Postgres
        if self.postgres_url:
            return await self._get_postgres(record_id)

        return None

    async def query_records(self, audit_filter: AuditFilter) -> list[AuditRecord]:
        """
        Query audit records with filters.

        Args:
            audit_filter: Filter criteria

        Returns:
            List of matching audit records
        """
        # For now, use in-memory filtering
        # TODO: Push filters to database for efficiency

        all_records = list(self._memory_store.values())

        # Apply filters
        matches = [record for record in all_records if audit_filter.matches(record)]

        # Sort by timestamp (newest first)
        matches.sort(key=lambda r: r.timestamp, reverse=True)

        # Apply limit and offset
        return matches[audit_filter.offset : audit_filter.offset + audit_filter.limit]

    async def get_provenance_chain(self, target: str) -> list[AuditRecord]:
        """
        Get complete provenance chain for a target.

        Args:
            target: Target identifier (file path, module name, etc.)

        Returns:
            List of audit records affecting this target, in chronological order
        """
        # Query all records for this target
        audit_filter = AuditFilter(limit=10000)  # Large limit for complete history

        all_records = await self.query_records(audit_filter)

        # Filter by target
        provenance = [record for record in all_records if record.target == target]

        # Sort chronologically (oldest first for provenance)
        provenance.sort(key=lambda r: r.timestamp)

        logger.debug(f"Found {len(provenance)} provenance records for target: {target}")

        return provenance

    async def verify_integrity(self) -> bool:
        """
        Verify integrity of stored records.

        Returns:
            True if all stored records are valid
        """
        invalid_count = 0

        for record_id, record in self._memory_store.items():
            if not record.verify():
                logger.error(f"Record {record_id} failed integrity check")
                invalid_count += 1

        if invalid_count > 0:
            logger.error(f"Found {invalid_count} invalid records in store")
            return False

        logger.info(f"All {len(self._memory_store)} records verified successfully")
        return True

    async def get_statistics(self) -> dict[str, Any]:
        """
        Get storage statistics.

        Returns:
            Dictionary with storage metrics
        """
        records = list(self._memory_store.values())

        if not records:
            return {
                "total_records": 0,
                "storage_backend": "memory",
            }

        return {
            "total_records": len(records),
            "storage_backend": "memory",
            "earliest_record": min(r.timestamp for r in records).isoformat(),
            "latest_record": max(r.timestamp for r in records).isoformat(),
            "total_findings": sum(len(r.findings) for r in records),
            "total_violations": sum(len(r.violations) for r in records),
            "signed_records": sum(1 for r in records if r.signatures),
        }

    # Private helper methods for database backends (to be implemented)

    async def _store_postgres(self, record: AuditRecord) -> None:
        """Store record in PostgreSQL."""
        # TODO: Implement PostgreSQL storage
        logger.debug(f"PostgreSQL storage not yet implemented for {record.record_id}")

    async def _store_dgraph(self, record: AuditRecord) -> None:
        """Store record in Dgraph."""
        # TODO: Implement Dgraph storage
        logger.debug(f"Dgraph storage not yet implemented for {record.record_id}")

    async def _cache_redis(self, record: AuditRecord) -> None:
        """Cache record in Redis."""
        # TODO: Implement Redis caching
        logger.debug(f"Redis caching not yet implemented for {record.record_id}")

    async def _get_redis(self, _record_id: str) -> AuditRecord | None:
        """Get record from Redis cache."""
        # TODO: Implement Redis retrieval
        return None

    async def _get_postgres(self, _record_id: str) -> AuditRecord | None:
        """Get record from PostgreSQL."""
        # TODO: Implement PostgreSQL retrieval
        return None
