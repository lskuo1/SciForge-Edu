"""
pre_commit_check.py

Purpose:
Run automated checks before commit.

Responsibilities:

- Run pytest
- Show result summary
- Block commit if checks fail
"""

import subprocess
import sys


def run_pytest() -> bool:
    result = subprocess.run(
        ["pytest", "-q"]
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