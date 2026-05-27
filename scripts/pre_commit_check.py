"""
pre_commit_check.py

Purpose:
Run automated pre-commit pipeline checks.

Responsibilities:

- Run pytest
- Synchronize API snapshots
- Stage updated snapshot files
- Show validation results
- Block commit when critical checks fail

Important notes:

- Executed automatically by git hooks
- Must run from project root
- Snapshot files are treated as system metadata
- Snapshot updates are automatic
"""

import os
import subprocess
import sys
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def run_pytest() -> bool:
    project_root = get_project_root()

    result = subprocess.run(
        ["python3", "-m", "pytest", "-q"],
        cwd=project_root,
        env={
            **os.environ,
            "PYTHONPATH": str(project_root)
        }
    )

    return result.returncode == 0


def update_snapshot() -> bool:
    project_root = get_project_root()

    result = subprocess.run(
        ["python3", "scripts/generate_snapshot.py"],
        cwd=project_root
    )

    return result.returncode == 2


def stage_snapshot():
    project_root = get_project_root()

    subprocess.run(
        ["git", "add", "docs/api_snapshot.md"],
        cwd=project_root
    )


def main():
    print("\nSciForge Pre-Commit Check\n")

    if not run_pytest():
        print("\n✗ Tests failed")
        print("✗ Commit aborted")

        sys.exit(1)

    print("\n✓ Tests passed")

    snapshot_updated = update_snapshot()

    if snapshot_updated:
        stage_snapshot()

        print("\nℹ API snapshot updated")
        print("✓ docs/api_snapshot.md staged")

        print("\nSuggested suffix:")
        print("[snapshot updated]")

    else:
        print("✓ Snapshot up to date")

    sys.exit(0)


if __name__ == "__main__":
    main()