"""
pre_commit_check.py

Purpose:
Run automated checks before commit.

Responsibilities:

- Run pytest
- Show result summary
- Block commit if checks fail
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
            **dict(__import__("os").environ),
            "PYTHONPATH": str(project_root)
        }
    )

    return result.returncode == 0

def main():
    print("\nSciForge Pre-Commit Check\n")

    ok = run_pytest()

    if ok:
        print("✓ Tests passed")
        sys.exit(0)

    print("✗ Tests failed")
    sys.exit(1)


if __name__ == "__main__":
    main()