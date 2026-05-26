"""
generate_snapshot.py

Purpose:
Generate temporary API snapshots and detect
whether the official snapshot is outdated.

Responsibilities:

- Generate API snapshot content
- Save temporary snapshot
- Compare with official snapshot
- Return snapshot status

Important notes:

- API snapshot is the source of truth for AI context
- Temporary snapshots are stored in docs/.generated/
- This module does NOT modify official snapshots
- Commit decisions remain controlled by users
"""

from pathlib import Path


def generate_snapshot() -> bool:

    project_root = (
        Path(__file__)
        .resolve()
        .parent
        .parent
    )

    generated_dir = (
        project_root
        / "docs"
        / ".generated"
    )

    generated_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    generated_file = (
        generated_dir
        / "api_snapshot.md"
    )

    official_file = (
        project_root
        / "docs"
        / "api_snapshot.md"
    )

    content = """# SciForge API Snapshot

Snapshot version: 0.2

Status:
Temporary test
"""

    generated_file.write_text(
        content,
        encoding="utf-8"
    )

    old_content = ""

    if official_file.exists():

        old_content = (
            official_file.read_text(
                encoding="utf-8"
            )
        )

    return old_content == content


def main():
    generate_snapshot()


if __name__ == "__main__":
    main()