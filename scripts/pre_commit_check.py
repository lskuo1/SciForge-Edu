"""
pre_commit_check.py

Purpose:
Run automated validation before git commit.

Responsibilities:

- Run pytest
- Generate API snapshot
- Show result summary
- Block commit if checks fail

Important notes:

- Executed automatically by git hooks
- Must run from project root
- Snapshot is updated before commit
"""

import os
import subprocess
import sys
from pathlib import Path


def run_pytest() -> bool:
    project_root = Path(__file__).resolve().parent.parent

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
    result = subprocess.run(
        ["python3", "scripts/generate_snapshot.py"]
    )

    return result.returncode == 0


def main():
    print("\nSciForge Pre-Commit Check\n")

    ok = run_pytest()

    if ok:
        snapshot_ok = update_snapshot()

        if not snapshot_ok:
            print("✗ Snapshot generation failed")
            sys.exit(1)

        print("✓ Snapshot updated")
        print("✓ Tests passed")
        sys.exit(0)

    print("✗ Tests failed")
    sys.exit(1)


if __name__ == "__main__":
    main()