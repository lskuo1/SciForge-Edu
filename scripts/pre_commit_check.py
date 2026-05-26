"""
pre_commit_check.py

Purpose:
Run automated validation before git commit.

Responsibilities:

- Run pytest
- Check API snapshot status
- Show validation results
- Block commit if checks fail

Important notes:

- Executed automatically by git hooks
- Must run from project root
- Does not modify repository files automatically
- Commit decisions remain controlled by users
"""

import os
import subprocess
import sys
from pathlib import Path


def run_pytest() -> bool:

    project_root = (
        Path(__file__)
        .resolve()
        .parent
        .parent
    )

    result = subprocess.run(
        [
            "python3",
            "-m",
            "pytest",
            "-q"
        ],
        cwd=project_root,
        env={
            **os.environ,
            "PYTHONPATH": str(
                project_root
            )
        }
    )

    return (
        result.returncode == 0
    )


def update_snapshot() -> bool:

    project_root = (
        Path(__file__)
        .resolve()
        .parent
        .parent
    )

    result = subprocess.run(
        [
            "python3",
            "scripts/generate_snapshot.py"
        ],
        cwd=project_root
    )

    return (
        result.returncode == 0
    )


def main():

    print(
        "\nSciForge Pre-Commit Check\n"
    )

    tests_ok = run_pytest()

    if not tests_ok:

        print(
            "\n✗ Tests failed"
        )

        sys.exit(1)

    snapshot_ok = (
        update_snapshot()
    )

    if not snapshot_ok:

        print(
            "\n⚠ API snapshot outdated"
        )

        print(
            "\nSuggested action:"
        )

        print(
            "git add docs/api_snapshot.md"
        )

        print(
            "\nSuggested suffix:"
        )

        print(
            "[snapshot updated]"
        )

        sys.exit(1)

    print(
        "\n✓ Tests passed"
    )

    print(
        "✓ Snapshot up to date"
    )

    sys.exit(0)


if __name__ == "__main__":
    main()