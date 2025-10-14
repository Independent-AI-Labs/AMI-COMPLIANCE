"""Pytest configuration for compliance tests."""

import sys
from pathlib import Path


def _setup_paths() -> None:
    """Setup sys.path for tests using iterative directory traversal."""
    current = Path(__file__).resolve()

    # Walk up to find .git (compliance submodule root)
    git_root = None
    search = current
    while search != search.parent:
        if (search / ".git").exists():
            git_root = search
            break
        search = search.parent

    if git_root:
        sys.path.insert(0, str(git_root))

    # Walk up to find orchestrator root (has base/ and .git)
    orchestrator_root = None
    search = current
    while search != search.parent:
        if (search / "base").exists() and (search / ".git").exists():
            orchestrator_root = search
            break
        search = search.parent

    if orchestrator_root:
        sys.path.insert(0, str(orchestrator_root))


_setup_paths()
